import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""df = pd.read_csv("oldSSN.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df["inc"] = df["inc"].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(9,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001'})
ax.set_title("Manoeuvre rate of SWARM B type mission with" + "\n" + "old SSN for the reference epoch 2016")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("oldSSN.pdf", dpi=1000, bbox_inches="tight")"""




"""df = pd.read_csv("newSSN.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df["inc"] = df["inc"].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(9,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001'})
ax.set_title("Manoeuvre rate of SWARM B type mission with" + "\n" + "new SSN for the reference epoch 2016")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("newSSN.pdf", dpi=1000, bbox_inches="tight")"""


df = pd.read_csv("SENTINEL3A_wc_newSSN_2036.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df["inc"] = df["inc"].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(9,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001'})
ax.set_title("Manoeuvre rate of Sentinel-3A type mission with" + "\n" + "new SSN for the epoch 2036")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("SENTINEL3A_wc_newSSN_2036.pdf", dpi=1000, bbox_inches="tight")
plt.show()


"""df = pd.read_csv("oldSSN_2022.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df["inc"] = df["inc"].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(9,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001'})
ax.set_title("Manoeuvre rate of SWARM B type mission with" + "\n" + "old SSN for the epoch 2022")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("oldSSN_2022.pdf", dpi=1000, bbox_inches="tight")"""

"""df = pd.read_csv("newSSN_2022.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df["inc"] = df["inc"].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(9,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre rate at ACPL = 0.0001'})
ax.set_title("Manoeuvre rate of SWARM B type mission with" + "\n" + "new SSN for the epoch 2022")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.savefig("newSSN_2022.pdf", dpi=1000, bbox_inches="tight")

plt.show()"""