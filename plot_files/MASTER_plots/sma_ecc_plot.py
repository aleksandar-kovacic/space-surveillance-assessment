import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

R = 6378.137

with open('MASTER_output_2036_sma_ecc.txt', "r") as f:
    lines = f.readlines()

flux_list_2036 = []
sma_list = []
ecc_list = []

for i in range(2,len(lines)):
    if lines[i][204:214] == "":
        pass
    else:
        flux_list_2036.append(float(lines[i][216:226]))
        sma_list.append(round(float(lines[i][0:12].strip()),0))
        ecc_list.append(float(lines[i][12:22]))



df_total_output = pd.DataFrame(data = {"flux": flux_list_2036, "sma": sma_list, "ecc": ecc_list})

df_total_output["hp"] = df_total_output["sma"] * (1-df_total_output["ecc"]) - R

df_total_output["hp"]=df_total_output["hp"].round(0).astype(int)
df_total_output = df_total_output.drop(df_total_output.index[df_total_output['hp'] < 0])
df_total_output = df_total_output.drop(df_total_output.index[df_total_output['flux'] == 0])
df_total_output = df_total_output.reset_index(drop=True)
print(df_total_output)

plt.bar(df_total_output["hp"], df_total_output["flux"])

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