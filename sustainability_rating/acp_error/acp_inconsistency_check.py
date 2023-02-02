import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)

"""df = pd.read_csv("plot_files/total_output_acp_single.csv")
df["annual_collision_p"].replace({"error": 0.0}, inplace=True)
df = df.astype({"annual_collision_p": float})
print("Binned ACP: " + str(df["annual_collision_p"].sum()))

df1 = pd.read_csv("plot_files/total_output_acp_total.csv")
df1["annual_collision_p"].replace({"error": 0.0}, inplace=True)
df1 = df1.astype({"annual_collision_p": float})
print("Total ACP: " + str(df1["annual_collision_p"].sum()))

print("Ratio: " + str(1-(df1["annual_collision_p"].sum())/df["annual_collision_p"].sum()))"""

#df_size_bin_2 = pd.read_csv("error_bin_single_future.csv")
df_size_bin_2 = pd.read_csv("../requirement_plots/acp_binned_emr.csv")
size_bin_number = len(df_size_bin_2['particle_size_min'].unique().tolist())
size_bin = list(range(1,size_bin_number+1))
particle_size_min_list = df_size_bin_2['particle_size_min'].unique().tolist()
df_additional = {"particle_size_min":particle_size_min_list, "size_bin":size_bin}
df_additional = pd.DataFrame(data=df_additional)
df = pd.merge(df_size_bin_2, df_additional)

df["annual_collision_p"].replace({"error": 0.0}, inplace=True)
df = df.astype({"annual_collision_p": float})

df["risk_red"].replace({"error": 0.0}, inplace=True)
df = df.astype({"risk_red": float})

df["res_risk"].replace({"error": 0.0}, inplace=True)
df = df.astype({"res_risk": float})

df["acpd"] = df["risk_red"] + df["res_risk"]



acp_sum = []
acpd_sum = []
sma_list = df_size_bin_2['sma'].unique().tolist()
for i in range(len(sma_list)):
    df_new = df[df['sma'].isin([sma_list[i]]) & df["size_bin"].isin(size_bin)]
    acp_sum.append(df_new["annual_collision_p"].sum())
    acpd_sum.append(df_new["acpd"].sum())
acp_sum = np.array(acp_sum)
acpd_sum = np.array(acpd_sum)
print("ACP Sum: " + str(acp_sum) + "\n")
print("ACP_d Sum: " + str(acpd_sum) + "\n")

df_total = pd.read_csv("../requirement_plots/acp_total_emr.csv")
df_total = df_total.astype({"annual_collision_p": float})
df_total = df_total.astype({"risk_red": float})
df_total = df_total.astype({"res_risk": float})
df_total["acpd"] = df_total["risk_red"] + df_total["res_risk"]
df_total = df_total.astype({"acpd": float})
df_total_list_acp = np.array(df_total["annual_collision_p"].to_list())
df_total_list_acpd = np.array(df_total["acpd"].to_list())
print("ACP Total: " + str(df_total_list_acp) + "\n")
print("ACP_d Total: " + str(df_total_list_acpd) + "\n")


error_list_acp = []
for l in range(len(df_total_list_acp)):
    error_acp = (1-(df_total_list_acp[l]/acp_sum[l]))*100
    if error_acp < 0:
        error_acp = (1-(acp_sum[l]/df_total_list_acp[l]))*100
    else:
        error_acp = (1-(df_total_list_acp[l]/acp_sum[l]))*100
    error_list_acp.append(error_acp)

error_list_acpd = []
for l in range(len(df_total_list_acpd)):
    error_acpd = (1-(df_total_list_acpd[l]/acpd_sum[l]))*100
    if error_acpd < 0:
        error_acpd = (1-(acpd_sum[l]/df_total_list_acpd[l]))*100
    else:
        error_acpd = (1-(df_total_list_acpd[l]/acpd_sum[l]))*100
    error_list_acpd.append(error_acpd)

print("ACP Error: " + str(np.array(error_list_acp)) + "\n")
print("ACP_d Error: " + str(np.array(error_list_acpd)) + "\n")

print("SMA: " + str(np.array(sma_list)-6378.137))

sma_list = np.array(sma_list) - 6378.137
plt.rcParams["figure.figsize"] = (17,4)
fig = plt.figure()
ax = fig.add_subplot(211)
ax.bar(sma_list, error_list_acp, width = 20)
ax.set_xlabel("Size Bin")
ax.set_ylabel("Error [%]")
ax.set_xticks(sma_list)
ax.grid(which = "both")
#plt.savefig("error_bin_single_future.pdf", format="pdf", bbox_inches="tight")
ax1 = fig.add_subplot(212)
ax1.bar(sma_list, error_list_acpd, width = 20)
ax1.set_xlabel("Size Bin")
ax1.set_ylabel("Error [%]")
ax1.set_xticks(sma_list)
ax1.grid(which = "both")
plt.show()
