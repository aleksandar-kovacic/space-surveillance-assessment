from traceback import print_tb
from matplotlib.colors import LogNorm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pkg_resources import load_entry_point
import seaborn as sns
from scipy.optimize import curve_fit
from configparser import ConfigParser
import matplotlib.gridspec as gridspec

#annual_collision_p      acpd        res_risk
annual_collision_probability = "annual_collision_p"
#   acp_binned      acp_total       acpd_binned     acpd_total      acp_binned_emr      acp_total_emr
which_file_binned = "acp_binned.csv"
which_file_total = "acp_total.csv"
#   error_list_acp     error_list_acpd     error_list_res_risk
which_error_list = "error_list_acp"

plt.rc('axes', axisbelow=True)

parameter_config = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
parameter_config.read("../ares_config.ini")

df = pd.read_csv("requirement_plots/" + which_file_binned)
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")

#d_repr: ACP_w
#d_repr = [0.015, 0.025, 0.035, 0.045, 0.055, 0.065, 0.075, 0.085, 0.095, 0.105, 0.115, 0.125, 0.135, 0.145, 0.155, 0.165, 0.175, 0.185, 0.195, 0.205, 0.215, 0.225, 0.235, 0.245, 0.255, 0.265, 0.275, 0.285, 0.295, 0.305, 0.315]

#d_repr: ACP_EMR
#d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319]

#d_repr: risk_red
d_repr = [0.025, 0.055, 0.085, 0.115, 0.145, 0.17, 0.205, 0.235, 0.265, 0.295, 0.325]

particle_size_max_list = [float(i) for i in parameter_config.getlist('parameters', 'particle_size_max')]
particle_size_min_list = [float(i) for i in parameter_config.getlist('parameters', 'particle_size_min')]

col_list = ["height", "mass", "depth", "diameter", "span", "width", "objectClass", "mass"]
df_mass = pd.read_excel("discos_database_re-entry_epoch_2016-11-01.xlsx", usecols = col_list)

df_mass.dropna(subset = ["mass"], inplace=True)
df_mass["d_repr"] = df_mass[["height", "depth", "width", "diameter", "span"]].max(axis=1)
df_mass.dropna(subset = ["d_repr"], inplace=True)

#If "discos_database_complete.xlsx" is read. Deletes unrealistic values
#df_mass = df[df["mass"] < 100000]
#df_mass = df[df["d_repr"] < 2500]

df_mass.reset_index(drop=True, inplace=True)

# Abhishek Bhatia's data & scatter plot.
# https://stackoverflow.com/questions/32536226/log-log-plot-linear-regression
input_X = df_mass["d_repr"].to_list()
input_X = np.array(input_X) #[:, np.newaxis]

output_Y = df_mass["mass"].to_list()
output_Y = np.array(output_Y) #[:, np.newaxis]

X = np.array(input_X)
y = np.array(output_Y)

def func(X, a, b):
    return a * np.power(X, b)

popt, pcov = curve_fit(func, X, y)

xaj = d_repr #np.logspace(-2, 2, 1000)
yaj = func(xaj, *popt)

#d_repr in [m]
d_repr_1 = np.array(d_repr)
#density in [kg/m^3]
roh = 2.8*((d_repr_1*100)**(-0.74)) * 1000
sphere_mass = (4/3)*roh*np.pi*(d_repr_1/2)**3
sphere_mass_list = sphere_mass.tolist()

debris_mass_list = []
for i in range(len(d_repr)):
    debris_mass_list.append(min(yaj[i], sphere_mass_list[i]))

size_bin = list(range(1,len(particle_size_max_list)+1))

N_list = []
for i in range(len(debris_mass_list)):
    M = 1150 #SENTINEL-3A mass
    v_rel = 10*1000
    m = debris_mass_list[i]
    L_c = 0.1
    span = 1
    
    if (m*(v_rel**2))/(2*M) < 40000:
        P = m * v_rel
    else:
        P = M + m

    N = 0.1*(P**0.75)*(L_c**(-1.71))
    N_list.append(N)

df_additional = {"particle_size_min":particle_size_min_list, "particle_size_max":particle_size_max_list, "size_bin":size_bin, "d_repr":d_repr, "debris_mass":debris_mass_list, "N": N_list}
df_additional = pd.DataFrame(data=df_additional)
df = pd.merge(df, df_additional)
df["annual_collision_p"].replace({"error": 0.0}, inplace=True)
df["effect"] = df["N"].astype(float)*df["annual_collision_p"].astype(float)


df = df.drop(columns = 'f_rem_risk')
df = df.drop(columns = 'f_res_risk')
df = df.drop(columns = 'f_risk_red')
df = df.drop(columns = 'false_alarm_rate')
df = df.drop(columns = 'rem_risk')
#df = df.drop(columns = 'res_risk')
#df = df.drop(columns = 'risk_red')

df["res_risk"].replace({"error": 0}, inplace=True)
df = df.astype({"res_risk": float})
df["risk_red"].replace({"error": 0}, inplace=True)
df = df.astype({"risk_red": float})
df["acpd"] = df["res_risk"].astype(float) + df["risk_red"].astype(float)
df["effect_acpd"] = df["N"].astype(float)*df["acpd"].astype(float)


df["acpl"].replace({"error": 0.0001}, inplace=True)
df['acpl'] = df['acpl'].astype("float")
df = df[df['acpl'] == 0.0001]
df.reset_index(drop=True, inplace=True)

h_list = df['sma'].unique().tolist()

#optical settings
d_ref_optical = 0.7/1000
h_ref_optical = 36000
exp_optical = -0.5

#values for Space Fence radar equation
lambda_radar_SF = 0.30/1000 #0.15
d_ref_radar_SF = 0.32/1000 #0.26 falls exactly on 2cm at 400km               #d_ref = 0.3, lambda = 0.3  #d_ref = 0.17, lambda = 0.3  #d_ref = 0.08, lambda = 0.13
h_ref_radar_SF = 2000
exp_radar_SF = 2.0
d_min_final_list_SF = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_SF*((h_list[i]/h_ref_radar_SF)**exp_radar_SF)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_SF**2)*((h_list[i]/h_ref_radar_SF)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_SF)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #convert d_min_final to m
    d_min_final = d_min_final * 1000
    
    d_min_final_list_SF.append(d_min_final)

df_fence_filter = {"d_min" : d_min_final_list_SF, "sma":h_list}
df_fence_filter = pd.DataFrame(data=df_fence_filter)

"""#Cut off the Size Bins which can be tracked and therefore avoided
df = pd.merge(df, df_fence_filter)
df = df[df['d_repr']<df['d_min']]
df.reset_index(drop=True, inplace=True)"""


#Implement Risk Matrix
#Likelihood
l_classes = [0.0001, 0.001, 0.01, 0.1]
#l_classes = [0.00001, 0.0001, 0.001, 0.01]
#l_classes = np.logspace(-5,-1,4).tolist()

conditions_likelihood = [
    df[annual_collision_probability].astype(float).lt(l_classes[0]),
    df[annual_collision_probability].astype(float).ge(l_classes[0]) & df[annual_collision_probability].astype(float).lt(l_classes[1]),
    df[annual_collision_probability].astype(float).ge(l_classes[1]) & df[annual_collision_probability].astype(float).lt(l_classes[2]),
    df[annual_collision_probability].astype(float).ge(l_classes[2]) & df[annual_collision_probability].astype(float).lt(l_classes[3]),
    df[annual_collision_probability].astype(float).ge(l_classes[3])
]
choices_likelihood = [1, 2, 3, 4, 5]
df['likelihood'] = np.select(conditions_likelihood, choices_likelihood)

#Consequence
#c_classes = [250, 500, 750, 1000]
c_classes = [1, 10, 100, 1000]
#c_classes = np.logspace(1,3,5).tolist()

conditions_consequence = [
    df['N'].astype(float).lt(c_classes[0]),
    df['N'].astype(float).ge(c_classes[0]) & df['N'].astype(float).lt(c_classes[1]),
    df['N'].astype(float).ge(c_classes[1]) & df['N'].astype(float).lt(c_classes[2]),
    df['N'].astype(float).ge(c_classes[2]) & df['N'].astype(float).lt(c_classes[3]),
    df['N'].astype(float).ge(c_classes[3]) 
]
choices_consequence = [1, 2, 3, 4, 5]
df['consequence'] = np.select(conditions_consequence, choices_consequence)

#Effect
df["risk"] = df['likelihood'] * df['consequence']

df111 = df[["likelihood","consequence", "risk", "sma", "d_repr", "res_risk"]]
print(df111.to_string())
print(l_classes)
#normalize the effect to a interval between 0 and 1
#df["effect"] = df["effect"]/df["effect"].max()

#==========================================================================================================================================================#

df["d_repr"]=np.around(df["d_repr"]*100, 2)
df = df.astype({"annual_collision_p": float})
#Heatmap
df_plot = df.pivot("d_repr", "sma", "risk")
fig, (ax1, ax) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 9]}, figsize = (6,5)) #figsize = (9,8)
#ax = fig.add_subplot(212)
#ax = sns.heatmap(df_plot, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
#ax = sns.heatmap(df_plot, cmap="YlGnBu", cbar_kws={'label': "Likelihood " + "(" + r"$ACP_{EMR}$" + ") ", "orientation": "horizontal"}, ax=ax)
#ax = sns.heatmap(df_plot, cmap="YlGnBu", cbar_kws={'label': "Risk = Likelihood " + "(" + r"$ACP_{d}$" + ") " + r'$ \cdot $' + " Consequence", "orientation": "horizontal"}, ax=ax)
ax = sns.heatmap(df_plot, cmap="YlGnBu", vmax = 12 , cbar_kws={'label': "Risk = Likelihood " + "(" + "Residual Risk" + ") " + r'$ \cdot $' + " Consequence", "orientation": "horizontal"}, ax=ax)
#, vmax = 10               norm = LogNorm()
#ax = sns.heatmap(df, fmt = ".0f", cbar_kws={'label': "Risk"}, ax=ax)
#ax.set_yticklabels(ax.get_yticks()+1, rotation = 0)
#ax.set_title("Likelihood for SENTINEL-3A type mission at i = 90° and population epoch 2036")
ax.set_title("Sustainability score for SENTINEL-3A type"+ "\n" +"mission at i = 90° and population epoch 2036")
ax.set_ylabel("Reference diameter "+ r"$d_{repr}$" +" [cm]")
ax.set_xlabel("Altitude [km]")
#ax.set_xticks(size_bin)
ax.invert_yaxis()
#fig.savefig("sustainability_rating_plots/Heat_Map_Cut_Off.pdf", format="pdf", bbox_inches="tight")
#fig.savefig("sustainability_rating_plots/Heat_Map_Full.pdf", format="pdf", bbox_inches="tight")

df_size_bin_2 = pd.read_csv("requirement_plots/"+which_file_binned)

#Because some xticks of the sma are lost due to the size threshold of the SSN, they should also not appear in the error plot.
sma_unique_list_1 = df['sma'].unique().tolist()
df_size_bin_2['sma'] = df_size_bin_2['sma'] - 6378.137
df_size_bin_2['sma'] = df_size_bin_2['sma'].round(0).astype("int")
sma_unique_list_2 = df_size_bin_2['sma'].unique().tolist()
new_list = list(set(sma_unique_list_2).difference(sma_unique_list_1))
for i in range(len(new_list)):
    df_size_bin_2 = df_size_bin_2[df_size_bin_2['sma'] != new_list[i]]

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
res_risk_sum = []
sma_list = df_size_bin_2['sma'].unique().tolist()
for i in range(len(sma_list)):
    df_new = df[df['sma'].isin([sma_list[i]]) & df["size_bin"].isin(size_bin)]
    acp_sum.append(df_new["annual_collision_p"].sum())
    acpd_sum.append(df_new["acpd"].sum())
    res_risk_sum.append(df_new["res_risk"].sum())
acp_sum = np.array(acp_sum)
acpd_sum = np.array(acpd_sum)
res_risk_sum = np.array(res_risk_sum)
#print("ACP Sum: " + str(acp_sum) + "\n")
#print("ACP_d Sum: " + str(acpd_sum) + "\n")

df_total = pd.read_csv("requirement_plots/"+which_file_total)

#Because some xticks of the sma are lost due to the size threshold of the SSN, they should also not appear in the error plot.
df_total['sma'] = df_total['sma'] - 6378.137
df_total['sma'] = df_total['sma'].round(0).astype("int")
sma_unique_list_2 = df_total['sma'].unique().tolist()
new_list = list(set(sma_unique_list_2).difference(sma_unique_list_1))
for i in range(len(new_list)):
    df_total = df_total[df_total['sma'] != new_list[i]]

df_total = df_total.astype({"annual_collision_p": float})
df_total = df_total.astype({"risk_red": float})
df_total = df_total.astype({"res_risk": float})
df_total["acpd"] = df_total["risk_red"] + df_total["res_risk"]
df_total = df_total.astype({"acpd": float})
df_total_list_acp = np.array(df_total["annual_collision_p"].to_list())
df_total_list_acpd = np.array(df_total["acpd"].to_list())
df_total_list_res_risk = np.array(df_total["res_risk"].to_list())
#print("ACP Total: " + str(df_total_list_acp) + "\n")
#print("ACP_d Total: " + str(df_total_list_acpd) + "\n")

if which_error_list == "error_list_acp":
    error_list = []
    for l in range(len(df_total_list_acp)):
        error_acp = (1-(df_total_list_acp[l]/acp_sum[l]))*100
        if error_acp < 0:
            error_acp = (1-(acp_sum[l]/df_total_list_acp[l]))*100
        else:
            error_acp = (1-(df_total_list_acp[l]/acp_sum[l]))*100
        error_list.append(error_acp)

elif which_error_list == "error_list_acpd":
    error_list = []
    for l in range(len(df_total_list_acpd)):
        error_acpd = (1-(df_total_list_acpd[l]/acpd_sum[l]))*100
        if error_acpd < 0:
            error_acpd = (1-(acpd_sum[l]/df_total_list_acpd[l]))*100
        else:
            error_acpd = (1-(df_total_list_acpd[l]/acpd_sum[l]))*100
        error_list.append(error_acpd)

elif which_error_list == "error_list_res_risk":
    error_list = []
    for l in range(len(df_total_list_res_risk)):
        error_res_risk = (1-(df_total_list_res_risk[l]/res_risk_sum[l]))*100
        if error_res_risk < 0:
            error_res_risk = (1-(res_risk_sum[l]/df_total_list_res_risk[l]))*100
        else:
            error_res_risk = (1-(df_total_list_res_risk[l]/res_risk_sum[l]))*100
        error_list.append(error_res_risk)

#print("ACP Error: " + str(np.array(error_list_acp)) + "\n")
#print("ACP_d Error: " + str(np.array(error_list_acpd)) + "\n")

sma_list = np.array(sma_list)
#plt.rcParams["figure.figsize"] = (17,4)
#ax1 = fig.add_subplot(211)
ax1.bar(sma_list, error_list, width = 20)
ax1.set_xlabel("Altitude [km]")
ax1.set_ylabel("Error [%]")
ax1.set_xticks(sma_list)
#ax1.set_yticks([0, 5 ,10, 15])
ax1.grid(which = "both")
fig.tight_layout()
#fig.savefig("requirement_plots/acpd_cov_2.pdf", dpi = 2500, bbox_inches = "tight")
plt.show()

"""df["d_repr"]=np.around(df["d_repr"]*100, 2)
df = df.astype({"annual_collision_p": float})

#Heatmap
df_plot = df.pivot("d_repr", "sma", "annual_collision_p")
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
#ax = sns.heatmap(df_plot, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df_plot, cmap="YlGnBu",norm = LogNorm(), cbar_kws={'label': "Likelihood " + "(" + r"$ACP_{EMR}$" + ")", "orientation": "horizontal"}, ax=ax)
#ax = sns.heatmap(df_plot, cmap="YlGnBu", vmax = 0.00037, cbar_kws={'label': "Risk = Likelihood " + "(" + r"$ACP_{EMR}$" + ") " + r'$ \cdot $' + " Consequence", "orientation": "horizontal"}, ax=ax)
#, vmax = 12   , vmax = 0.00037
#ax = sns.heatmap(df, fmt = ".0f", cbar_kws={'label': "Risk"}, ax=ax)
#ax.set_yticklabels(ax.get_yticks()+1, rotation = 0)
ax.set_title("Likelihood for SENTINEL-3A type mission at i = 90° and population epoch 2036" +"\n"+ r"$D_{ref}$" + " = "+str(d_ref_radar_SF*1000)+" m, " + "$\u03BB$"+ " = "+str(lambda_radar_SF*1000)+" m")
#ax.set_title("Sustainability score for SENTINEL-3A type mission at i = 90° and population epoch 2036" +"\n"+ r"$D_{ref}$" + " = "+str(d_ref_radar_SF*1000)+" m, " + "$\u03BB$"+ " = "+str(lambda_radar_SF*1000)+" m")
ax.set_ylabel("Reference diameter "+ r"$d_{repr}$" +" [cm]")
ax.set_xlabel("Altitude [km]")
#ax.set_xticks(size_bin)
ax.invert_yaxis()
#fig.savefig("requirement_plots/emr_i=90°_1.pdf", dpi = 2500, bbox_inches = "tight", format = "pdf")

plt.show()"""

#==========================================================================================================================================================#

"""font = {'size'   : 12}
plt.rc('font', **font)

#2D charts
df_sma_filter = df[df['sma'] == 800]
df_sma_filter.reset_index(drop=True, inplace=True)
df_sma_filter = df_sma_filter.astype({"size_bin": int, "annual_collision_p": float, "effect": float})
#print(df_sma_filter.to_string())
fig = plt.figure()"""

"""ax = fig.add_subplot(111) #121
x = df_sma_filter["size_bin"].to_list()
#y = df_sma_filter["annual_collision_p"].to_list()
y = df_sma_filter["annual_collision_p"]
df_sma_filter = df_sma_filter.drop(columns = ['res_risk', "risk_red", "scaling_factor", "acpd", "effect_acpd", "debris_mass", "man_rate"])
print(df_sma_filter)
ax.bar(x,y, width=0.7, label = "h = 800km" + "\n" + "i = 90°")
ax.set_ylabel(r'$ACP_w$')
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,len(particle_size_max_list)+1,2))
ax.set_title("Likelihood")
ax.grid(axis = "y")
file_name = "Likelihood"
"""

"""ax = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["N"].to_list()
ax.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 90°")
ax.set_ylabel("Number of fragments created by a collision")
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,len(particle_size_max_list)+1, 2))
ax.set_title("Consequence")
plt.yscale("log")
file_name = "Consequence"
"""


"""
ax = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["consequence"].to_list()
ax.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 90°")
ax.set_ylabel("Consequence score")
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,len(particle_size_max_list)+1, 2))
ax.set_title("Consequence")
file_name = "Consequence_Score"
"""

"""
ax = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["likelihood"].to_list()
ax.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 90°")
ax.set_ylabel("Likelihood score")
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,len(particle_size_max_list)+1, 2))
ax.set_yticks([1,2,3,4,5])
ax.set_title("Likelihood")
file_name = "Likelihood_Score"
"""

"""ax = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["risk"].to_list()
ax.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 90°")
ax.set_ylabel("Risk")
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,len(particle_size_max_list)+1, 2))
ax.set_title("Risk = Likelihood score " + r'$ \cdot $' + " Consequence score") #\cdot
file_name = "Risk_Score_new"


fig.tight_layout()
#fig.set_size_inches(7, 5)
ax.legend()
fig.savefig("sustainability_rating_plots/" + str(file_name) + ".pdf", format="pdf", bbox_inches="tight")
plt.show()"""


#==========================================================================================================================================================#

"""#3d Bar Chart
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

df = df.astype({"size_bin": int, "annual_collision_p": float, "effect": float})
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x3 = df["size_bin"].to_list()
y3 = df["sma"].to_list()
z3 = df["effect"].to_list()

dx = 1
dy = 1
dz = 1

ax1.bar3d(x3, y3, z3, dx, dy, dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()"""
    
