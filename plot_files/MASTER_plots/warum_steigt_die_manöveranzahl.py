import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

R = 6378.137

with open('warum_steigt_die_manöveranzahl.txt', "r") as f:
    lines = f.readlines()

flux_list_2022 = []
sma_list = []
inc_list = []

for i in range(2,len(lines)):
    flux_list_2022.append(float(lines[i][216:226]))
    sma_list.append(round(float(lines[i][0:12].strip()),0))
    inc_list.append(float(lines[i][12:22].strip()))



df_total_output = pd.DataFrame(data = {"flux": flux_list_2022, "sma": sma_list, "inc": inc_list})

print(df_total_output)

plt.bar(df_total_output["inc"], df_total_output["flux"])

"""#sns.set(rc = {'figure.figsize':(9,7)})
df_total_output = df_total_output.pivot("ecc", "hp", "flux")
ax = plt.axes()
#ax = sns.heatmap(df_total_output, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df_total_output, cbar_kws={'label': 'Flux'})
#annot=True,fmt = ".0f"
ax.set_title("Eccentricity vs. Semi-major axis")
ax.set_ylabel("Eccentricity")
ax.set_xlabel("Semi-major axis [km]")
ax.invert_yaxis()"""
#plt.savefig("SENTINEL3A_newSSN_2022.pdf" ,dpi = 1500, bbox_inches = "tight")



plt.show()