#%% Import
import time
from tkinter import getboolean
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.constants as spc
import itertools
import pathlib
import shutil

from datetime import datetime
from pprint import pprint
from configparser import ConfigParser

from drama import ares
from drama import utils

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
CONFIG_DIR = SCRIPT_DIR / "config"

utils.config_file_paths_dict["macos"] = [str(CONFIG_DIR) + "/{}/config.json"]

ares._default_input_lines = {
    "ares.inp": {
        "id": (0, 0, lambda x: str(x)),
        "functionality": (3, 0, lambda x: str(x)),
        "particle_size_min": (4, 0, lambda x: str(x)),
        "particle_size_max": (5, 0, lambda x: str(x)),
        "radar_wavelength": (16, 0, lambda x: str(x)),
        "EMR_switch": (20, 0, lambda x: str(x)),
        "min_EMR_ratio": (21, 0, lambda x: str(x)),
        "mass": (22, 0, lambda x: str(x)),
        "spacecraft_radius": (23, 0, lambda x: str(x)),
        "sma": (24, 0, lambda x: str(x)),
        "ecc": (25, 0, lambda x: str(x)),
        "inc": (26, 0, lambda x: str(x)),
        "raan": (27, 0, lambda x: str(x)),
        "aop": (28, 0, lambda x: str(x)),
        "epoch": (29, (0, 1, 2), lambda x: x.strftime("%Y %m %d")),
        "uncertainty_type": (30, 0, lambda x: str(x)),
        "uncertainty_along": (31, 0, lambda x: str(x)),
        "uncertainty_cross": (32, 0, lambda x: str(x)),
        "uncertainty_radial": (33, 0, lambda x: str(x)),
        "lead_time": (34, 0, lambda x: str(x)),
        "type_of_catalogue": (35, 0, lambda x: str(x)),
        "scaling_factor": (72, 0, lambda x: str(x)),
        "collision_probability_alogrithm": (111, 0, lambda x: str(x)),
        "avoidance_manoeuvre_criteria": (112, 0, lambda x: str(x)),
        "target_collision_probability_level": (113, 0, lambda x: str(x)),
        "allowed_minimum_miss_distance": (114, 0, lambda x: str(x))
    },
    "ares.cfg": {
        "ARESMASTERDataDirectory": (3, 1, lambda x: (x + "/", True)),
        "input_focus": (4, 1, lambda x: (x + "/", True)),
    },
}

parameter_config = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
parameter_config.read("ares_config.ini")

def update_line_column(line_no, column, lines, value_str):
    """Update a column value in ARES input file"""

    line = lines[line_no].split()
    line[column] = value_str
    line = " " + " ".join(line) + "\n"
    lines[line_no] = line
    return lines

#Get the parameters min_order, max_order and n_steps out of the function update_acpl_param() in order to collect them in input_parameters_collection
acpl_input = {}
def update_acpl_param(lines, min_order, max_order, n_steps):
    """Update ACPL evaluation array"""

    if n_steps > 10:
        raise ValueError("Only values upto 10 accepted.")

    params = np.logspace(min_order, max_order, n_steps)
    acpl_input.update({"min_order": min_order, "max_order": max_order, "n_steps" : n_steps})
    # :d changes n_steps to integer
    lines = update_line_column(280, 0, lines, "{:d}".format(n_steps))
    lines[281] = "x " * n_steps
    for i in range(n_steps):
        lines = update_line_column(281, i, lines, "{:2.1e}".format(params[i]))
    return lines

def update_covariance_matrix(lines):
    """Update covariance matrix"""

    covariance_matrix = np.reshape([float(i) for i in parameter_config.getlist('debris_uncertainty', 'covariance_matrix')], (36, 18))
    covariance_matrix = covariance_matrix * float(parameter_config["debris_uncertainty"]["covariance_matrix_factor"])
    
    line_counter = 172
    k = 0
    while line_counter <= 207:
        lines[line_counter] = "x " * 18
        for i in range(18):
            lines = update_line_column(line_counter, i, lines, "{:.2f}".format(covariance_matrix[k][i]))
        line_counter = line_counter + 1
        k = k + 1
    return lines

scaling_factor_table_for_input_file = []
def update_scaling_factor_table(lines, scaling_factor):
    """Update scaling factor table"""

    scaling_factor_table = np.reshape([float(i) for i in parameter_config.getlist('debris_uncertainty', 'scaling_factor_table')], (36, 6))

    scaling_factor_table[int(parameter_config["debris_uncertainty"]["a"]):int(parameter_config["debris_uncertainty"]["b"]),
    int(parameter_config["debris_uncertainty"]["c"]):int(parameter_config["debris_uncertainty"]["d"])] = scaling_factor
    scaling_factor_table[int(parameter_config["debris_uncertainty"]["e"]):int(parameter_config["debris_uncertainty"]["f"]), 
    int(parameter_config["debris_uncertainty"]["g"]):int(parameter_config["debris_uncertainty"]["h"])] = scaling_factor
    scaling_factor_table[int(parameter_config["debris_uncertainty"]["i"]):int(parameter_config["debris_uncertainty"]["j"]), 
    int(parameter_config["debris_uncertainty"]["k"]):int(parameter_config["debris_uncertainty"]["l"])] = scaling_factor
    
    #scaling_factor_table[:, :] = scaling_factor

    scaling_factor_table_for_input_file.append(scaling_factor_table)

    line_counter = 234
    k = 0
    while line_counter <= 269:
        lines[line_counter] = "x " * 6
        for i in range(6):
            lines = update_line_column(line_counter, i, lines, "{:.2f}".format(scaling_factor_table[k][i]))
        line_counter = line_counter + 1
        k = k + 1
    return lines

acpl_min_order = float(parameter_config["acpl"]["acpl_min_order"])
acpl_max_order = float(parameter_config["acpl"]["acpl_max_order"])
acpl_steps = int(parameter_config["acpl"]["acpl_steps"])
def update_default_config(d_ref=0.32, h_ref=2000, scaling_factor = 1):
    template_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares_template.inp"
    input_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares.inp"
    with open(template_path, "r") as f:
        lines = f.readlines()
    lines = update_line_column(69, 0, lines, "{:3.2e}".format(d_ref))
    lines = update_line_column(70, 0, lines, "{:3.2e}".format(h_ref))
    lines = update_acpl_param(lines, min_order=acpl_min_order, max_order=acpl_max_order, n_steps = acpl_steps)
    lines = update_covariance_matrix(lines)
    lines = update_scaling_factor_table(lines, scaling_factor)

    with open(input_path, "w") as f:
        f.writelines(lines)


def run(config, dependent_variables, d_ref, h_ref, scaling_factor):
    update_default_config(d_ref=d_ref, h_ref=h_ref, scaling_factor = scaling_factor)
    return ares.run(config, dependent_variables, parallel=parameter_config.getboolean("parallel_computation", "parallel"))

def main():
    start = time.time()
    #%% Run demo
    _R_EARTH = 6378.137
    year = [int(i) for i in parameter_config.getlist('parameters', 'year')]
    month = [int(i) for i in parameter_config.getlist('parameters', 'month')]
    day = [int(i) for i in parameter_config.getlist('parameters', 'day')]
    epoch_list = []
    for i in range(len(year)):
        epoch_list.append(datetime(year[i], month[i], day[i]))
    config = {
        "functionality": [int(i) for i in parameter_config.getlist('parameters', 'functionality')],
        "particle_size_min": [float(i) for i in parameter_config.getlist('parameters', 'particle_size_min')],
        "particle_size_max": [float(i) for i in parameter_config.getlist('parameters', 'particle_size_max')],
        "radar_wavelength": [float(i) for i in parameter_config.getlist('parameters', 'radar_wavelength')],
        "EMR_switch": [int(i) for i in parameter_config.getlist('parameters', 'EMR_switch')],
        "min_EMR_ratio": [float(i) for i in parameter_config.getlist('parameters', 'min_EMR_ratio')],
        "mass": [float(i) for i in parameter_config.getlist('parameters', 'mass')],
        "spacecraft_radius": [float(i) for i in parameter_config.getlist('parameters', 'spacecraft_radius')],
        "sma": list(np.array([float(i) for i in parameter_config.getlist('parameters', 'altitude')]) + _R_EARTH),
        "inc": [float(i) for i in parameter_config.getlist('parameters', 'inc')],
        "ecc": [float(i) for i in parameter_config.getlist('parameters', 'ecc')],
        "raan": [float(i) for i in parameter_config.getlist('parameters', 'raan')],
        "aop": [float(i) for i in parameter_config.getlist('parameters', 'aop')],
        "epoch": epoch_list,
        "uncertainty_type": [int(i) for i in parameter_config.getlist('parameters', 'uncertainty_type')],
        "uncertainty_along": [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_along')],
        "uncertainty_cross": [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_cross')],
        "uncertainty_radial": [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_radial')],
        "lead_time": [float(i) for i in parameter_config.getlist('parameters', 'lead_time')],
        "type_of_catalogue": [int(i) for i in parameter_config.getlist('parameters', 'type_of_catalogue')],
        "scaling_factor": [float(i) for i in parameter_config.getlist('parameters', 'scaling_factor')],
        "collision_probability_alogrithm": [int(i) for i in parameter_config.getlist('parameters', 'collision_probability_alogrithm')],
        "avoidance_manoeuvre_criteria": [int(i) for i in parameter_config.getlist('parameters', 'avoidance_manoeuvre_criteria')],
        "target_collision_probability_level": [float(i) for i in parameter_config.getlist('parameters', 'target_collision_probability_level')],
        "allowed_minimum_miss_distance": [float(i) for i in parameter_config.getlist('parameters', 'allowed_minimum_miss_distance')]
    }

    if parameter_config.getboolean("dependent_variables", "dependent_variable_mode") == True:
        dependent_variables = [[str(parameter_config["dependent_variables"]["variable_1"]), str(parameter_config["dependent_variables"]["variable_2"])]]
    else:
        dependent_variables = []

    annual_collision_p = []
    acpl = []
    f_rem_risk = []
    f_res_risk = []
    f_risk_red = []
    false_alarm_rate = []
    man_rate = []
    rem_risk = []
    res_risk = []
    risk_red = []
    d_ref_list_values_for_plot = []
    first_parameter_list_values_for_plot = []
    second_parameter_list_values_for_plot = []
    third_parameter_list_values_for_plot = []
    fourth_parameter_list_values_for_plot = []
    scaling_factor_list_values_for_plot = []
    set_mode = []

    def internal_config_dictionary():
        #This function contains the config dictionary in a form as it is listed in the ARES output. This internal_config
        #dictionary is used just for the correct arrangement of the final output dataframe. If this file would be used as input for ARES, 
        #then a problem would appear that some entries would be overwritten. This is the case because this dictionary is arranged in alphabetical order 
        #and doesnt taken into account in what way the script modifies the values in the ares.inp file.
        internal_config = {
            'EMR_switch': [int(i) for i in parameter_config.getlist('parameters', 'EMR_switch')],
            'allowed_minimum_miss_distance': [float(i) for i in parameter_config.getlist('parameters', 'allowed_minimum_miss_distance')],
            'aop': [float(i) for i in parameter_config.getlist('parameters', 'aop')],
            'avoidance_manoeuvre_criteria': [int(i) for i in parameter_config.getlist('parameters', 'avoidance_manoeuvre_criteria')],
            'collision_probability_alogrithm': [int(i) for i in parameter_config.getlist('parameters', 'collision_probability_alogrithm')],
            'ecc': [float(i) for i in parameter_config.getlist('parameters', 'ecc')],
            'epoch': epoch_list,
            'functionality': [int(i) for i in parameter_config.getlist('parameters', 'functionality')],
            'inc': [float(i) for i in parameter_config.getlist('parameters', 'inc')],
            'lead_time': [float(i) for i in parameter_config.getlist('parameters', 'lead_time')],
            'mass': [float(i) for i in parameter_config.getlist('parameters', 'mass')],
            'min_EMR_ratio': [float(i) for i in parameter_config.getlist('parameters', 'min_EMR_ratio')],
            'particle_size_max': [float(i) for i in parameter_config.getlist('parameters', 'particle_size_max')],
            'particle_size_min': [float(i) for i in parameter_config.getlist('parameters', 'particle_size_min')],
            'raan': [float(i) for i in parameter_config.getlist('parameters', 'raan')],
            'radar_wavelength': [float(i) for i in parameter_config.getlist('parameters', 'radar_wavelength')],
            'scaling_factor': [float(i) for i in parameter_config.getlist('parameters', 'scaling_factor')],
            'sma': list(np.array([float(i) for i in parameter_config.getlist('parameters', 'altitude')]) + _R_EARTH),
            'spacecraft_radius': [float(i) for i in parameter_config.getlist('parameters', 'spacecraft_radius')],
            'target_collision_probability_level': [float(i) for i in parameter_config.getlist('parameters', 'target_collision_probability_level')],
            'type_of_catalogue': [int(i) for i in parameter_config.getlist('parameters', 'type_of_catalogue')],
            'uncertainty_along': [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_along')],
            'uncertainty_cross': [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_cross')],
            'uncertainty_radial': [float(i) for i in parameter_config.getlist('parameters', 'uncertainty_radial')],
            'uncertainty_type': [int(i) for i in parameter_config.getlist('parameters', 'uncertainty_type')]
        }
        return internal_config
    internal_config = internal_config_dictionary()

    value_list = []
    key_list = []
    for key, value in internal_config.items():
        if parameter_config.getboolean("dependent_variables", "dependent_variable_mode") == True:
            if type(value) == list and len(value) > 1 and key != dependent_variables[0][0] and key != dependent_variables[0][1]:
                value_list.append(value)
                key_list.append(key)
            else:
                pass
        else:
            if type(value) == list and len(value) > 1:
                value_list.append(value)
                key_list.append(key)
            else:
                pass
    value_list = list(reversed(value_list))
    key_list = list(reversed(key_list))


    d_ref_list = [float(i) for i in parameter_config.getlist('additional_parameters', 'd_ref')]
    scaling_factor_list = [float(i) for i in parameter_config.getlist('debris_uncertainty', 'scaling_factor_list')] #[0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    for j in range(len(d_ref_list)):
        for k in range(len(scaling_factor_list)):
            results = run(config, dependent_variables, d_ref=d_ref_list[j], h_ref = 2000, scaling_factor = scaling_factor_list[k])
        
            #this part is executed when a dependent_variables calculation is performed
            if not dependent_variables:
                if len(key_list) == 2:
                    first_parameter = value_list[0]
                    second_parameter = value_list[1]

                    new_first_parameter = len(second_parameter)*first_parameter
                    new_second_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in second_parameter))

                    num_of_combinations = len(first_parameter) * len(second_parameter)
                    w = 0
                    while w < num_of_combinations:
                        first_parameter_list_values_for_plot += acpl_steps*[new_first_parameter[w]]
                        second_parameter_list_values_for_plot += acpl_steps*[new_second_parameter[w]]
                        w = w+1
                    d_ref_list_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*num_of_combinations*[scaling_factor_list[k]]
                    set_mode.append(2)

                    print(first_parameter_list_values_for_plot)
                    print(second_parameter_list_values_for_plot)
                
                elif len(key_list) == 1:
                    first_parameter = value_list[0]
                    new_first_parameter = first_parameter
                    num_of_combinations = len(first_parameter)
                    w = 0
                    while w < num_of_combinations:
                        first_parameter_list_values_for_plot += acpl_steps*[new_first_parameter[w]]
                        w = w+1            
                    d_ref_list_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*num_of_combinations*[scaling_factor_list[k]]
                    set_mode.append(1)

                elif len(key_list) == 0:
                    d_ref_list_values_for_plot += acpl_steps*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*[scaling_factor_list[k]]   
                    set_mode.append(0)

            #this part is executed when a dependent_variables calculation is performed
            else:
                if len(key_list) == 2:
                    third_parameter = config[dependent_variables[0][0][0]]
                    fourth_parameter = config[dependent_variables[0][1][0]]

                    first_parameter = value_list[0]
                    second_parameter = value_list[1]
                    new_first_parameter = len(second_parameter)*first_parameter
                    new_second_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in second_parameter))

                    new_first_parameter = len(third_parameter)*new_first_parameter
                    new_second_parameter = len(third_parameter)*new_second_parameter
                    new_third_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)*len(second_parameter)) for x in third_parameter))
                    new_fourth_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)*len(second_parameter)) for x in fourth_parameter))

                    num_of_combinations = len(first_parameter) * len(second_parameter) * len(third_parameter)
                    w = 0
                    while w < num_of_combinations:
                        first_parameter_list_values_for_plot += acpl_steps*[new_first_parameter[w]]
                        second_parameter_list_values_for_plot += acpl_steps*[new_second_parameter[w]]
                        third_parameter_list_values_for_plot += acpl_steps*[new_third_parameter[w]]
                        fourth_parameter_list_values_for_plot += acpl_steps*[new_fourth_parameter[w]]
                        w = w + 1
                    d_ref_list_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*num_of_combinations*[scaling_factor_list[k]]
                    set_mode.append(2)
                
                elif len(key_list) == 1:
                    third_parameter = config[dependent_variables[0][0][0]]
                    fourth_parameter = config[dependent_variables[0][1][0]]

                    first_parameter = value_list[0]
                    new_first_parameter = first_parameter

                    new_first_parameter = len(third_parameter)*new_first_parameter
                    new_third_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in third_parameter))
                    new_fourth_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in fourth_parameter))

                    num_of_combinations = len(first_parameter) * len(third_parameter)
                    w = 0
                    while w < num_of_combinations:
                        first_parameter_list_values_for_plot += acpl_steps*[new_first_parameter[w]]
                        third_parameter_list_values_for_plot += acpl_steps*[new_third_parameter[w]]
                        fourth_parameter_list_values_for_plot += acpl_steps*[new_fourth_parameter[w]]
                        w = w + 1
                    d_ref_list_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*num_of_combinations*[scaling_factor_list[k]]
                    set_mode.append(1)

                elif len(key_list) == 0:
                    third_parameter = config[dependent_variables[0][0][0]]
                    fourth_parameter = config[dependent_variables[0][1][0]]

                    new_third_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, 1) for x in third_parameter))
                    new_fourth_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, 1) for x in fourth_parameter))

                    num_of_combinations = len(third_parameter)
                    w = 0
                    while w < num_of_combinations:
                        third_parameter_list_values_for_plot += acpl_steps*[new_third_parameter[w]]
                        fourth_parameter_list_values_for_plot += acpl_steps*[new_fourth_parameter[w]]
                        w = w + 1
                    d_ref_list_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
                    scaling_factor_list_values_for_plot +=acpl_steps*num_of_combinations*[scaling_factor_list[k]]
                    set_mode.append(0)

            #pprint(results)

            #Collecting all parameters from the individual runs in seperate lists
            all_parameters_string = ["annual_collision_p", "acpl", "f_rem_risk", "f_res_risk", "f_risk_red", "false_alarm_rate", "man_rate", "rem_risk", "res_risk", "risk_red"]
            all_parameters_list = [annual_collision_p, acpl, f_rem_risk, f_res_risk, f_risk_red, false_alarm_rate, man_rate, rem_risk, res_risk, risk_red]
            
            for res in results["results"]:
                annual_collision_p.append(res[all_parameters_string[0]])        
            
            for p in range(1,10):
                for res in results["results"]:
                    for single_run_res in res["cola_evaluation"][all_parameters_string[p]]:
                        all_parameters_list[p].append(single_run_res)
            
            if results["errors"]:
                error_list_1 = ["error"]*len(results["errors"])
                for i in range(len(error_list_1)):
                    all_parameters_list[0].append(error_list_1[i])
                error_list_2 = ["error"]*acpl_steps*len(results["errors"])
                for j in range(1,10):
                    for i in range(len(error_list_2)):  
                        all_parameters_list[j].append(error_list_2[i])
            
                #Sort the list
                for u in range(len(results["errors"])):
                    if len(key_list) == 0:
                        index_variable = fourth_parameter_list_values_for_plot.index(results["errors"][u]["config"]["particle_size_max"])
                    else:
                        index_variable = fourth_parameter_list_values_for_plot.index(results["errors"][u]["config"]["particle_size_max"]) * len(value_list[0])
                    annual_collision_p[index_variable : index_variable] = ["error"]
                del annual_collision_p[-len(results["errors"]):]

                for n in range(1,10):
                    for m in range(len(results["errors"])):
                        if len(key_list) == 0:
                            index_variable = fourth_parameter_list_values_for_plot.index(results["errors"][m]["config"]["particle_size_max"]) *acpl_steps
                        else:
                            index_variable = fourth_parameter_list_values_for_plot.index(results["errors"][m]["config"]["particle_size_max"]) *acpl_steps * len(value_list[0])
                        all_parameters_list[n][index_variable:index_variable] = ["error"]*acpl_steps
                    del all_parameters_list[n][-acpl_steps*len(results["errors"]):]
            
    for i in range(len(all_parameters_list)):
        print("All " + all_parameters_string[i] + ": "  + str(all_parameters_list[i]))
                
    #This line is necessary to assign the annual_collision_p value to each ACPL line in the data frame down below.
    annual_collision_p_for_plot = list(itertools.chain.from_iterable(itertools.repeat(x, acpl_steps) for x in annual_collision_p))

    #Save the output data to csv file in order to plot the data in seperate python file (plot_file.py)
    #Merging of the individual lists of the individual runs
    if not dependent_variables:
        if set_mode[0] == 2:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, key_list[0]: first_parameter_list_values_for_plot, key_list[1]:second_parameter_list_values_for_plot, "d_ref":d_ref_list_values_for_plot,
                "scaling_factor":scaling_factor_list_values_for_plot}
            )
        elif set_mode[0] == 1:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, key_list[0]: first_parameter_list_values_for_plot, "d_ref":d_ref_list_values_for_plot,
                "scaling_factor":scaling_factor_list_values_for_plot}
            )
        elif set_mode[0] == 0:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, "d_ref":d_ref_list_values_for_plot,
                "scaling_factor":scaling_factor_list_values_for_plot}
            )
    else:
        if set_mode[0] == 2:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, key_list[0]: first_parameter_list_values_for_plot, key_list[1]:second_parameter_list_values_for_plot, "d_ref":d_ref_list_values_for_plot,
                "scaling_factor":scaling_factor_list_values_for_plot, dependent_variables[0][0][0]:third_parameter_list_values_for_plot, 
                dependent_variables[0][1][0]:fourth_parameter_list_values_for_plot}
            )
        elif set_mode[0] == 1:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, key_list[0]: first_parameter_list_values_for_plot, "d_ref":d_ref_list_values_for_plot,
                "scaling_factor":scaling_factor_list_values_for_plot, dependent_variables[0][0][0]:third_parameter_list_values_for_plot, 
                dependent_variables[0][1][0]:fourth_parameter_list_values_for_plot}
            )
        elif set_mode[0] == 0:
            df_total_output = pd.DataFrame(
                data = {"annual_collision_p": annual_collision_p_for_plot, "acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
                "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
                "risk_red":risk_red, "d_ref":d_ref_list_values_for_plot, "scaling_factor":scaling_factor_list_values_for_plot, 
                dependent_variables[0][0][0]:third_parameter_list_values_for_plot, dependent_variables[0][1][0]:fourth_parameter_list_values_for_plot}
            )

    df_total_output.to_csv(parameter_config["path"]["ares_output"], sep=',', index=False)
    
    #Save the Input Parameters
    shutil.copyfile("ares_config.ini", parameter_config["path"]["ares_config_path"])
    
    #Calculate the computing time
    end = time.time()
    print("Calculation Time: " + str(format(end-start, ".2f")) + "s")

if __name__ == "__main__":
    main()