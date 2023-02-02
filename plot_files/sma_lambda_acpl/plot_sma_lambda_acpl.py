import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("SENTINEL3A_newSSN_2022.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(6,4)})
df_new = df_new.pivot("radar_wavelength", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new, annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001 and i = 90°'})
ax.set_title("Manoeuvre rate of SWARM B type mission with radar" + "\n" + "wavelength variation for the new Space Fence and epoch 2022")
ax.set_ylabel("Radar wavelength [m]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("SENTINEL3A_newSSN_2022.pdf", dpi=1000, bbox_inches="tight")

plt.show()