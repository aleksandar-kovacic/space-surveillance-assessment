import pandas as pd
import matplotlib.pyplot as plt
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


parameter_list = ["c_sigma_t", "c_sigma_n", "c_sigma_r", "c_sigma_t", "c_sigma_n", "c_sigma_r", "c_sigma_t", "c_sigma_n", "c_sigma_r", "c_sigma_t", "c_sigma_n", "c_sigma_r"]
df_list = [df1, df1, df1, df2, df2, df2, df3, df3, df3, df4, df4, df4]
perigee_list =['h$_{p1,AT}$', 'h$_{p1,CT}$', 'h$_{p1,RA}$', 'h$_{p2,AT}$', 'h$_{p2,CT}$', 'h$_{p2,RA}$', 'h$_{p3,AT}$', 'h$_{p3,CT}$', 'h$_{p3,RA}$', 'h$_{p4,AT}$', 'h$_{p4,CT}$', 'h$_{p4,RA}$']
my_dict = {
            'h$_{p1,AT}$': df1["c_sigma_t"], 'h$_{p1,CT}$': df1["c_sigma_n"], 'h$_{p1,RA}$': df1["c_sigma_r"],
            'h$_{p2,AT}$': df2["c_sigma_t"], 'h$_{p2,CT}$': df2["c_sigma_n"], 'h$_{p2,RA}$': df2["c_sigma_r"],
            'h$_{p3,AT}$': df3["c_sigma_t"], 'h$_{p3,CT}$': df3["c_sigma_n"], 'h$_{p3,RA}$': df3["c_sigma_r"],
            'h$_{p4,AT}$': df4["c_sigma_t"], 'h$_{p4,CT}$': df4["c_sigma_n"], 'h$_{p4,RA}$': df4["c_sigma_r"]
            }

plt.rcParams["figure.figsize"] = (16,5)
plt.rc('axes', axisbelow=True)

#========================================================================================#
fig_dump, ax_dump = plt.subplots()
for i in range(len(my_dict)):
    scatter = ax_dump.scatter([list(my_dict.keys())[i]]*len(list(my_dict[perigee_list[i]])), list(my_dict[perigee_list[i]]), c = df_list[i]["c_j2k_ecc"])

fig_dump1, ax_dump1 = plt.subplots()
for i in range(len(my_dict)):
    scatter1 = ax_dump1.scatter([list(my_dict.keys())[i]]*len(list(my_dict[perigee_list[i]])), list(my_dict[perigee_list[i]]), c = df_list[i]["c_j2k_inc"])
#========================================================================================#

#fig, ax = plt.subplots(figsize = (7,4.5))
fig = plt.figure()
ax = fig.add_subplot(121)

size_of_marker = 20

for i in range(len(my_dict)):
    ax.scatter([list(my_dict.keys())[i]]*len(list(my_dict[perigee_list[i]])), list(my_dict[perigee_list[i]]), c = df_list[i]["c_j2k_ecc"], s=size_of_marker)

ax.set_yscale("log")
ax.set_xlabel("Perigee altitude class")
ax.set_ylabel("Uncertainty [m]")
ax.set_yticks([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
ax.grid(axis = "y")
ax.set_title("(a): Eccentricity colouring")

# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(), title="Eccentricity", loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5)
ax.add_artist(legend1)


#plt.subplots_adjust(bottom=0.3)




#fig1, ax1 = plt.subplots(figsize = (7,4.5))
ax1 = fig.add_subplot(122)

for i in range(len(my_dict)):
    ax1.scatter([list(my_dict.keys())[i]]*len(list(my_dict[perigee_list[i]])), list(my_dict[perigee_list[i]]), c = df_list[i]["c_j2k_inc"], s = size_of_marker)

ax1.set_yscale("log")
ax1.set_xlabel("Perigee altitude class")
ax1.set_ylabel("Uncertainty [m]")
ax1.set_yticks([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
ax1.grid(axis = "y")
ax1.set_title("(b): Inclination colouring")

# Shrink current axis's height by 10% on the bottom
box1 = ax1.get_position()
ax1.set_position([box1.x0, box1.y0 + box1.height * 0.1, box1.width, box1.height * 0.9])

# produce a legend with the unique colors from the scatter
legend2 = ax1.legend(*scatter1.legend_elements(), title="Inclination [°]", loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5)
ax1.add_artist(legend2)

#fig.tight_layout()
fig.suptitle("Uncertainty in along-, cross- and radial direction across four perigee altitude classes")
plt.subplots_adjust(bottom=0.3)

fig.savefig("uncertainty_inc_ecc.pdf", format = "pdf", dpi = 3000, bbox_inches = "tight")

plt.show()