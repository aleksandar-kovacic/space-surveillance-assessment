import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from intersect import intersection

df = pd.read_csv("AEOLUS_oldSSN_2022.csv")
df1 = pd.read_csv("AEOLUS_newSSN_2022.csv")
df2 = pd.read_csv("AEOLUS_oldSSN_pop_2022.csv")
df3 = pd.read_csv("AEOLUS_newSSN_pop_2022.csv")
satellite_name = "AEOLUS"
ACPL = 0.00005
correction = -0.00016
correction_y = 0.012

fig = plt.figure(figsize=(11,9.5))

ax = fig.add_subplot(221)

ax_man = ax.twinx()
ax_man.plot(df["acpl"], df["man_rate"], label = "Manoeuvre rate", color = "black")
ax_man.set_ylabel("Manoeuvre rate")

ax.plot(df["acpl"], df["f_rem_risk"], label = "Fractional remaining risk")
ax.plot(df["acpl"], df["f_res_risk"], label = "Fractional residual risk")
ax.plot(df["acpl"], df["f_risk_red"], label = "Fractional risk reduction")
ax.set_xscale("log")
ax.set_xticks(np.logspace(-6, -1, 6))
ax.set_yticks(np.linspace(0, 1, 11))
ax.grid(which = "both")
ax.set_xlabel("Accepted collision probability level")
ax.set_ylabel("Fractional risk")
ax.set_title("Old SSN")
ax.axvline(x = ACPL, color = "red")

ax_line_x = np.array([ACPL, ACPL])
ax_line_y = np.array([0, 1])
ax_x, ax_y = intersection(df["acpl"], df["f_rem_risk"], ax_line_x, ax_line_y)
ax.axhline(y = ax_y[0]+correction_y, color = "red")
ax.plot(ax_x[0], ax_y[0]+correction_y, marker='o', markersize=3, color="black")

#=========================================================================================================#

ax1 = fig.add_subplot(222)

ax1_man = ax1.twinx()
ax1_man.plot(df1["acpl"], df1["man_rate"], label = "Manoeuvre rate", color = "black")
ax1_man.set_ylabel("Manoeuvre rate")

ax1.plot(df1["acpl"], df1["f_rem_risk"], label = "Fractional remaining risk")
ax1.plot(df1["acpl"], df1["f_res_risk"], label = "Fractional residual risk")
ax1.plot(df1["acpl"], df1["f_risk_red"], label = "Fractional risk reduction")
ax1.set_xscale("log")
ax1.set_xticks(np.logspace(-6, -1, 6))
ax1.set_yticks(np.linspace(0, 1, 11))
ax1.grid(which = "both")
ax1.set_xlabel("Accepted collision probability level")
ax1.set_ylabel("Fractional risk")
ax1.set_title("New SSN")
ax1.axhline(y = ax_y[0]+correction_y, color = "red")

ax1_line_x = np.array([1e-9, 1e-1])
ax1_line_y = np.array([ax_y[0]+correction_y, ax_y[0]+correction_y])
ax1_x, ax1_y = intersection(df1["acpl"], df1["f_rem_risk"], ax1_line_x, ax1_line_y)
ax1.axvline(x = ax1_x[0]+correction, color = "red")
ax1.plot(ax1_x[0]+correction, ax1_y[0], marker='o', markersize=3, color="black")

#=========================================================================================================#
ax2 = fig.add_subplot(223)

ax2_man = ax2.twinx()
ax2_man.plot(df2["acpl"], df2["man_rate"], label = "Manoeuvre rate", color = "black")
ax2_man.set_ylabel("Manoeuvre rate")

ax2.plot(df2["acpl"], df2["f_rem_risk"], label = "Fractional remaining risk")
ax2.plot(df2["acpl"], df2["f_res_risk"], label = "Fractional residual risk")
ax2.plot(df2["acpl"], df2["f_risk_red"], label = "Fractional risk reduction")
ax2.set_xscale("log")
ax2.set_xticks(np.logspace(-6, -1, 6))
ax2.set_yticks(np.linspace(0, 1, 11))
ax2.grid(which = "both")
ax2.set_xlabel("Accepted collision probability level")
ax2.set_ylabel("Fractional risk")
ax2.set_title("Old SSN with population size threshold > 1.43 cm")


#=========================================================================================================#


ax3 = fig.add_subplot(224)

ax3_man = ax3.twinx()
ax3_man.plot(df3["acpl"], df3["man_rate"], label = "Manoeuvre rate", color = "black")
ax3_man.set_ylabel("Manoeuvre rate")

ax3.plot(df3["acpl"], df3["f_rem_risk"], label = "Fractional remaining risk")
ax3.plot(df3["acpl"], df3["f_res_risk"], label = "Fractional residual risk")
ax3.plot(df3["acpl"], df3["f_risk_red"], label = "Fractional risk reduction")
ax3.set_xscale("log")
ax3.set_xticks(np.logspace(-6, -1, 6))
ax3.set_yticks(np.linspace(0, 1, 11))
ax3.grid(which = "both")
ax3.set_xlabel("Accepted collision probability level")
ax3.set_ylabel("Fractional risk")
ax3.set_title("New SSN with population size threshold > 1.43 cm")


handles, labels = [(a + b) for a, b in zip(ax.get_legend_handles_labels(), ax_man.get_legend_handles_labels())]
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.93),fancybox=True, ncol=5)
fig.suptitle("AEOLUS\nEpoch: 2022")
fig.tight_layout(pad = 3)
fig.savefig("AEOLUS_rem_risk_analysis.pdf", dpi = 3000, bbox_inches = "tight")
plt.show()