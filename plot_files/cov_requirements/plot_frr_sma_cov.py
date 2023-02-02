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
df=pd.read_csv("cov_middle.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")

start = 0
end = acpl_steps
i=0

f_risk_red_list = []
man_rate_list = []
sma_list = []
sf_list = []

#print(df.to_string())

while i < int(len(df)/acpl_steps):
    df_new = df[start:end]

    x1=np.array(df_new["f_risk_red"].to_list())
    y1=np.array(df_new["man_rate"].to_list())
    x2=np.array([0.9, 0.9])
    y2=np.array([-5, 2000])
    
    x, y = intersection(x1, y1, x2, y2)
    f_risk_red_list.append(x[0])
    man_rate_list.append(y[0])
    
    sma_list.append(df_new.at[start, "sma"])
    sf_list.append(df_new.at[start, "scaling_factor"])

    start = start + acpl_steps
    end = end + acpl_steps
    i=i+1

df_total_output = pd.DataFrame(
        data = {"f_risk_red": f_risk_red_list, "man_rate": man_rate_list, "sma": sma_list, "scaling_factor": sf_list}
    )
print(df_total_output)

sns.set(rc = {'figure.figsize':(6.8,5.7)})
df_total_output = df_total_output.pivot("scaling_factor", "sma", "man_rate")
ax = plt.axes()
#ax = sns.heatmap(df_total_output, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df_total_output, annot=True, fmt = ".0f", cbar_kws={'label': 'Manoeuvre rate at fractional risk reduction = 90%'})
ax.set_title("0.1 m$^2$ ≤ s ≤ 1 m$^2$"+"\n"+"Sentinel-3A type mission with new SSN for the epoch 2022")
ax.set_ylabel("Scaling factor")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("cov_middle.pdf" ,dpi = 2500, bbox_inches = "tight", format = "pdf")

plt.show()