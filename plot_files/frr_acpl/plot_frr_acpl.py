from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np
import seaborn as sns
from intersect import intersection

#Plot Manoeuvre Rate at Fractional Risk Reduction = 0.9
acpl_steps = 10
#df = pd.read_csv("total_output.csv")
df=pd.read_csv("frr_acpl_oldSSN_2016.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df['inc'] = df['inc'].round(0).astype("int")

start = 0
end = acpl_steps
i=0

f_risk_red_list = []
inc_list = []
acpl_list = []
sma_list = []

#print(df.to_string())

while i < int(len(df)/acpl_steps):
    df_new = df[start:end]

    x1=np.array(df_new["acpl"].to_list())
    y1=np.array(df_new["f_risk_red"].to_list())
    x2=np.array([-5,2000])
    y2=np.array([0.9, 0.9])
    
    x, y = intersection(x1, y1, x2, y2)
    acpl_list.append(x[0])
    f_risk_red_list.append(y[0])
    
    sma_list.append(df_new.at[start, "sma"])
    inc_list.append(df_new.at[start, "inc"])

    start = start + acpl_steps
    end = end + acpl_steps
    i=i+1

df_total_output = pd.DataFrame(
        data = {"f_risk_red": f_risk_red_list, "acpl": acpl_list, "sma": sma_list, "inc": inc_list}
    )
print(df_total_output)


df_total_output = df_total_output.pivot("inc", "sma", "acpl")
ax = plt.axes()
#ax = sns.heatmap(df_total_output, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df_total_output, cbar_kws={'label': 'ACPL at fractional risk reduction 90%'})
ax.set_title("ACPL of SWARM B type mission with" + "\n" + "old SSN for the epoch 2016")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()

plt.savefig("frr_acpl_oldSSN_2016.pdf", dpi = 1500, bbox_inches = "tight")

plt.show()

#print(df[ (df["inc"] == 15) & (df["sma"] == 300) ])