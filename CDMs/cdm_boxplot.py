import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("train_data.csv")
#filter dataframe to only obtain values for tca at around 1 day
df = df[(df["time_to_tca"]>0.95) & (df["time_to_tca"]<1.05)]
#filter dataframe to only obtain radar cross section < 0.1 m^2
df = df[df["c_rcs_estimate"]<0.1]
#select the necessary columns
df = df[["c_sigma_t", "c_sigma_n", "c_sigma_r", "time_to_tca", "c_h_per", "c_rcs_estimate", "c_j2k_ecc", "c_j2k_inc"]]

df1 = df[df["c_h_per"] <= 350]
df1["perigee_altitude_class"] = "h$_{p1}$"
df2 = df[(df["c_h_per"] > 350) & (df["c_h_per"] <= 550)]
df2["perigee_altitude_class"] = "h$_{p2}$"
df3 = df[(df["c_h_per"] > 550) & (df["c_h_per"] <= 800)]
df3["perigee_altitude_class"] = "h$_{p3}$"
df4 = df[(df["c_h_per"] > 800) & (df["c_h_per"] <= 2000)]
df4["perigee_altitude_class"] = "h$_{p4}$"
df5 = df[(df["c_h_per"] > 2000) & (df["c_h_per"] <= 25000)]
df5["perigee_altitude_class"] = "h$_{p5}$"

df_complete = pd.concat([df1,df2,df3,df4,df5],ignore_index=True)

#my_dict = {'h$_{p1}$': df1["c_sigma_t"], 'h$_{p2}$': df2["c_sigma_t"], 'h$_{p3}$': df3["c_sigma_t"], 'h$_{p4}$': df4["c_sigma_t"]}

my_dict = {
            'h$_{p1,AT}$': df1["c_sigma_t"], 'h$_{p1,CT}$': df1["c_sigma_n"], 'h$_{p1,RA}$': df1["c_sigma_r"],
            'h$_{p2,AT}$': df2["c_sigma_t"], 'h$_{p2,CT}$': df2["c_sigma_n"], 'h$_{p2,RA}$': df2["c_sigma_r"],
            'h$_{p3,AT}$': df3["c_sigma_t"], 'h$_{p3,CT}$': df3["c_sigma_n"], 'h$_{p3,RA}$': df3["c_sigma_r"],
            'h$_{p4,AT}$': df4["c_sigma_t"], 'h$_{p4,CT}$': df4["c_sigma_n"], 'h$_{p4,RA}$': df4["c_sigma_r"]
            }


fig1, ax1 = plt.subplots()
bp = ax1.boxplot(my_dict.values(), showmeans=True)
# You can access boxplot items using ist dictionary

fig, ax = plt.subplots(figsize=(14, 5))
ax.boxplot(my_dict.values(), showmeans=True)

ax.set_xticklabels(my_dict.keys())
ax.set_yscale("log")

ax.grid(axis = "y")
ax.legend([bp['medians'][0], bp['means'][0]], ['median', 'mean'])



x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12]

"""y = [
    df1["c_sigma_t"].median(),
    df2["c_sigma_t"].median(), 
    df3["c_sigma_t"].median(), 
    df4["c_sigma_t"].median(), 
    df1["c_sigma_t"].mean(), 
    df2["c_sigma_t"].mean(), 
    df3["c_sigma_t"].mean(), 
    df4["c_sigma_t"].mean()
    ]"""

y = [
    df1["c_sigma_t"].median(), df1["c_sigma_n"].median(), df1["c_sigma_r"].median(),
    df2["c_sigma_t"].median(), df2["c_sigma_n"].median(), df2["c_sigma_r"].median(),
    df3["c_sigma_t"].median(), df3["c_sigma_n"].median(), df3["c_sigma_r"].median(),
    df4["c_sigma_t"].median(), df4["c_sigma_n"].median(), df4["c_sigma_r"].median(),
    df1["c_sigma_t"].mean(), df1["c_sigma_n"].mean(), df1["c_sigma_r"].mean(),
    df2["c_sigma_t"].mean(), df2["c_sigma_n"].mean(), df2["c_sigma_r"].mean(),
    df3["c_sigma_t"].mean(), df3["c_sigma_n"].mean(), df3["c_sigma_r"].mean(),
    df4["c_sigma_t"].mean(), df4["c_sigma_n"].mean(), df4["c_sigma_r"].mean()
    ]
y = list(map(int, list(np.around(np.array(y), 0))))

ax.scatter(x,y, color = "white")
for i, txt in enumerate(y):
    median_x = 0.3
    median_y = 0
    mean_x = 0.15
    mean_y= 0
    deviation_x = [median_x, median_x, median_x, median_x,median_x, median_x, median_x, median_x,median_x, median_x, median_x, median_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x, mean_x]
    deviation_y = [median_y, median_y, median_y, median_y,median_y, median_y, median_y, median_y,median_y, median_y, median_y, median_y, 1500, mean_y, mean_y, mean_y, mean_y, mean_y, mean_y, mean_y, mean_y, mean_y, 20, mean_y]
    ax.annotate(txt, (x[i]+deviation_x[i], y[i]+deviation_y[i]))

ax.set_xlabel("Perigee altitude class")
ax.set_ylabel("Uncertainty [m]")
ax.set_title("Uncertainty in along-, cross- and radial-direction across four perigee altitude classes")
ax.set_yticks([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
fig.savefig("boxplot_uncertainty.pdf", format = "pdf", dpi = 3000, bbox_inches = "tight")

plt.show()