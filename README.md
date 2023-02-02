# SST-ARES

## Modeling of SST networks with ARES

## Description
This project consists of two sub-projects. 
1. With ares_script.py it is possible to perform parametric ARES computations. 
2. The sustainability_rating.py file provides a model, which assesses the impact of collisions on the space environment.

## Usage
### Usage of ares_script.py

Before you start: 

1. Step: Define the global path to the master_data folder in ares.cfg. Insert the path in front of 'Path to MASTER data files'.
2. Step: Define the global path to the config folder in the drama-gui.cfg file in DRAMA3WorkspaceDirectory.
3. Step: Define the global path to ares_osx in the drama-gui.cfg file in ARESBinary.

Perform the analysis:

Disclaimer: ARES uses the condensed population data provided by MASTER. This data can be found in config/master_data. For memory reasons, only the reference population for the epoch 2016-11-01 is stored in config/master_data. If it becomes necessary to perform analyses for other epochs, they must be downloaded from https://sdup.esoc.esa.int/master/downloads (MASTER-8 Condensed Population Files) and stored in config/master_data.

1. Step: Provide your input data and follow the instructions in the ares_config.ini file.
2. Step: Run ares_script.py
3. Step: The output data will be saved in plot_files/total_output.csv as dataframe
4. Step: Plot the data in the csv file by providing your own plot files (depending on what you want analyze) or use the already existing plot files, e.g. plot_files/plot_risk_reduction_inc_sma.py, which shows the a heat map for the manoeuvre rates depending on multiple inclination and semi-major axis values.

### Usage of sustainability_rating.py

1. The Python script sustainability_rating.py requires two input files. First file: Compute ARES output with ares_script.py for a complete population e.g. 0.01-100 and save it as acp_binned.csv. Second file: Compute ARES output with ares_script.py for a binned population e.g. 0.01-0.03, 0.03-0.06, 0.06-0.09, ..., 99.97-100.
2. Save both files in: ares_project/sustainability_rating/requirement_plots as acp_total.csv and acp_binned.csv respectively.
3. Define in sustainability_rating.py which collision probability you want to analyze (annual_collision_p or acid or res_risk).
4. Define which error list should be used (has to match with the metric that is analyzed in 3): error_list_acp or error_list_acpd or error_list_res_risk
5. Define the d_repr list
6. Make sure that the ares_script.ini file has the binned population defined in particle_size_min and particle_size_max
7. Step: Run sustainability_rating.py. File location: sustainability_rating/sustainability_rating.py.

## Authors and acknowledgment
Kovacic, Aleksandar

Siminski, Jan
