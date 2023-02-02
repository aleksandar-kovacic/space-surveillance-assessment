#%% Import
import numpy as np
import pathlib

from datetime import datetime
from pprint import pprint

from drama import ares
from drama import utils

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
CONFIG_DIR = SCRIPT_DIR / "config"

utils.config_file_paths_dict["macos"] = [str(CONFIG_DIR) + "/{}/config.json"]

# May not be needed for newest python_drama_package

ares._default_input_lines = {
    "ares.inp": {
        "epoch": (29, (0, 1, 2), lambda x: x.strftime("%Y %m %d")),
        "id": (0, 0, lambda x: str(x)),
        "particle_size_min": (4, 0, lambda x: str(x)),
        "particle_size_max": (5, 0, lambda x: str(x)),
        "sma": (24, 0, lambda x: str(x)),
        "ecc": (25, 0, lambda x: str(x)),
        "inc": (26, 0, lambda x: str(x)),
        "raan": (27, 0, lambda x: str(x)),
        "aop": (28, 0, lambda x: str(x)),
        "spacecraft_radius": (23, 0, lambda x: str(x)),
        "mass": (22, 0, lambda x: str(x)),
        "functionality": (3, 0, lambda x: str(x)),
        "radar_wavelength": (16, 0, lambda x: str(x)),
        "EMR_switch": (20, 0, lambda x: str(x)),
        "uncertainty_type": (30, 0, lambda x: str(x)),
        "uncertainty_along": (31, 0, lambda x: str(x)),
        "uncertainty_cross": (32, 0, lambda x: str(x)),
        "uncertainty_radial": (33, 0, lambda x: str(x)),
        "lead_time": (34, 0, lambda x: str(x)),
    },
    "ares.cfg": {
        "ARESMASTERDataDirectory": (3, 1, lambda x: (x + "/", True)),
        "input_focus": (4, 1, lambda x: (x + "/", True)),
    },
}


def update_line_column(line_no, column, lines, value_str):
    """Update a column value in ARES input file"""

    line = lines[line_no].split()
    line[column] = value_str
    line = " " + " ".join(line) + "\n"
    lines[line_no] = line
    return lines


def update_acpl_param(lines, min_order, max_order, n_steps):
    """Update ACPL evaluation array"""

    if n_steps > 10:
        raise ValueError("Only values upto 10 accepted.")

    params = np.logspace(min_order, max_order, n_steps)

    lines = update_line_column(280, 0, lines, "{:d}".format(n_steps))
    lines[281] = "x " * n_steps
    for i in range(n_steps):
        lines = update_line_column(281, i, lines, "{:2.1e}".format(params[i]))

    return lines


def update_default_config(d_ref=0.32, h_ref=2000):
    template_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares_template.inp"
    input_path = str(CONFIG_DIR) + "/TOOLS/ARES/default/ares.inp"
    with open(template_path, "r") as f:
        lines = f.readlines()

    lines = update_line_column(69, 0, lines, "{:3.2e}".format(d_ref))
    lines = update_line_column(70, 0, lines, "{:3.2e}".format(h_ref))
    #lines = update_acpl_param(lines, -9, -2, 10)
    lines = update_acpl_param(lines, -4, -2, 1)

    with open(input_path, "w") as f:
        f.writelines(lines)


def run(config, d_ref):
    update_default_config(d_ref=d_ref)
    return ares.run(config, parallel=False)


def main():
    #%% Run demo
    _R_EARTH = 6378.137

    config = {
        "particle_size_min": 0.01,
        "particle_size_max": 100,
        "epoch": datetime(2016, 11, 1),
        "sma": [_R_EARTH + 505],
        "inc": [90],
        "ecc": 3.28e-4,
        "raan": 76.4433,
        "aop": 92.5926,
        "spacecraft_radius": 4.55,

    }
    #dependent_variables = []
    results = run(config, d_ref=0.32)

    pprint(results)


if __name__ == "__main__":
    main()
