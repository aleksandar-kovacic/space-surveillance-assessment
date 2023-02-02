from pprint import pprint
from datetime import datetime
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

######################################################################################################################################################
######################################################################################################################################################
results = {'config': {'EMR_switch': 0,
            'allowed_minimum_miss_distance': 1.5,
            'aop': 92.5926,
            'avoidance_manoeuvre_criteria': 0,
            'collision_probability_alogrithm': 0,
            'ecc': 0.000328,
            'epoch': 3,
            'id': 'PyAres',
            'inc': [87.75],
            'lead_time': 1,
            'mass': 468,
            'min_EMR_ratio': 40,
            'particle_size_max': [0.01778, 0.89125, 0.01122, 5.62341],
            'particle_size_min': [0.01413, 0.70795, 0.01, 4.46684],
            'raan': 76.4433,
            'radar_wavelength': [0.15],
            'scaling_factor': -1,
            'sma': [6883.137],
            'spacecraft_radius': 0.1,
            'target_collision_probability_level': 0.1,
            'type_of_catalogue': 1,
            'uncertainty_along': 0.2,
            'uncertainty_cross': 1.0,
            'uncertainty_radial': 0.075,
            'uncertainty_type': 2},
 'errors': [{'config': {'EMR_switch': 0,
                        'allowed_minimum_miss_distance': 1.5,
                        'aop': 92.5926,
                        'avoidance_manoeuvre_criteria': 0,
                        'collision_probability_alogrithm': 0,
                        'ecc': 0.000328,
                        'epoch': 3,
                        'id': 'PyAres',
                        'inc': 87.75,
                        'lead_time': 1,
                        'mass': 468,
                        'min_EMR_ratio': 40,
                        'particle_size_max': 0.89125,
                        'particle_size_min': 0.70795,
                        'raan': 76.4433,
                        'radar_wavelength': 0.15,
                        'scaling_factor': -1,
                        'sma': 6883.137,
                        'spacecraft_radius': 0.1,
                        'target_collision_probability_level': 0.1,
                        'type_of_catalogue': 1,
                        'uncertainty_along': 0.2,
                        'uncertainty_cross': 1.0,
                        'uncertainty_radial': 0.075,
                        'uncertainty_type': 2},
             'errfile': '---\n'
                        'message no:     1\n'
                        'type: warning\n'
                        'title: ARES input\n'
                        'location: [m_AresInput] loadInputFromFile\n'
                        'message: \n'
                        'EMR switch set to '
                        'off                                       \n'
                        'User-input EMR is '
                        'ignored                                   \n'
                        '---\n'
                        'message no:     2\n'
                        'type: warning\n'
                        'title: MASTER Execution information\n'
                        'location: [m_fluxes] obtainFluxNew\n'
                        'message: \n'
                        'MASTER issued '
                        'remarks.                                      \n'
                        '                                                            \n',
             'logfile': ' \n'
                        '                 __/__/    __/_/__/    __/__/__/  '
                        '_/__/_/\n'
                        '               __/   __/  __/    __/  __/        __/\n'
                        '              __/__/__/  __/_/__/    __/__/      '
                        '__/__/\n'
                        '             __/   __/  __/    __/  __/             '
                        '__/\n'
                        '            __/   __/  __/     __/ __/__/__/  '
                        '_/__/_/\n'
                        ' \n'
                        '        Debris Risk Assessment and Mitigation '
                        'Analysis Tool Suite\n'
                        '       MASTER(-based) Assessment of Risk Event '
                        'Statistics Software\n'
                        '                           (DRAMA-ARES v3.1.0)\n'
                        ' \n'
                        ' '
                        '-----------------------------------------------------------------------\n'
                        ' ARES version  : 3.1.0\n'
                        ' Build date    : 23-Feb-21\n'
                        ' Platform      : x86_64-linux-gnu\n'
                        ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                        ' '
                        '-----------------------------------------------------------------------\n'
                        ' [25/05/2022 16:00:39] INFO Starting ARES version '
                        '3.1.0\n'
                        ' [25/05/2022 16:00:39] INFO Starting progress report\n'
                        ' [25/05/2022 16:00:39] INFO Loading input file\n'
                        '[[\n'
                        'WARNING Overriding user-input EMR\n'
                        ']]\n'
                        ' [25/05/2022 16:00:39] INFO Validating input file\n'
                        ' [25/05/2022 16:00:39] INFO Allocating resources\n'
                        ' [25/05/2022 16:00:39] INFO Loading covariance '
                        'tables\n'
                        ' [25/05/2022 16:00:39] INFO Computing population '
                        'flux\n'
                        'Calling MASTER v8.0.2 API..\n'
                        'Scanning datafiles for most recent reference '
                        'population...\n'
                        'Fetching population files: Man-made Population...\n'
                        'Most recent reference epoch: 2016/11\n'
                        'Target orbit scenario\n'
                        ' Currently using: FOCUS v2.5.7\n'
                        'Reading from propagation parameter file '
                        '/Users/alekskovacic/Desktop/python_test/\n'
                        'config/TOOLS/ARES/default/focus//focus.prm\n'
                        'File operation successful (79) OPENED '
                        '/Users/alekskovacic/Desktop/python_test/co\n'
                        'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                        '- static orbit\n'
                        '[[\n'
                        "REMARK in subroutine 'uinput':\n"
                        '  Target orbit epochs overrule simulation time for '
                        'target orbit scenario.\n'
                        ']]\n'
                        ' '
                        '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                        '#  1 /   1 :  2016 11 01 00    6883.14 0.00033  '
                        '87.75   76.44   92.59\n'
                        'Uncertainty indicators available!\n'
                        "Now processing 'Man-made Population' ...\n"
                        'Reading probability table header from '
                        '/Users/alekskovacic/Desktop/python_test/co\n'
                        'nfig/master_data//cond_20161101_00_leo.prb.\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n'
                        '\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '         *************** MASTER issued remarks! '
                        '**************\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n'
                        '\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n',
             'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                       b'_/__/_/\n               __/   __/  __/    __/  __/   '
                       b'     __/\n              __/__/__/  __/_/__/    __/__/'
                       b'      __/__/\n             __/   __/  __/    __/  __/'
                       b'             __/\n            __/   __/  __/     __/ '
                       b'__/__/__/  _/__/_/\n \n        Debris Risk Assessment '
                       b'and Mitigation Analysis Tool Suite\n       MASTER(-ba'
                       b'sed) Assessment of Risk Event Statistics Software\n  '
                       b'                         (DRAMA-ARES v3.1.0)\n \n ----'
                       b'----------------------------------------------------'
                       b'---------------\n ARES version  : 3.1.0\n Build date  '
                       b'  : 23-Feb-21\n Platform      : x86_64-linux-gnu\n Com'
                       b'piler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n ---'
                       b'----------------------------------------------------'
                       b'----------------\n [25/05/2022 16:00:39] INFO Startin'
                       b'g ARES version 3.1.0\n [25/05/2022 16:00:39] INFO Sta'
                       b'rting progress report\n [25/05/2022 16:00:39] INFO Lo'
                       b'ading input file\n [25/05/2022 16:00:39] \x1b[31mWAR'
                       b'NING\x1b[0m Overriding user-input EMR\n [25/05/2022 '
                       b'16:00:39] INFO Validating input file\n [25/05/2022 16'
                       b':00:39] INFO Allocating resources\n [25/05/2022 16:00'
                       b':39] INFO Loading covariance tables\n [25/05/2022 16:'
                       b'00:39] INFO Computing population flux\n [25/05/2022 1'
                       b'6:00:40] INFO MASTER issued remarks\n [25/05/2022 16:'
                       b'00:40] INFO Computing detectable and catastrophic fl'
                       b'uxes\n [25/05/2022 16:00:40] INFO Minimum detectable '
                       b'size for target orbit / m: 0.169E-01\n [25/05/2022 16'
                       b':00:40] INFO Trying to merge low and high eccentrici'
                       b'ty bins\n [25/05/2022 16:00:40] INFO Unable to merge '
                       b'covs for low and high ecc. objects\n [25/05/2022 16:0'
                       b'0:40] INFO Computing global fluxes\n [25/05/2022 16:0'
                       b'0:40] INFO Computing collision rates\n [25/05/2022 16'
                       b':00:40] INFO Computing manoeuvre rates and avoidance'
                       b'\n [25/05/2022 16:00:40] INFO Using 11 threads\n [25/0'
                       b'5/2022 16:00:40] ERROR Fatal error! Index mismatch i'
                       b'n i_group2index\n [25/05/2022 16:00:40] ERROR  size: '
                       b'          2 >           1\n  \nAres finished with code'
                       b' 200\n  \n Unclassified error                         '
                       b'                 \n                                  '
                       b'                           \n                        '
                       b'                                     \n  \n',
             'status': 'error in ARES'},
            {'config': {'EMR_switch': 0,
                        'allowed_minimum_miss_distance': 1.5,
                        'aop': 92.5926,
                        'avoidance_manoeuvre_criteria': 0,
                        'collision_probability_alogrithm': 0,
                        'ecc': 0.000328,
                        'epoch': 3,
                        'id': 'PyAres',
                        'inc': 87.75,
                        'lead_time': 1,
                        'mass': 468,
                        'min_EMR_ratio': 40,
                        'particle_size_max': 5.62341,
                        'particle_size_min': 4.46684,
                        'raan': 76.4433,
                        'radar_wavelength': 0.15,
                        'scaling_factor': -1,
                        'sma': 6883.137,
                        'spacecraft_radius': 0.1,
                        'target_collision_probability_level': 0.1,
                        'type_of_catalogue': 1,
                        'uncertainty_along': 0.2,
                        'uncertainty_cross': 1.0,
                        'uncertainty_radial': 0.075,
                        'uncertainty_type': 2},
             'errfile': '---\n'
                        'message no:     1\n'
                        'type: warning\n'
                        'title: ARES input\n'
                        'location: [m_AresInput] loadInputFromFile\n'
                        'message: \n'
                        'EMR switch set to '
                        'off                                       \n'
                        'User-input EMR is '
                        'ignored                                   \n'
                        '---\n'
                        'message no:     2\n'
                        'type: warning\n'
                        'title: MASTER Execution information\n'
                        'location: [m_fluxes] obtainFluxNew\n'
                        'message: \n'
                        'MASTER issued '
                        'remarks.                                      \n'
                        '                                                            \n',
             'logfile': ' \n'
                        '                 __/__/    __/_/__/    __/__/__/  '
                        '_/__/_/\n'
                        '               __/   __/  __/    __/  __/        __/\n'
                        '              __/__/__/  __/_/__/    __/__/      '
                        '__/__/\n'
                        '             __/   __/  __/    __/  __/             '
                        '__/\n'
                        '            __/   __/  __/     __/ __/__/__/  '
                        '_/__/_/\n'
                        ' \n'
                        '        Debris Risk Assessment and Mitigation '
                        'Analysis Tool Suite\n'
                        '       MASTER(-based) Assessment of Risk Event '
                        'Statistics Software\n'
                        '                           (DRAMA-ARES v3.1.0)\n'
                        ' \n'
                        ' '
                        '-----------------------------------------------------------------------\n'
                        ' ARES version  : 3.1.0\n'
                        ' Build date    : 23-Feb-21\n'
                        ' Platform      : x86_64-linux-gnu\n'
                        ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                        ' '
                        '-----------------------------------------------------------------------\n'
                        ' [25/05/2022 16:00:39] INFO Starting ARES version '
                        '3.1.0\n'
                        ' [25/05/2022 16:00:39] INFO Starting progress report\n'
                        ' [25/05/2022 16:00:39] INFO Loading input file\n'
                        '[[\n'
                        'WARNING Overriding user-input EMR\n'
                        ']]\n'
                        ' [25/05/2022 16:00:39] INFO Validating input file\n'
                        ' [25/05/2022 16:00:39] INFO Allocating resources\n'
                        ' [25/05/2022 16:00:39] INFO Loading covariance '
                        'tables\n'
                        ' [25/05/2022 16:00:39] INFO Computing population '
                        'flux\n'
                        'Calling MASTER v8.0.2 API..\n'
                        'Scanning datafiles for most recent reference '
                        'population...\n'
                        'Fetching population files: Man-made Population...\n'
                        'Most recent reference epoch: 2016/11\n'
                        'Target orbit scenario\n'
                        ' Currently using: FOCUS v2.5.7\n'
                        'Reading from propagation parameter file '
                        '/Users/alekskovacic/Desktop/python_test/\n'
                        'config/TOOLS/ARES/default/focus//focus.prm\n'
                        'File operation successful (79) OPENED '
                        '/Users/alekskovacic/Desktop/python_test/co\n'
                        'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                        '- static orbit\n'
                        '[[\n'
                        "REMARK in subroutine 'uinput':\n"
                        '  Target orbit epochs overrule simulation time for '
                        'target orbit scenario.\n'
                        ']]\n'
                        ' '
                        '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                        '#  1 /   1 :  2016 11 01 00    6883.14 0.00033  '
                        '87.75   76.44   92.59\n'
                        'Uncertainty indicators available!\n'
                        "Now processing 'Man-made Population' ...\n"
                        'Reading probability table header from '
                        '/Users/alekskovacic/Desktop/python_test/co\n'
                        'nfig/master_data//cond_20161101_00_leo.prb.\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n'
                        '\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '         *************** MASTER issued remarks! '
                        '**************\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n'
                        '\n'
                        ' '
                        '_________________________________________________________________________\n'
                        '\n',
             'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                       b'_/__/_/\n               __/   __/  __/    __/  __/   '
                       b'     __/\n              __/__/__/  __/_/__/    __/__/'
                       b'      __/__/\n             __/   __/  __/    __/  __/'
                       b'             __/\n            __/   __/  __/     __/ '
                       b'__/__/__/  _/__/_/\n \n        Debris Risk Assessment '
                       b'and Mitigation Analysis Tool Suite\n       MASTER(-ba'
                       b'sed) Assessment of Risk Event Statistics Software\n  '
                       b'                         (DRAMA-ARES v3.1.0)\n \n ----'
                       b'----------------------------------------------------'
                       b'---------------\n ARES version  : 3.1.0\n Build date  '
                       b'  : 23-Feb-21\n Platform      : x86_64-linux-gnu\n Com'
                       b'piler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n ---'
                       b'----------------------------------------------------'
                       b'----------------\n [25/05/2022 16:00:39] INFO Startin'
                       b'g ARES version 3.1.0\n [25/05/2022 16:00:39] INFO Sta'
                       b'rting progress report\n [25/05/2022 16:00:39] INFO Lo'
                       b'ading input file\n [25/05/2022 16:00:39] \x1b[31mWAR'
                       b'NING\x1b[0m Overriding user-input EMR\n [25/05/2022 '
                       b'16:00:39] INFO Validating input file\n [25/05/2022 16'
                       b':00:39] INFO Allocating resources\n [25/05/2022 16:00'
                       b':39] INFO Loading covariance tables\n [25/05/2022 16:'
                       b'00:39] INFO Computing population flux\n [25/05/2022 1'
                       b'6:00:40] INFO MASTER issued remarks\n [25/05/2022 16:'
                       b'00:40] INFO Computing detectable and catastrophic fl'
                       b'uxes\n [25/05/2022 16:00:40] INFO Minimum detectable '
                       b'size for target orbit / m: 0.169E-01\n [25/05/2022 16'
                       b':00:40] INFO Trying to merge low and high eccentrici'
                       b'ty bins\n [25/05/2022 16:00:40] INFO Unable to merge '
                       b'covs for low and high ecc. objects\n [25/05/2022 16:0'
                       b'0:40] INFO Computing global fluxes\n [25/05/2022 16:0'
                       b'0:40] INFO Computing collision rates\n [25/05/2022 16'
                       b':00:40] INFO Computing manoeuvre rates and avoidance'
                       b'\n [25/05/2022 16:00:40] INFO Using 11 threads\n [25/0'
                       b'5/2022 16:00:40] ERROR Fatal error! Index mismatch i'
                       b'n i_group2index\n [25/05/2022 16:00:40] ERROR Fatal e'
                       b'rror! Index mismatch in i_group2index\n [25/05/2022 1'
                       b'6:00:40] ERROR Fatal error! Index mismatch in i_grou'
                       b'p2index\n [25/05/2022 16:00:40] ERROR  size:         '
                       b'  3 >           1\n [25/05/2022 16:00:40] ERROR Fatal'
                       b' error! Index mismatch in i_group2index\n [25/05/2022'
                       b' 16:00:40] ERROR Fatal error! Index mismatch in i_gr'
                       b'oup2index\n [25/05/2022 16:00:40] ERROR Fatal error! '
                       b'Index mismatch in i_group2index\n [25/05/2022 16:00:4'
                       b'0] ERROR  size:           3 >           1\n [25/05/20'
                       b'22 16:00:40] ERROR  size:           3 >           1\n'
                       b' [25/05/2022 16:00:40] ERROR Fatal error! Index mism'
                       b'atch in i_group2index\n  \nAres finished with code 200'
                       b'\n  \n [25/05/2022 16:00:40] ERROR Fatal error! Index '
                       b'mismatch in i_group2index\n [25/05/2022 16:00:40] ERR'
                       b'OR  size:           3 >           1\n [25/05/2022 16:'
                       b'00:40] ERROR  size:           3 >           1\n [25/0'
                       b'5/2022 16:00:40] ERROR Fatal error! Index mismatch i'
                       b'n i_group2index\n  \nAres finished with code 200\n '
                       b' \n [25/05/2022 16:00:40] ERROR  size:           3 > '
                       b'          1\n  \nAres finished with code 200\n  \n U'
                       b'nclassified error                                   '
                       b'       \n                                            '
                       b'                 \n [25/05/2022 16:00:40] ERROR  size'
                       b':           3 >           1\n [25/05/2022 16:00:40] E'
                       b'RROR Fatal error! Index mismatch in i_group2index\n  '
                       b'\nAres finished with code 200\n  \n Unclassified er'
                       b'ror                                          \n      '
                       b'                                                    '
                       b'   \n                                                '
                       b'             \n  \n [25/05/2022 16:00:40] ERROR  size:'
                       b'           3 >           1\n  \n',
             'status': 'error in ARES'}],
 'results': [{'annual_collision_p': 4.151e-07,
              'cola_evaluation': {'acpl': [0.0001, 0.001, 0.01],
                                  'f_rem_risk': [1.0, 1.0, 1.0],
                                  'f_res_risk': [1.0, 1.0, 1.0],
                                  'f_risk_red': [0.0, 0.0, 0.0],
                                  'false_alarm_rate': [0.0, 0.0, 0.0],
                                  'man_rate': [0.0, 0.0, 0.0],
                                  'rem_risk': [4.15111e-07,
                                               4.15111e-07,
                                               4.15111e-07],
                                  'res_risk': [9.76807e-08,
                                               9.76807e-08,
                                               9.76807e-08],
                                  'risk_red': [0.0, 0.0, 0.0]},
              'config': {'EMR_switch': 0,
                         'allowed_minimum_miss_distance': 1.5,
                         'aop': 92.5926,
                         'avoidance_manoeuvre_criteria': 0,
                         'collision_probability_alogrithm': 0,
                         'ecc': 0.000328,
                         'epoch': 3,
                         'id': 'PyAres',
                         'inc': 87.75,
                         'lead_time': 1,
                         'mass': 468,
                         'min_EMR_ratio': 40,
                         'particle_size_max': 0.01778,
                         'particle_size_min': 0.01413,
                         'raan': 76.4433,
                         'radar_wavelength': 0.15,
                         'scaling_factor': -1,
                         'sma': 6883.137,
                         'spacecraft_radius': 0.1,
                         'target_collision_probability_level': 0.1,
                         'type_of_catalogue': 1,
                         'uncertainty_along': 0.2,
                         'uncertainty_cross': 1.0,
                         'uncertainty_radial': 0.075,
                         'uncertainty_type': 2},
              'errfile': '---\n'
                         'message no:     1\n'
                         'type: warning\n'
                         'title: ARES input\n'
                         'location: [m_AresInput] loadInputFromFile\n'
                         'message: \n'
                         'EMR switch set to '
                         'off                                       \n'
                         'User-input EMR is '
                         'ignored                                   \n'
                         '---\n'
                         'message no:     2\n'
                         'type: warning\n'
                         'title: MASTER Execution information\n'
                         'location: [m_fluxes] obtainFluxNew\n'
                         'message: \n'
                         'MASTER issued '
                         'remarks.                                      \n'
                         '                                                            \n'
                         '---\n'
                         'message no:     3\n'
                         'type: warning\n'
                         'title: MASTER Execution information\n'
                         'location: [m_fluxes] obtainFluxNew\n'
                         'message: \n'
                         'MASTER issued '
                         'warnings.                                     \n'
                         '                                                            \n'
                         '---\n'
                         'message no:     4\n'
                         'type: warning\n'
                         'title: Complete model had to be used\n'
                         'location: [m_collProb] COLL_PROB_BPLANE\n'
                         'message: \n'
                         'The complete model for det. coll. prob computation '
                         'was used \n'
                         'Message repeated       186 '
                         'times                                                                                                                                                                        \n',
              'logfile': ' \n'
                         '                 __/__/    __/_/__/    __/__/__/  '
                         '_/__/_/\n'
                         '               __/   __/  __/    __/  __/        '
                         '__/\n'
                         '              __/__/__/  __/_/__/    __/__/      '
                         '__/__/\n'
                         '             __/   __/  __/    __/  __/             '
                         '__/\n'
                         '            __/   __/  __/     __/ __/__/__/  '
                         '_/__/_/\n'
                         ' \n'
                         '        Debris Risk Assessment and Mitigation '
                         'Analysis Tool Suite\n'
                         '       MASTER(-based) Assessment of Risk Event '
                         'Statistics Software\n'
                         '                           (DRAMA-ARES v3.1.0)\n'
                         ' \n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' ARES version  : 3.1.0\n'
                         ' Build date    : 23-Feb-21\n'
                         ' Platform      : x86_64-linux-gnu\n'
                         ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' [25/05/2022 16:00:39] INFO Starting ARES version '
                         '3.1.0\n'
                         ' [25/05/2022 16:00:39] INFO Starting progress '
                         'report\n'
                         ' [25/05/2022 16:00:39] INFO Loading input file\n'
                         '[[\n'
                         'WARNING Overriding user-input EMR\n'
                         ']]\n'
                         ' [25/05/2022 16:00:39] INFO Validating input file\n'
                         ' [25/05/2022 16:00:39] INFO Allocating resources\n'
                         ' [25/05/2022 16:00:39] INFO Loading covariance '
                         'tables\n'
                         ' [25/05/2022 16:00:39] INFO Computing population '
                         'flux\n'
                         'Calling MASTER v8.0.2 API..\n'
                         'Scanning datafiles for most recent reference '
                         'population...\n'
                         'Fetching population files: Man-made Population...\n'
                         'Most recent reference epoch: 2016/11\n'
                         'Target orbit scenario\n'
                         ' Currently using: FOCUS v2.5.7\n'
                         'Reading from propagation parameter file '
                         '/Users/alekskovacic/Desktop/python_test/\n'
                         'config/TOOLS/ARES/default/focus//focus.prm\n'
                         'File operation successful (79) OPENED '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                         '- static orbit\n'
                         '[[\n'
                         "REMARK in subroutine 'uinput':\n"
                         '  Target orbit epochs overrule simulation time for '
                         'target orbit scenario.\n'
                         ']]\n'
                         ' '
                         '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                         '#  1 /   1 :  2016 11 01 00    6883.14 0.00033  '
                         '87.75   76.44   92.59\n'
                         'Uncertainty indicators available!\n'
                         "Now processing 'Man-made Population' ...\n"
                         'Reading probability table header from '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/master_data//cond_20161101_00_leo.prb.\n'
                         '[[\n'
                         'WARNING in subroutine master_plugin:\n'
                         '  ARES DUMP: Data of bin  1 outside given bins. '
                         'Results will be incomplete!!!\n'
                         ']]\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '         ********** MASTER issued warning messages! '
                         '**********\n'
                         '         *************** MASTER issued remarks! '
                         '**************\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n',
              'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                        b'_/__/_/\n               __/   __/  __/    __/  __/   '
                        b'     __/\n              __/__/__/  __/_/__/    __/__/'
                        b'      __/__/\n             __/   __/  __/    __/  __/'
                        b'             __/\n            __/   __/  __/     __/ '
                        b'__/__/__/  _/__/_/\n \n        Debris Risk Assessm'
                        b'ent and Mitigation Analysis Tool Suite\n       MASTER'
                        b'(-based) Assessment of Risk Event Statistics Softwar'
                        b'e\n                           (DRAMA-ARES v3.1.0)'
                        b'\n \n --------------------------------------------'
                        b'---------------------------\n ARES version  : 3.1'
                        b'.0\n Build date    : 23-Feb-21\n Platform      : x'
                        b'86_64-linux-gnu\n Compiler      : GNU Fortran (Debian'
                        b' 8.3.0-6) 8.3.0\n -----------------------------------'
                        b'------------------------------------\n [25/05/2022 16'
                        b':00:39] INFO Starting ARES version 3.1.0\n [25/05/202'
                        b'2 16:00:39] INFO Starting progress report\n [25/05/20'
                        b'22 16:00:39] INFO Loading input file\n [25/05/2022 16'
                        b':00:39] \x1b[31mWARNING\x1b[0m Overriding user-inp'
                        b'ut EMR\n [25/05/2022 16:00:39] INFO Validating input '
                        b'file\n [25/05/2022 16:00:39] INFO Allocating resource'
                        b's\n [25/05/2022 16:00:39] INFO Loading covariance tab'
                        b'les\n [25/05/2022 16:00:39] INFO Computing population'
                        b' flux\n [25/05/2022 16:00:40] INFO MASTER issued rema'
                        b'rks\n [25/05/2022 16:00:40] \x1b[31mWARNING\x1b[0m '
                        b'MASTER issued warnings\n [25/05/2022 16:00:40] INFO C'
                        b'omputing detectable and catastrophic fluxes\n [25/05/'
                        b'2022 16:00:40] INFO Minimum detectable size for targ'
                        b'et orbit / m: 0.169E-01\n [25/05/2022 16:00:40] INFO '
                        b'Trying to merge low and high eccentricity bins\n [25/'
                        b'05/2022 16:00:40] INFO Unable to merge covs for low '
                        b'and high ecc. objects\n [25/05/2022 16:00:40] INFO Co'
                        b'mputing global fluxes\n [25/05/2022 16:00:40] INFO Co'
                        b'mputing collision rates\n [25/05/2022 16:00:40] INFO '
                        b'Computing manoeuvre rates and avoidance\n [25/05/2022'
                        b' 16:00:40] INFO Using 11 threads\n [25/05/2022 16:00:'
                        b'40] INFO Building output files\n [25/05/2022 16:00:40'
                        b'] INFO Building gnuplot driver files\n [25/05/2022 16'
                        b':00:40] INFO Program finished properly\n',
              'status': 'success'},
             {'annual_collision_p': 1.547e-07,
              'cola_evaluation': {'acpl': [0.0001, 0.001, 0.01],
                                  'f_rem_risk': [1.0, 1.0, 1.0],
                                  'f_res_risk': [1, 2, 3],
                                  'f_risk_red': [1, 2, 3],
                                  'false_alarm_rate': [0.0, 0.0, 0.0],
                                  'man_rate': [0.0, 0.0, 0.0],
                                  'rem_risk': [1.54682e-07,
                                               1.54682e-07,
                                               1.54682e-07],
                                  'res_risk': [0.0, 0.0, 0.0],
                                  'risk_red': [0.0, 0.0, 0.0]},
              'config': {'EMR_switch': 0,
                         'allowed_minimum_miss_distance': 1.5,
                         'aop': 92.5926,
                         'avoidance_manoeuvre_criteria': 0,
                         'collision_probability_alogrithm': 0,
                         'ecc': 0.000328,
                         'epoch': 3,
                         'id': 'PyAres',
                         'inc': 87.75,
                         'lead_time': 1,
                         'mass': 468,
                         'min_EMR_ratio': 40,
                         'particle_size_max': 0.01122,
                         'particle_size_min': 0.01,
                         'raan': 76.4433,
                         'radar_wavelength': 0.15,
                         'scaling_factor': -1,
                         'sma': 6883.137,
                         'spacecraft_radius': 0.1,
                         'target_collision_probability_level': 0.1,
                         'type_of_catalogue': 1,
                         'uncertainty_along': 0.2,
                         'uncertainty_cross': 1.0,
                         'uncertainty_radial': 0.075,
                         'uncertainty_type': 2},
              'errfile': '---\n'
                         'message no:     1\n'
                         'type: warning\n'
                         'title: ARES input\n'
                         'location: [m_AresInput] loadInputFromFile\n'
                         'message: \n'
                         'EMR switch set to '
                         'off                                       \n'
                         'User-input EMR is '
                         'ignored                                   \n'
                         '---\n'
                         'message no:     2\n'
                         'type: warning\n'
                         'title: MASTER Execution information\n'
                         'location: [m_fluxes] obtainFluxNew\n'
                         'message: \n'
                         'MASTER issued '
                         'remarks.                                      \n'
                         '                                                            \n',
              'logfile': ' \n'
                         '                 __/__/    __/_/__/    __/__/__/  '
                         '_/__/_/\n'
                         '               __/   __/  __/    __/  __/        '
                         '__/\n'
                         '              __/__/__/  __/_/__/    __/__/      '
                         '__/__/\n'
                         '             __/   __/  __/    __/  __/             '
                         '__/\n'
                         '            __/   __/  __/     __/ __/__/__/  '
                         '_/__/_/\n'
                         ' \n'
                         '        Debris Risk Assessment and Mitigation '
                         'Analysis Tool Suite\n'
                         '       MASTER(-based) Assessment of Risk Event '
                         'Statistics Software\n'
                         '                           (DRAMA-ARES v3.1.0)\n'
                         ' \n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' ARES version  : 3.1.0\n'
                         ' Build date    : 23-Feb-21\n'
                         ' Platform      : x86_64-linux-gnu\n'
                         ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' [25/05/2022 16:00:39] INFO Starting ARES version '
                         '3.1.0\n'
                         ' [25/05/2022 16:00:39] INFO Starting progress '
                         'report\n'
                         ' [25/05/2022 16:00:39] INFO Loading input file\n'
                         '[[\n'
                         'WARNING Overriding user-input EMR\n'
                         ']]\n'
                         ' [25/05/2022 16:00:39] INFO Validating input file\n'
                         ' [25/05/2022 16:00:39] INFO Allocating resources\n'
                         ' [25/05/2022 16:00:39] INFO Loading covariance '
                         'tables\n'
                         ' [25/05/2022 16:00:39] INFO Computing population '
                         'flux\n'
                         'Calling MASTER v8.0.2 API..\n'
                         'Scanning datafiles for most recent reference '
                         'population...\n'
                         'Fetching population files: Man-made Population...\n'
                         'Most recent reference epoch: 2016/11\n'
                         'Target orbit scenario\n'
                         ' Currently using: FOCUS v2.5.7\n'
                         'Reading from propagation parameter file '
                         '/Users/alekskovacic/Desktop/python_test/\n'
                         'config/TOOLS/ARES/default/focus//focus.prm\n'
                         'File operation successful (79) OPENED '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                         '- static orbit\n'
                         '[[\n'
                         "REMARK in subroutine 'uinput':\n"
                         '  Target orbit epochs overrule simulation time for '
                         'target orbit scenario.\n'
                         ']]\n'
                         ' '
                         '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                         '#  1 /   1 :  2016 11 01 00    6883.14 0.00033  '
                         '87.75   76.44   92.59\n'
                         'Uncertainty indicators available!\n'
                         "Now processing 'Man-made Population' ...\n"
                         'Reading probability table header from '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/master_data//cond_20161101_00_leo.prb.\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '         *************** MASTER issued remarks! '
                         '**************\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n',
              'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                        b'_/__/_/\n               __/   __/  __/    __/  __/   '
                        b'     __/\n              __/__/__/  __/_/__/    __/__/'
                        b'      __/__/\n             __/   __/  __/    __/  __/'
                        b'             __/\n            __/   __/  __/     __/ '
                        b'__/__/__/  _/__/_/\n \n        Debris Risk Assessm'
                        b'ent and Mitigation Analysis Tool Suite\n       MASTER'
                        b'(-based) Assessment of Risk Event Statistics Softwar'
                        b'e\n                           (DRAMA-ARES v3.1.0)'
                        b'\n \n --------------------------------------------'
                        b'---------------------------\n ARES version  : 3.1'
                        b'.0\n Build date    : 23-Feb-21\n Platform      : x'
                        b'86_64-linux-gnu\n Compiler      : GNU Fortran (Debian'
                        b' 8.3.0-6) 8.3.0\n -----------------------------------'
                        b'------------------------------------\n [25/05/2022 16'
                        b':00:39] INFO Starting ARES version 3.1.0\n [25/05/202'
                        b'2 16:00:39] INFO Starting progress report\n [25/05/20'
                        b'22 16:00:39] INFO Loading input file\n [25/05/2022 16'
                        b':00:39] \x1b[31mWARNING\x1b[0m Overriding user-inp'
                        b'ut EMR\n [25/05/2022 16:00:39] INFO Validating input '
                        b'file\n [25/05/2022 16:00:39] INFO Allocating resource'
                        b's\n [25/05/2022 16:00:39] INFO Loading covariance tab'
                        b'les\n [25/05/2022 16:00:39] INFO Computing population'
                        b' flux\n [25/05/2022 16:00:40] INFO MASTER issued rema'
                        b'rks\n [25/05/2022 16:00:40] INFO Computing detectable'
                        b' and catastrophic fluxes\n [25/05/2022 16:00:40] INFO'
                        b' Minimum detectable size for target orbit / m: 0.169'
                        b'E-01\n [25/05/2022 16:00:41] INFO Trying to merge low'
                        b' and high eccentricity bins\n [25/05/2022 16:00:41] I'
                        b'NFO Unable to merge covs for low and high ecc. objec'
                        b'ts\n [25/05/2022 16:00:41] INFO Computing global flux'
                        b'es\n [25/05/2022 16:00:41] INFO Computing collision r'
                        b'ates\n [25/05/2022 16:00:41] INFO Computing manoeuvre'
                        b' rates and avoidance\n [25/05/2022 16:00:41] INFO Usi'
                        b'ng 11 threads\n [25/05/2022 16:00:41] INFO Building o'
                        b'utput files\n [25/05/2022 16:00:41] INFO Building gnu'
                        b'plot driver files\n [25/05/2022 16:00:41] INFO Progra'
                        b'm finished properly\n',
              'status': 'success'}]}


"""
particle_size_min_list = [0.01413, 0.70795, 0.01, 4.46684]
particle_size_max_list = [0.01778, 0.89125, 0.01122, 5.62341]

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


sma_list = [2]
acpl_steps = 3
error_list_1 = ["error"]*len(sma_list)
for i in range(len(error_list_1)):
    all_parameters_list[0].append(error_list_1[i])
error_list_2 = ["error"]*acpl_steps*len(sma_list)
for j in range(1,10):
    for i in range(len(error_list_2)):  
        all_parameters_list[j].append(error_list_2[i])

for i in range(len(all_parameters_list)):
    print("All " + all_parameters_string[i] + ": "  + str(all_parameters_list[i]))


#for err in results["errors"]:
    #print([err][0]["config"]["particle_size_max"])

    #print(particle_size_max_list.index())


x = [4.151e-07, 1.547e-07, 'error', 'error']
y = [0.0001, 0.001, 0.01, 0.0001, 0.001, 0.01, 'error', 'error', 'error', 'error', 'error', 'error']


for i in range(len(results["errors"])*len(sma_list)):
    print("Value: "+str(results["errors"][i]["config"]["particle_size_max"]) + " Index: " +str(particle_size_max_list.index(results["errors"][i]["config"]["particle_size_max"])))
    x[particle_size_max_list.index(results["errors"][i]["config"]["particle_size_max"]) : particle_size_max_list.index(results["errors"][i]["config"]["particle_size_max"])] = ["error"]
del x[-len(sma_list)*len(results["errors"]):]

counter = acpl_steps-1
for i in range(len(results["errors"])*len(sma_list)):
    print(results["errors"][i]["config"]["particle_size_max"])
    y[particle_size_max_list.index(results["errors"][i]["config"]["particle_size_max"]) +counter : particle_size_max_list.index(results["errors"][i]["config"]["particle_size_max"])+counter] = ["error"]*acpl_steps
    counter = counter + acpl_steps + 1
del y[-acpl_steps*len(results["errors"])*len(sma_list):]


print(x)
print(y)


annual_collision_p=[1.547e-07, 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 7.727e-07, 4.151e-07, 2.374e-06]

for u in range(len(results["errors"])):
    #print("Value: "+str(results["errors"][u]["config"]["particle_size_max"]) + " Index: " +str(particle_size_max_list.index(results["errors"][u]["config"]["particle_size_max"])))
    index_variable = particle_size_max_list.index(results["errors"][u]["config"]["particle_size_max"])
    annual_collision_p[index_variable : index_variable] = ["error"]*len(sma_list)
del annual_collision_p[-len(results["errors"]):]

"""








############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
results = {'config': {'aop': 171.3,
            'ecc': 1e-06,
            'epoch': 21,
            'id': 'PyAres',
            'inc': [46, 90.1],
            'raan': 70.2,
            'sma': 7078.137,
            'spacecraft_radius': 0.1},
 'errors': [],
 'results': [{'annual_collision_p': 3.185e-05,
              'cola_evaluation': {'acpl': [1e-09,
                                           6e-09,
                                           3.6e-08,
                                           2.2e-07,
                                           1.3e-06,
                                           7.7e-06,
                                           4.6e-05,
                                           0.00028,
                                           0.0017,
                                           0.01],
                                  'f_rem_risk': [0.0328783,
                                                 0.0344028,
                                                 0.0407038,
                                                 0.0509426,
                                                 0.0792319,
                                                 0.179352,
                                                 0.231009,
                                                 0.313893,
                                                 0.521209,
                                                 0.680044],
                                  'f_res_risk': [0.0,
                                                 0.0,
                                                 0.0,
                                                 0.0,
                                                 0.0,
                                                 0.0226251,
                                                 0.0841474,
                                                 0.18286,
                                                 0.42977,
                                                 0.618939],
                                  'f_risk_red': [1.0,
                                                 1.0,
                                                 1.0,
                                                 1.0,
                                                 1.0,
                                                 0.977375,
                                                 0.915853,
                                                 0.81714,
                                                 0.57023,
                                                 0.381061],
                                  'false_alarm_rate': [0.999999,
                                                       0.999998,
                                                       0.999995,
                                                       0.999989,
                                                       0.999973,
                                                       0.999828,
                                                       0.999287,
                                                       0.998134,
                                                       0.992099,
                                                       0.950758],
                                  'man_rate': [37.7142,
                                               20.3176,
                                               6.0529,
                                               2.79121,
                                               1.08181,
                                               0.151513,
                                               0.0343246,
                                               0.0117079,
                                               0.00192973,
                                               0.00020692],
                                  'rem_risk': [1.04702e-06,
                                               1.09556e-06,
                                               1.29622e-06,
                                               1.62228e-06,
                                               2.52316e-06,
                                               5.71152e-06,
                                               7.35654e-06,
                                               9.99599e-06,
                                               1.6598e-05,
                                               2.16562e-05],
                                  'res_risk': [0.0,
                                               0.0,
                                               0.0,
                                               0.0,
                                               0.0,
                                               6.04966e-07,
                                               2.24999e-06,
                                               4.88944e-06,
                                               1.14915e-05,
                                               1.65496e-05],
                                  'risk_red': [3.07982e-05,
                                               3.07497e-05,
                                               3.0549e-05,
                                               3.0223e-05,
                                               2.93221e-05,
                                               2.61337e-05,
                                               2.44887e-05,
                                               2.18492e-05,
                                               1.52472e-05,
                                               1.01891e-05]},
              'config': {'aop': 171.3,
                         'ecc': 1e-06,
                         'epoch': 21,
                         'id': 'PyAres',
                         'inc': 46,
                         'raan': 70.2,
                         'sma': 7078.137,
                         'spacecraft_radius': 0.1},
              'errfile': '---\n'
                         'message no:     1\n'
                         'type: warning\n'
                         'title: ARES input\n'
                         'location: [m_AresInput] loadInputFromFile\n'
                         'message: \n'
                         'EMR switch set to '
                         'off                                       \n'
                         'User-input EMR is '
                         'ignored                                   \n'
                         '---\n'
                         'message no:     2\n'
                         'type: warning\n'
                         'title: MASTER Execution information\n'
                         'location: [m_fluxes] obtainFluxNew\n'
                         'message: \n'
                         'MASTER issued '
                         'remarks.                                      \n'
                         '                                                            \n'
                         '---\n'
                         'message no:     3\n'
                         'type: warning\n'
                         'title: Complete model had to be used\n'
                         'location: [m_collProb] COLL_PROB_BPLANE\n'
                         'message: \n'
                         'The complete model for det. coll. prob computation '
                         'was used \n'
                         'Message repeated      4433 '
                         'times                                                                                                                                                                        \n',
              'logfile': ' \n'
                         '                 __/__/    __/_/__/    __/__/__/  '
                         '_/__/_/\n'
                         '               __/   __/  __/    __/  __/        '
                         '__/\n'
                         '              __/__/__/  __/_/__/    __/__/      '
                         '__/__/\n'
                         '             __/   __/  __/    __/  __/             '
                         '__/\n'
                         '            __/   __/  __/     __/ __/__/__/  '
                         '_/__/_/\n'
                         ' \n'
                         '        Debris Risk Assessment and Mitigation '
                         'Analysis Tool Suite\n'
                         '       MASTER(-based) Assessment of Risk Event '
                         'Statistics Software\n'
                         '                           (DRAMA-ARES v3.1.0)\n'
                         ' \n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' ARES version  : 3.1.0\n'
                         ' Build date    : 23-Feb-21\n'
                         ' Platform      : x86_64-linux-gnu\n'
                         ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' [05/03/2022 10:11:57] INFO Starting ARES version '
                         '3.1.0\n'
                         ' [05/03/2022 10:11:57] INFO Starting progress '
                         'report\n'
                         ' [05/03/2022 10:11:57] INFO Loading input file\n'
                         '[[\n'
                         'WARNING Overriding user-input EMR\n'
                         ']]\n'
                         ' [05/03/2022 10:11:57] INFO Validating input file\n'
                         ' [05/03/2022 10:11:57] INFO Allocating resources\n'
                         ' [05/03/2022 10:11:57] INFO Loading covariance '
                         'tables\n'
                         ' [05/03/2022 10:11:57] INFO Computing population '
                         'flux\n'
                         'Calling MASTER v8.0.2 API..\n'
                         'Scanning datafiles for most recent reference '
                         'population...\n'
                         'Fetching population files: Man-made Population...\n'
                         'Most recent reference epoch: 2016/11\n'
                         'Target orbit scenario\n'
                         ' Currently using: FOCUS v2.5.7\n'
                         'Reading from propagation parameter file '
                         '/Users/alekskovacic/Desktop/python_test/\n'
                         'config/TOOLS/ARES/default/focus//focus.prm\n'
                         'File operation successful (79) OPENED '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                         '- static orbit\n'
                         '[[\n'
                         "REMARK in subroutine 'uinput':\n"
                         '  Target orbit epochs overrule simulation time for '
                         'target orbit scenario.\n'
                         ']]\n'
                         ' '
                         '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                         '#  1 /   1 :  2018 11 01 00    7078.14 0.00000  '
                         '46.00   70.20  171.30\n'
                         'Uncertainty indicators available!\n'
                         "Now processing 'Man-made Population' ...\n"
                         'Reading probability table header from '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/master_data//cond_20181101_01_leo.prb.\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '         *************** MASTER issued remarks! '
                         '**************\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n',
              'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                        b'_/__/_/\n               __/   __/  __/    __/  __/   '
                        b'     __/\n              __/__/__/  __/_/__/    __/__/'
                        b'      __/__/\n             __/   __/  __/    __/  __/'
                        b'             __/\n            __/   __/  __/     __/ '
                        b'__/__/__/  _/__/_/\n \n        Debris Risk Assessm'
                        b'ent and Mitigation Analysis Tool Suite\n       MASTER'
                        b'(-based) Assessment of Risk Event Statistics Softwar'
                        b'e\n                           (DRAMA-ARES v3.1.0)'
                        b'\n \n --------------------------------------------'
                        b'---------------------------\n ARES version  : 3.1'
                        b'.0\n Build date    : 23-Feb-21\n Platform      : x'
                        b'86_64-linux-gnu\n Compiler      : GNU Fortran (Debian'
                        b' 8.3.0-6) 8.3.0\n -----------------------------------'
                        b'------------------------------------\n [05/03/2022 10'
                        b':11:57] INFO Starting ARES version 3.1.0\n [05/03/202'
                        b'2 10:11:57] INFO Starting progress report\n [05/03/20'
                        b'22 10:11:57] INFO Loading input file\n [05/03/2022 10'
                        b':11:57] \x1b[31mWARNING\x1b[0m Overriding user-inp'
                        b'ut EMR\n [05/03/2022 10:11:57] INFO Validating input '
                        b'file\n [05/03/2022 10:11:57] INFO Allocating resource'
                        b's\n [05/03/2022 10:11:57] INFO Loading covariance tab'
                        b'les\n [05/03/2022 10:11:57] INFO Computing population'
                        b' flux\n [05/03/2022 10:12:03] INFO MASTER issued rema'
                        b'rks\n [05/03/2022 10:12:03] INFO Computing detectable'
                        b' and catastrophic fluxes\n [05/03/2022 10:12:03] INFO'
                        b' Minimum detectable size for target orbit / m: 0.492'
                        b'E-01\n [05/03/2022 10:12:03] INFO Trying to merge low'
                        b' and high eccentricity bins\n [05/03/2022 10:12:03] I'
                        b'NFO Unable to merge covs for low and high ecc. objec'
                        b'ts\n [05/03/2022 10:12:03] INFO Computing global flux'
                        b'es\n [05/03/2022 10:12:03] INFO Computing collision r'
                        b'ates\n [05/03/2022 10:12:03] INFO Computing manoeuvre'
                        b' rates and avoidance\n [05/03/2022 10:12:03] INFO Usi'
                        b'ng 11 threads\n [05/03/2022 10:12:37] INFO Building o'
                        b'utput files\n [05/03/2022 10:12:37] INFO Building gnu'
                        b'plot driver files\n [05/03/2022 10:12:37] INFO Progra'
                        b'm finished properly\n',
              'status': 'success'},
             {'annual_collision_p': 4.376e-05,
              'cola_evaluation': {'acpl': [1e-09,
                                           6e-09,
                                           3.6e-08,
                                           2.2e-07,
                                           1.3e-06,
                                           7.7e-06,
                                           4.6e-05,
                                           0.00028,
                                           0.0017,
                                           0.01],
                                  'f_rem_risk': [0.0493873,
                                                 0.0504405,
                                                 0.0555632,
                                                 0.0631818,
                                                 0.0882343,
                                                 0.16647,
                                                 0.244132,
                                                 0.357986,
                                                 0.555546,
                                                 0.733085],
                                  'f_res_risk': [0.0,
                                                 0.0,
                                                 0.0,
                                                 0.0,
                                                 0.0,
                                                 0.00378973,
                                                 0.0966087,
                                                 0.232684,
                                                 0.468802,
                                                 0.680991],
                                  'f_risk_red': [1.0,
                                                 1.0,
                                                 1.0,
                                                 1.0,
                                                 1.0,
                                                 0.99621,
                                                 0.903391,
                                                 0.767316,
                                                 0.531198,
                                                 0.319009],
                                  'false_alarm_rate': [0.999999,
                                                       0.999998,
                                                       0.999994,
                                                       0.999988,
                                                       0.99997,
                                                       0.999849,
                                                       0.999454,
                                                       0.998315,
                                                       0.991696,
                                                       0.956529],
                                  'man_rate': [38.0671,
                                               21.5501,
                                               6.75895,
                                               3.36893,
                                               1.31715,
                                               0.241685,
                                               0.0606015,
                                               0.016676,
                                               0.00234251,
                                               0.000268719],
                                  'rem_risk': [2.16142e-06,
                                               2.20751e-06,
                                               2.43171e-06,
                                               2.76513e-06,
                                               3.86155e-06,
                                               7.28551e-06,
                                               1.06843e-05,
                                               1.56671e-05,
                                               2.43133e-05,
                                               3.20832e-05],
                                  'res_risk': [0.0,
                                               0.0,
                                               0.0,
                                               0.0,
                                               0.0,
                                               1.38772e-07,
                                               3.53761e-06,
                                               8.52039e-06,
                                               1.71666e-05,
                                               2.49365e-05],
                                  'risk_red': [4.16033e-05,
                                               4.15572e-05,
                                               4.1333e-05,
                                               4.09995e-05,
                                               3.99031e-05,
                                               3.64792e-05,
                                               3.30803e-05,
                                               2.80975e-05,
                                               1.94514e-05,
                                               1.16814e-05]},
              'config': {'aop': 171.3,
                         'ecc': 1e-06,
                         'epoch': 21,
                         'id': 'PyAres',
                         'inc': 90.1,
                         'raan': 70.2,
                         'sma': 7078.137,
                         'spacecraft_radius': 0.1},
              'errfile': '---\n'
                         'message no:     1\n'
                         'type: warning\n'
                         'title: ARES input\n'
                         'location: [m_AresInput] loadInputFromFile\n'
                         'message: \n'
                         'EMR switch set to '
                         'off                                       \n'
                         'User-input EMR is '
                         'ignored                                   \n'
                         '---\n'
                         'message no:     2\n'
                         'type: warning\n'
                         'title: MASTER Execution information\n'
                         'location: [m_fluxes] obtainFluxNew\n'
                         'message: \n'
                         'MASTER issued '
                         'remarks.                                      \n'
                         '                                                            \n'
                         '---\n'
                         'message no:     3\n'
                         'type: warning\n'
                         'title: Complete model had to be used\n'
                         'location: [m_collProb] COLL_PROB_BPLANE\n'
                         'message: \n'
                         'The complete model for det. coll. prob computation '
                         'was used \n'
                         'Message repeated      4108 '
                         'times                                                                                                                                                                        \n',
              'logfile': ' \n'
                         '                 __/__/    __/_/__/    __/__/__/  '
                         '_/__/_/\n'
                         '               __/   __/  __/    __/  __/        '
                         '__/\n'
                         '              __/__/__/  __/_/__/    __/__/      '
                         '__/__/\n'
                         '             __/   __/  __/    __/  __/             '
                         '__/\n'
                         '            __/   __/  __/     __/ __/__/__/  '
                         '_/__/_/\n'
                         ' \n'
                         '        Debris Risk Assessment and Mitigation '
                         'Analysis Tool Suite\n'
                         '       MASTER(-based) Assessment of Risk Event '
                         'Statistics Software\n'
                         '                           (DRAMA-ARES v3.1.0)\n'
                         ' \n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' ARES version  : 3.1.0\n'
                         ' Build date    : 23-Feb-21\n'
                         ' Platform      : x86_64-linux-gnu\n'
                         ' Compiler      : GNU Fortran (Debian 8.3.0-6) 8.3.0\n'
                         ' '
                         '-----------------------------------------------------------------------\n'
                         ' [05/03/2022 10:12:37] INFO Starting ARES version '
                         '3.1.0\n'
                         ' [05/03/2022 10:12:37] INFO Starting progress '
                         'report\n'
                         ' [05/03/2022 10:12:37] INFO Loading input file\n'
                         '[[\n'
                         'WARNING Overriding user-input EMR\n'
                         ']]\n'
                         ' [05/03/2022 10:12:37] INFO Validating input file\n'
                         ' [05/03/2022 10:12:37] INFO Allocating resources\n'
                         ' [05/03/2022 10:12:37] INFO Loading covariance '
                         'tables\n'
                         ' [05/03/2022 10:12:37] INFO Computing population '
                         'flux\n'
                         'Calling MASTER v8.0.2 API..\n'
                         'Scanning datafiles for most recent reference '
                         'population...\n'
                         'Fetching population files: Man-made Population...\n'
                         'Most recent reference epoch: 2016/11\n'
                         'Target orbit scenario\n'
                         ' Currently using: FOCUS v2.5.7\n'
                         'Reading from propagation parameter file '
                         '/Users/alekskovacic/Desktop/python_test/\n'
                         'config/TOOLS/ARES/default/focus//focus.prm\n'
                         'File operation successful (79) OPENED '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/TOOLS/ARES/default/focus//focus.prm\n'
                         '- static orbit\n'
                         '[[\n'
                         "REMARK in subroutine 'uinput':\n"
                         '  Target orbit epochs overrule simulation time for '
                         'target orbit scenario.\n'
                         ']]\n'
                         ' '
                         '_____________YYYY_MM_DD_HH__SMA_______ECC_____INC_____RAAN____AoP\n'
                         '#  1 /   1 :  2018 11 01 00    7078.14 0.00000  '
                         '90.10   70.20  171.30\n'
                         'Uncertainty indicators available!\n'
                         "Now processing 'Man-made Population' ...\n"
                         'Reading probability table header from '
                         '/Users/alekskovacic/Desktop/python_test/co\n'
                         'nfig/master_data//cond_20181101_01_leo.prb.\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '         *************** MASTER issued remarks! '
                         '**************\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n'
                         '\n'
                         ' '
                         '_________________________________________________________________________\n'
                         '\n',
              'output': b' \n                 __/__/    __/_/__/    __/__/__/  '
                        b'_/__/_/\n               __/   __/  __/    __/  __/   '
                        b'     __/\n              __/__/__/  __/_/__/    __/__/'
                        b'      __/__/\n             __/   __/  __/    __/  __/'
                        b'             __/\n            __/   __/  __/     __/ '
                        b'__/__/__/  _/__/_/\n \n        Debris Risk Assessm'
                        b'ent and Mitigation Analysis Tool Suite\n       MASTER'
                        b'(-based) Assessment of Risk Event Statistics Softwar'
                        b'e\n                           (DRAMA-ARES v3.1.0)'
                        b'\n \n --------------------------------------------'
                        b'---------------------------\n ARES version  : 3.1'
                        b'.0\n Build date    : 23-Feb-21\n Platform      : x'
                        b'86_64-linux-gnu\n Compiler      : GNU Fortran (Debian'
                        b' 8.3.0-6) 8.3.0\n -----------------------------------'
                        b'------------------------------------\n [05/03/2022 10'
                        b':12:37] INFO Starting ARES version 3.1.0\n [05/03/202'
                        b'2 10:12:37] INFO Starting progress report\n [05/03/20'
                        b'22 10:12:37] INFO Loading input file\n [05/03/2022 10'
                        b':12:37] \x1b[31mWARNING\x1b[0m Overriding user-inp'
                        b'ut EMR\n [05/03/2022 10:12:37] INFO Validating input '
                        b'file\n [05/03/2022 10:12:37] INFO Allocating resource'
                        b's\n [05/03/2022 10:12:37] INFO Loading covariance tab'
                        b'les\n [05/03/2022 10:12:37] INFO Computing population'
                        b' flux\n [05/03/2022 10:12:43] INFO MASTER issued rema'
                        b'rks\n [05/03/2022 10:12:43] INFO Computing detectable'
                        b' and catastrophic fluxes\n [05/03/2022 10:12:43] INFO'
                        b' Minimum detectable size for target orbit / m: 0.492'
                        b'E-01\n [05/03/2022 10:12:43] INFO Trying to merge low'
                        b' and high eccentricity bins\n [05/03/2022 10:12:43] I'
                        b'NFO Unable to merge covs for low and high ecc. objec'
                        b'ts\n [05/03/2022 10:12:43] INFO Computing global flux'
                        b'es\n [05/03/2022 10:12:43] INFO Computing collision r'
                        b'ates\n [05/03/2022 10:12:43] INFO Computing manoeuvre'
                        b' rates and avoidance\n [05/03/2022 10:12:43] INFO Usi'
                        b'ng 11 threads\n [05/03/2022 10:13:18] INFO Building o'
                        b'utput files\n [05/03/2022 10:13:18] INFO Building gnu'
                        b'plot driver files\n [05/03/2022 10:13:18] INFO Progra'
                        b'm finished properly\n',
              'status': 'success'}]}



"""
#Sammeln aller annual_collision_probability Werte aus den einzelnen Durchläufen
annual_collision_p = []
for res in results["results"]:
    annual_collision_p.append(res['annual_collision_p'])
print("All Annual Collision Probability (annual_collision_p) values: " + str(annual_collision_p))

#Sammeln aller Accepted Collision Probability (acpl) Werte aus den einzelnen Durchläufen
acpl = []
for res in results["results"]:
    for single_run_res in res["cola_evaluation"]["acpl"]:
        acpl.append(single_run_res)
print("All Accepted Collision Probability (acpl) values: " + str(acpl))

#Sammeln aller Residual Risk Werte aus den einzelnen Durchläufen
res_risk = []
for res in results["results"]:
    for single_run_res in res["cola_evaluation"]["res_risk"]:
        res_risk.append(single_run_res)
print("All Residual Risk values: " + str(res_risk))

#Sammeln aller Risk Reduction Werte aus den einzelnen Durchläufen
risk_red = []
for res in results["results"]:
    for single_run_res in res["cola_evaluation"]["risk_red"]:
        risk_red.append(single_run_res)
print("All Risk Reduction values: " + str(risk_red))


next_run = 0
end_of_list = 10
# Solange durchiterieren, bis man durch die gesammelten acpl Liste durchkommt (man hätte auch risk_red oder res_risk nehmen können, 
# da diese auch 10 Einträge haben)
while next_run < len(acpl):
    start_of_list = 0 + next_run
    end_of_list = end_of_list + next_run
    x = acpl[start_of_list:end_of_list]
    y1 = res_risk[start_of_list:end_of_list]
    y2 = risk_red[start_of_list:end_of_list]
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.ylabel("Risk")
    plt.xlabel("Accepted Collision Probability Level")
    plt.show()
    next_run = next_run + 10
"""
"""
import matplotlib.pyplot as plt
x = results["results"][0]["cola_evaluation"]["acpl"]
y1 = results["results"][0]["cola_evaluation"]["res_risk"]
y2 = results["results"][0]["cola_evaluation"]["risk_red"]
plt.plot(x,y1)
plt.plot(x,y2)
plt.ylabel("Risk")
plt.xlabel("Accepted Collision Probability Level")
plt.show()
"""

annual_collision_p = [4.376e-05, 3.039e-05, 4.376e-05, 3.039e-05]
acpl = [1e-09, 6e-09, 3.6e-08, 2.2e-07, 1.3e-06, 7.7e-06, 4.6e-05, 0.00028, 0.0017, 0.01, 1e-09, 6e-09, 3.6e-08, 2.2e-07, 1.3e-06, 7.7e-06, 4.6e-05, 0.00028, 0.0017, 0.01, 1e-09, 6e-09, 3.6e-08, 2.2e-07, 1.3e-06, 7.7e-06, 4.6e-05, 0.00028, 0.0017, 0.01, 1e-09, 6e-09, 3.6e-08, 2.2e-07, 1.3e-06, 7.7e-06, 4.6e-05, 0.00028, 0.0017, 0.01]
res_risk = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.46648e-06, 1.24501e-05, 2.10963e-05, 2.88662e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.78525e-06, 1.14834e-05, 1.58396e-05, 1.92528e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 1.38772e-07, 3.53761e-06, 8.52039e-06, 1.71666e-05, 2.49365e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 6.15878e-07, 3.49521e-06, 7.19336e-06, 1.15496e-05, 1.49628e-05]
risk_red = [6.79599e-05, 6.75114e-05, 6.54377e-05, 6.31158e-05, 5.76603e-05, 4.33548e-05, 3.30812e-05, 2.80975e-05, 1.94514e-05, 1.16814e-05, 5.42558e-05, 5.39611e-05, 5.25983e-05, 5.06726e-05, 4.40737e-05, 2.65856e-05, 1.77159e-05, 1.40177e-05, 9.66149e-06, 6.2483e-06, 4.16033e-05, 4.15572e-05, 4.1333e-05, 4.09995e-05, 3.99031e-05, 3.64792e-05, 3.30803e-05, 2.80975e-05, 1.94514e-05, 1.16814e-05, 2.55363e-05, 2.55101e-05, 2.53799e-05, 2.51064e-05, 2.39853e-05, 2.05952e-05, 1.77159e-05, 1.40177e-05, 9.66149e-06, 6.2483e-06]
"""
x1 = acpl[0:10]
y11 = res_risk[0:10]
y12 = risk_red[0:10]

x2 = acpl[10:20]
y21 = res_risk[10:20]
y22 = risk_red[10:20]

x3 = acpl[20:30]
y31 = res_risk[20:30]
y32 = risk_red[20:30]

x4 = acpl[30:40]
y41 = res_risk[30:40]
y42 = risk_red[30:40]

plt.plot(x1, y11, "o-", color = "green")
plt.plot(x1, y12, "o-", color = "darkgreen")
plt.plot(x2, y21, "o-", color = "blue")
plt.plot(x2, y22, "o-", color = "darkblue")
plt.plot(x3, y31, "o-", color = "grey")
plt.plot(x3, y32, "o-", color = "darkgrey")
plt.plot(x4, y41, "o-", color = "red")
plt.plot(x4, y42, "o-", color = "darkred")
plt.ylabel("Risk")
plt.xlabel("Accepted Collision Probability Level")
plt.show()

"""
"""
start = 0
end = 10
x = acpl[start:end]
y1 = res_risk[start:end]
y2 = risk_red[start:end]
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
"""

"""
start = 0
end = 10
# Solange durchiterieren, bis man durch die gesammelten acpl Liste durchkommt (man hätte auch risk_red oder res_risk nehmen können, 
# da diese auch 10 Einträge haben)
while end <= len(acpl):
    x = acpl[start:end]
    y1 = res_risk[start:end]
    y2 = risk_red[start:end]
    plt.plot(x,y1, label = "Residual Risk")
    #plt.plot(x,y2, label = "Risk Reduction")
    plt.legend(loc="upper center", prop={'size': 8})
    plt.ylabel("Risk")
    plt.xlabel("Accepted Collision Probability Level")
    start = start + 10
    end = end +10
plt.show()
"""

lambda_radar = 0.3/1000
d_ref_radar = 0.32/1000
h_ref_radar = 2000
exp_radar = 2

d_ref_optical = 0.7/1000
h_ref_optical = 36000
exp_optical = -0.5


h_list = [
    100,200,300,400,500,600,700,800,900,1000,
    2000,3000,4000,5000,6000,7000,8000,9000,10000,
    20000,30000
]

d_min_final_list=[]
#zum plotten der einzelnen Geraden
d_min_radar_line = []
d_min_optical_line = []
d_rcs_line = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar*((h_list[i]/h_ref_radar)**exp_radar)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar**2)*((h_list[i]/h_ref_radar)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #d_min_final in cm umrechnen für die besser Darstellbarkeit
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list.append(d_min_final)
    #zum plotten der einzelnen Geraden
    d_min_radar_line.append(d_min_radar*1000*100)
    d_min_optical_line.append(d_min_optical*1000*100)
    d_rcs_line.append(d_rcs*1000*100)

#print(d_min_final_list)

###############################################################################

lambda_radar_SF = 0.1/1000 #noch umändern auf 0.1
d_ref_radar_SF = 0.1/1000
h_ref_radar_SF = 2000
exp_radar_SF = 2
d_min_final_list_SF = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_SF*((h_list[i]/h_ref_radar_SF)**exp_radar_SF)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_SF**2)*((h_list[i]/h_ref_radar_SF)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_SF)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #d_min_final in cm umrechnen für die besser Darstellbarkeit
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_SF.append(d_min_final)

#print(d_min_final_list)

################################################################

lambda_radar_SF_2 = 0.075/1000 #noch umändern auf 0.1
d_ref_radar_SF_2 = 0.1/1000
h_ref_radar_SF_2 = 2000
exp_radar_SF_2 = 2
d_min_final_list_SF_2 = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_SF_2*((h_list[i]/h_ref_radar_SF_2)**exp_radar_SF)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_SF_2**2)*((h_list[i]/h_ref_radar_SF_2)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_SF_2)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #d_min_final in cm umrechnen für die besser Darstellbarkeit
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_SF_2.append(d_min_final)

#print(d_min_final_list)

"""
#plt.plot(h_list, d_min_final_list[0:len(h_list)], label = "Detectable Size: " + str(d_ref_radar*1000*100) + "cm, " + "Wavelength: " + str(lambda_radar*1000) + "m")
plt.plot(h_list, d_min_final_list_SF[0:len(h_list)], label = "Detectable Size: " + str(d_ref_radar_SF*1000*100) + "cm, " + "Wavelength: " + str(lambda_radar_SF*1000) +"m")
plt.plot(h_list, d_min_final_list_SF_2[0:len(h_list)], label = "Detectable Size: " + str(d_ref_radar_SF_2*1000*100) + "cm, " + "Wavelength: " + str(lambda_radar_SF_2*1000) + "m")
plt.yscale("log")
plt.xscale("log")
plt.legend(loc="lower right", prop={'size': 8})
plt.ylabel("Minimal Detectable Diamater d [cm]")
plt.xlabel("Altitude h [km]")

#plt.axhline(y=3.1, color = "r", linestyle = "-")
#plt.axvline(x=500, color = "r", linestyle = "-")
#plt.axhline(y=10, color = "y", linestyle = "-")
#plt.axvline(x=2000, color = "y", linestyle = "-")
#plt.axhline(y=1, color="g", linestyle="-")

plt.axhline(y=1, color = "r", linestyle = "-")
plt.axvline(x=300, color = "r", linestyle = "-")

plt.minorticks_on()
#axis = "y"
plt.grid(which = "both")"""

#zum plotten der einzelnen Geraden
h_list_first = [100,900]
h_list_second = [900,5000]
h_list_third = [5000, 30000]
plt.plot(h_list_first, d_min_radar_line)
plt.plot(h_list_second, d_min_optical_line)
plt.plot(h_list_third, d_rcs_line)
plt.yscale("log")
plt.xscale("log")

plt.show()



"""import itertools
sma_list = [500,600,700, 800]
inc_list = [45,60,75, 90]
d_ref_list = [0.32]
annual_collision_p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

sma_list_for_plot = []
inc_list_for_plot = []
d_ref_list_for_plot = []

#Hier die Parameter definieren, die variiert werden
first_parameter = sma_list
second_parameter = inc_list

new_first_parameter = len(second_parameter)*first_parameter
new_second_parameter = list(itertools.chain.from_iterable(itertools.repeat(x, len(first_parameter)) for x in second_parameter))

num_of_combinations = len(first_parameter) * len(second_parameter)
w = 0
while w < num_of_combinations:
    sma_list_for_plot += 10*[new_first_parameter[w]]
    inc_list_for_plot += 10*[new_second_parameter[w]]
    w = w+1

for j in range(len(d_ref_list)):
    d_ref_list_for_plot += 10*num_of_combinations*[d_ref_list[j]]

annual_collision_p_for_plot = list(itertools.chain.from_iterable(itertools.repeat(l, 10) for l in annual_collision_p))

print(len(sma_list_for_plot))
print(len(inc_list_for_plot))
print(len(d_ref_list_for_plot))
print(len(annual_collision_p_for_plot))"""

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

"""scaling_factor_table[:4, 4:6] = 0.7
scaling_factor_table[:4, 4:6] = 0.8
scaling_factor_table[12:16, 4:6] = 0.7
scaling_factor_table[24:28, 4:6] = 0.7
print(scaling_factor_table)
"""




config = {
        # Standard: "particle_size_min": 0.01
        "particle_size_min": 0.01,
        "particle_size_max": 100,
        #Space Fence works in S-Band i.e. radar_wavelength = 0.075m-0.15m
        "radar_wavelength": 33,
        "EMR_switch": 0,
        "min_EMR_ratio": 40,
        #mass of spacecraft
        "mass": 468,
        #Swarm B = 4.55m
        "spacecraft_radius": 4.55,
        "sma": [300, 400, 500],
        #Swarm B inlicnation = 87.75
        "inc": [90, 56],
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
        "scaling_factor": -1,
        "collision_probability_alogrithm": 0,
        "avoidance_manoeuvre_criteria": 0,
        "target_collision_probability_level": 0.1,
        "allowed_minimum_miss_distance": 1.5
    }
d_ref_list = [0.1]
acpl_input={"min_order": 3, "max_order": 4, "n_steps" : 5}
data = {**config, **{"d_ref": d_ref_list}, **acpl_input, **{"scaling_factor_table" : scaling_factor_table}}

import pickle
import json

"""#save in format that could be used in other files
with open('input_parameters.pkl', 'wb') as f:
    pickle.dump(data, f)

#save in readable format
with open("input_parameters.txt", 'w') as f: 
    for key, value in data.items(): 
        f.write('%s:%s\n' % (key, value))"""


"""with open('input_parameters.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)

loaded_dict["epoch"].strftime('%Y-%m-%d')
pprint(loaded_dict)"""





