import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

R = 6378.137

with open('MASTER_2022_altitude_declination.txt', "r") as f:
    lines = f.readlines()

density_list = []
altitude_list = []
declination_list = []

for i in range(2,len(lines)):
    if lines[i][204:214] == "":
        pass
    else:
        density_list.append(float(lines[i][216:226]))
        altitude_list.append(round(float(lines[i][0:11].strip()),10))
        declination_list.append(float(lines[i][15:19]))

density_list = [round(item * 1000000, 4) for item in density_list]


fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')

ax.plot_trisurf(altitude_list, declination_list, density_list, cmap='viridis', edgecolor='none')
ax.set_title('MASTER 2022 population with size threshold between 0.01 m and 100 m')
ax.set_xticks([0, 500, 1000, 1500, 2000])
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90])
#ax.set_zticks([0e-6, 1e-6, 2e-6, 3e-6, 4e-6, 5e-6])
ax.set_xlabel("Altitude [km]")
ax.set_ylabel("Declination [°]")
ax.set_zlabel("Spatial density [10$^{-6}$/km$^3$]")

fig.savefig("MASTER_2022_altitude_declination.pdf", format = "pdf", dpi = 3000, bbox_inches = "tight")


plt.show()