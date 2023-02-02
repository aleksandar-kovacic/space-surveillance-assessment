#%% Import
import time
from tkinter import VERTICAL
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.constants as spc
import itertools
import pathlib

from datetime import datetime
from pprint import pprint

from drama import ares
from drama import utils

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
CONFIG_DIR = SCRIPT_DIR / "config"

utils.config_file_paths_dict["macos"] = [str(CONFIG_DIR) + "/{}/config.json"]

# May not be needed for newest python_drama_package
# Default Parameter aus der ares.inp Datei aufrufen
# Zugriff auf den Pfad zur Master Popoulation und auf input_focus der ares.cfg Datei
# Sind das die Werte, die übernommen werden, wenn ich die unten bei def main(): config weglasse?
# Übernimmt die lambda Funktion den Wert aus der ares.inp Datei und wendet dann den String bzw. strftime an?
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


covariance_matrix = np.array([
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2],
    [1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2, 1.0, 0.4, 0.2]
])

#covariance_matrix = covariance_matrix * 0.01

scaling_factor_table = np.array([
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
])
#Improvement through Space Fence, Paper by Koltiska --> i = 60°-110°, e < 0.1, Objects detected mainly in LEO 
scaling_factor_table[:4, 4:6] = 0.7
scaling_factor_table[12:16, 4:6] = 0.7
scaling_factor_table[24:28, 4:6] = 0.7

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
    # :d formatiert n_steps zum Integer
    lines = update_line_column(280, 0, lines, "{:d}".format(n_steps))
    lines[281] = "x " * n_steps
    for i in range(n_steps):
        lines = update_line_column(281, i, lines, "{:2.1e}".format(params[i]))
    return lines

def update_covariance_matrix(lines):
    """Update covariance matrix"""
    line_counter = 172
    k = 0
    while line_counter <= 207:
        lines[line_counter] = "x " * 18
        for i in range(18):
            lines = update_line_column(line_counter, i, lines, "{:.2f}".format(covariance_matrix[k][i]))
        line_counter = line_counter + 1
        k = k + 1
    return lines

def update_scaling_factor_table(lines):
    """Update scaling factor table"""
    line_counter = 234
    k = 0
    while line_counter <= 269:
        lines[line_counter] = "x " * 6
        for i in range(6):
            lines = update_line_column(line_counter, i, lines, "{:.2f}".format(scaling_factor_table[k][i]))
        line_counter = line_counter + 1
        k = k + 1
    return lines

def update_default_config(d_ref=0.2, h_ref=2000):
    template_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares_template.inp"
    input_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares.inp"
    with open(template_path, "r") as f:
        lines = f.readlines()

    lines = update_line_column(69, 0, lines, "{:3.2e}".format(d_ref))
    lines = update_line_column(70, 0, lines, "{:3.2e}".format(h_ref))
    #ursprünglich: lines = update_acpl_param(lines, -9, -2, 10)
    #für Remaining Risk Kurve anpassen: update_acpl_param(lines, -9, -1.4, 10)
    #für gleichmäßige Einteilung: 1e-09, 1e-08, 1e-07...: update_acpl_param(lines, -9, -1, 9)
    #für schnelle Berechnung wenn man nur ACPL = 0.0001 braucht: update_acpl_param(lines, min_order= -4, max_order= -2, n_steps = 1)
    #lines = update_acpl_param(lines, min_order=-8, max_order=-3, n_steps = 10)
    lines = update_acpl_param(lines, min_order= -4, max_order= -2, n_steps = 1) #nicht vergessen acpl_steps unten an n_steps anzupassen
    lines = update_covariance_matrix(lines)
    lines = update_scaling_factor_table(lines)

    with open(input_path, "w") as f:
        f.writelines(lines)
    
#adapt to n_steps (acpl_steps needs to be equal to n_steps which was defined few lines above)
acpl_steps = 1


def run(config, d_ref, h_ref):
    update_default_config(d_ref=d_ref, h_ref=h_ref)
    return ares.run(config, parallel=True)


def main():
    start = time.time()
    #%% Run demo
    _R_EARTH = 6378.137
    #Die beiden Parameter, die hier definiert werden, müssen auch unten fürs plotten definiert werden bei first_parameter and second_parameter
    #sma Swarm B = 505km
    #sma_list = [_R_EARTH+200, _R_EARTH+300,_R_EARTH+400,_R_EARTH+500,_R_EARTH+600,_R_EARTH+700,_R_EARTH+800,_R_EARTH+900,_R_EARTH+1000]
    #sma_list = [_R_EARTH+200,_R_EARTH+400,_R_EARTH+600,_R_EARTH+800,_R_EARTH+1000,_R_EARTH+1200, _R_EARTH+1400,_R_EARTH+1600,_R_EARTH+1800,_R_EARTH+2000]
    #sma_list = [_R_EARTH+500,_R_EARTH+600,_R_EARTH+700,_R_EARTH+800,_R_EARTH+900,_R_EARTH+1000]
    #sma_list = [_R_EARTH+300,_R_EARTH+400]
    sma_list = [_R_EARTH+505]
    #inc_list = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
    #inc_list = [0, 30, 60, 90, 120, 150, 180]
    #inc_list = [0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105]
    #inc_list = [0, 15, 30, 45, 60, 75, 90]
    #inc_list = [85, 87.5, 90, 92.5, 95]
    inc_list = [90]
    #wavelength_list = [0.15, 0.125, 0.1, 0.075]
    wavelength_list = [0.3]
    #Swarm B
    config = {
        # Standard: "particle_size_min": 0.01
        "particle_size_min": 0.01,
        "particle_size_max": 100,
        #Space Fence works in S-Band i.e. radar_wavelength = 0.075m-0.15m
        "radar_wavelength": wavelength_list,
        "EMR_switch": 0,
        "min_EMR_ratio": 40,
        #mass of spacecraft
        "mass": 468,
        #Swarm B = 4.55m
        "spacecraft_radius": 4.55,
        "sma": sma_list,
        #Swarm B inlicnation = 87.75
        "inc": inc_list,
        "ecc": 3.28e-4,
        "raan": 76.4433,
        "aop": 92.5926,
        "epoch": datetime(2016, 11, 1),
        #uncertainty_type: 1 = user-entered uncertainties (along, cross, radial), 2 = catalogue uncertainties
        "uncertainty_type": 2,
        "uncertainty_along": 0.2,
        "uncertainty_cross": 1.0,
        "uncertainty_radial": 0.075,
        #Time between event prediction and event-occurance (TCA - Time to closest approach)
        "lead_time": 1,
        #type_of_catalogue: 1 = CDM data, 2 = user-defined covariances (covariance_matrix)
        "type_of_catalogue": 1,
        #scaling_factor: int-number = global scaling factor, negative value = user-defined scaling factors (scaling_factor_table) 
        "scaling_factor": 1,
        "collision_probability_alogrithm": 0,
        "avoidance_manoeuvre_criteria": 0,
        "target_collision_probability_level": 0.1,
        "allowed_minimum_miss_distance": 1.5
    }

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
    d_ref_values_for_plot = []
    sma_list_values_for_plot = []
    inc_list_values_for_plot=[]
    wavelength_list_values_for_plot = []

    #Put in one or multiple d_ref values that should be used for the simulation
    d_ref_list = [0.32]
    for j in range(len(d_ref_list)):
        results = run(config, d_ref=d_ref_list[j], h_ref = 2000)
        """
        #Jetzt ist sma_list = 2. Wenn man aber weitere Parameter definiert z.B. 2 Werte für die Inklination, 
        #dann muss number_of_combinations mit *len(inc_list) erweitert werden. Damit wären es dann 4 Kombinationsmöglichkeiten für einen d_ref Wert.
        number_of_combinations = len(sma_list) * len(inclination_list)
        w = 0
        while w < number_of_combinations:
            d_ref_values_for_plot.append(d_ref_list[j])
            sma_list_values_for_plot.append(sma_list[w])
            inclination_list_values_for_plot.append(inclination_list[w])
            w = w + 1
        """
        #Define the parameters that should be varied
        first_parameter = sma_list
        second_parameter = inc_list
        first_parameter_list_values_for_plot = sma_list_values_for_plot
        second_parameter_list_values_for_plot = inc_list_values_for_plot

        new_first_parameter = len(second_parameter)*first_parameter
        new_second_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in second_parameter))

        num_of_combinations = len(first_parameter) * len(second_parameter)
        w = 0
        while w < num_of_combinations:
            first_parameter_list_values_for_plot += acpl_steps*[new_first_parameter[w]]
            second_parameter_list_values_for_plot += acpl_steps*[new_second_parameter[w]]
            w = w+1
        d_ref_values_for_plot += acpl_steps*num_of_combinations*[d_ref_list[j]]
        
    #results = run(config, d_ref=0.32, h_ref = 2000)

        pprint(results)
        
        #Collecting all parameters from the individual runs in seperate lists
        all_parameters_string = ["annual_collision_p", "acpl", "f_rem_risk", "f_res_risk", "f_risk_red", "false_alarm_rate", "man_rate", "rem_risk", "res_risk", "risk_red"]
        all_parameters_list = [annual_collision_p, acpl, f_rem_risk, f_res_risk, f_risk_red, false_alarm_rate, man_rate, rem_risk, res_risk, risk_red]
        
        for res in results["results"]:
            annual_collision_p.append(res[all_parameters_string[0]])
        
        for p in range(1,10):
            for res in results["results"]:
                for single_run_res in res["cola_evaluation"][all_parameters_string[p]]:
                    all_parameters_list[p].append(single_run_res)
        
        for k in range(10):
            print("All " + all_parameters_string[k] + ": "  + str(all_parameters_list[k]))
    
    #This line is necessary to assign the annual_collision_p value to each ACPL line in the data frame down below.
    annual_collision_p_for_plot = list(itertools.chain.from_iterable(itertools.repeat(x, acpl_steps) for x in annual_collision_p))
    
    #Calculate the computing time
    end = time.time()
    print("Calculation Time: " + str(format(end-start, ".2f")) + "s")

    #Save output data to csv file in order to plot the data in seperate python file (plot_file.py)
    #Merging of the individual lists of the individual runs
    df_total_output = pd.DataFrame(
        data = {"annual_collision_p": annual_collision_p_for_plot,"acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, 
        "f_risk_red":f_risk_red, "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk,
        "risk_red":risk_red, "sma": sma_list_values_for_plot, "inc":inc_list_values_for_plot, "d_ref":d_ref_values_for_plot}
    )
    df_total_output.to_csv("plot_files/total_output.csv", sep=',', index=False)

    #Save the Input Parameters (doesnt work yet, because 2d data is created whenever I use more than one e.g. sma-value.)
    """
    df_input_parameters = pd.DataFrame(data = {**acpl_input,  **config, **{"d_ref": d_ref_list}})
    df_input_parameters.to_csv("input_parameters.csv", sep = ",", index = False)
    #Save the scaling factor table
    np.savetxt("scaling_factor_table.csv", scaling_factor_table, delimiter=",", fmt='%.2f')
    """
    
    #Old Code
    """
    ares_output = "old_0,0177_ares_output_data.csv"
    acp_d_ref_data = "old_0,0177_acp_d_ref_data.csv"
    sma_data = "old_0,0177_sma_data.csv"
    """

    """
    ares_output = "output_data.csv"
    acp_d_ref_data = "acp_d_ref_data.csv"
    sma_data = "sma_data.csv"
    
    df_output_data = pd.DataFrame(
        data={"acpl": acpl, "f_rem_risk": f_rem_risk, "f_res_risk":f_res_risk, "f_risk_red":f_risk_red, 
        "false_alarm_rate":false_alarm_rate, "man_rate":man_rate, "rem_risk":rem_risk, "res_risk":res_risk, "risk_red":risk_red}
    )
    df_output_data.to_csv(ares_output, sep=',', index=False)

    df_acp_d_ref = pd.DataFrame(
        data={"d_ref": d_ref_values_for_plot, "annual_collision_p": annual_collision_p}
    )
    df_acp_d_ref.to_csv(acp_d_ref_data, sep=',', index=False)

    df_sma = pd.DataFrame(
        data={"sma": sma_list_values_for_plot}
    )
    df_sma.to_csv(sma_data, sep=',', index=False)

    """

if __name__ == "__main__":
    main()
