import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

df = pd.read_csv("bin_single_future.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
#df = df.loc[df['acpl'] == 0.0001]

d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
#d_repr = [0.01102, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
#d_repr = [0.01389, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
#d_repr = [0.016195, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
particle_size_min_list = [0.01, 0.01122, 0.01413, 0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509]
particle_size_max_list = [0.01122, 0.01413, 0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509, 100]
#particle_size_min_list = [0.01, 0.01413, 0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509]
#particle_size_max_list = [0.01413, 0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509, 100]
#particle_size_min_list = [0.01, 0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509]
#particle_size_max_list = [0.01778, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509, 100]
#particle_size_min_list = [0.01, 0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509]
#particle_size_max_list = [0.02239, 0.02818, 0.03548, 0.04467, 0.05623, 0.07079, 0.08912, 0.11220, 0.14125, 0.17783, 0.22387, 0.28184, 0.35481, 0.44668, 0.56234, 0.70795, 0.89125, 1.12202, 1.41254, 1.77828, 2.23872, 2.81838, 3.54813, 4.46684, 5.62341, 7.07946, 8.91251, 11.22019, 14.12538, 17.78279, 22.38721, 28.18383, 35.48134, 44.66836, 56.23413, 70.79458, 89.12509, 100]
#size_bin = list(range(1,42))
size_bin = list(range(1,len(d_repr)+1))

col_list = ["height", "mass", "depth", "diameter", "span", "width", "objectClass", "mass"]
df_mass = pd.read_excel("discos_database_re-entry_epoch_2016-11-01.xlsx", usecols = col_list)
#df = pd.read_excel("discos_database_complete.xlsx", usecols = col_list)

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

"""roh_aluminum = 2700
sphere_mass_list = []
for i in range(len(d_repr)):
    sphere_mass = (4/3)*roh_aluminum*np.pi*(d_repr[i]/2)**3
    sphere_mass_list.append(sphere_mass)"""

#d_repr in [m]
d_repr_1 = np.array(d_repr)
#density in [kg/m^3]
roh = 2.8*((d_repr_1*100)**(-0.74)) * 1000
sphere_mass = (4/3)*roh*np.pi*(d_repr_1/2)**3
sphere_mass_list = sphere_mass.tolist()

debris_mass_list = []
print(yaj)
print(sphere_mass_list)
for i in range(len(d_repr)):
    debris_mass_list.append(min(yaj[i], sphere_mass_list[i]))


N_list = []
for i in range(len(debris_mass_list)):
    M = 468 #Swarm B mass
    v_rel = 10*1000
    m = debris_mass_list[i]
    L_c = 0.01
    span = 1
    
    #if m < M:
    if d_repr[i] < span:
        if (m*v_rel**2)/(2*M) > 40000:
            P = M + m
        else:
            P = m * v_rel
    #elif m > M:
    elif d_repr[i] > span:
        if (M*v_rel**2)/(2*m) > 40000:
            P = M + m
        else:
            P = M * v_rel
    
    """if (m*v_rel**2)/(2*M) < 40000:
        P = M + m
    else:
        P = m * v_rel"""

    N = 0.1*(P**0.75)*(L_c**(-1.71))
    N_list.append(N)

df_additional = {"particle_size_min":particle_size_min_list, "particle_size_max":particle_size_max_list, "size_bin":size_bin, "d_repr":d_repr, "debris_mass":debris_mass_list, "N": N_list}
df_additional = pd.DataFrame(data=df_additional)
df = pd.merge(df, df_additional)
df["annual_collision_p"].replace({"error": 0.0}, inplace=True)
df["effect"] = df["N"].astype(float)*df["annual_collision_p"].astype(float)

df = df.drop('f_rem_risk',1)
df = df.drop('f_res_risk',1)
df = df.drop('f_risk_red',1)
df = df.drop('false_alarm_rate',1)
df = df.drop('rem_risk',1)
#df = df.drop('res_risk',1)
#df = df.drop('risk_red',1)

df["acpl"].replace({"error": 0.0001}, inplace=True)
df['acpl'] = df['acpl'].astype("float")
df = df[df['acpl'] == 0.0001]
#df['size_bin'] = df['size_bin'].astype("int")
df.reset_index(drop=True, inplace=True)

"""#Use only first 21 Size bins
df = df[df['size_bin'].between(0, 22)]"""

#print(df.to_string())

h_list = df['sma'].unique().tolist()

#optical settings
d_ref_optical = 0.7/1000
h_ref_optical = 36000
exp_optical = -0.5

#values for Space Fence radar equation
lambda_radar_SF = 0.15/1000 #0.15
d_ref_radar_SF = 0.26/1000 #0.26 kommt genau auf 400km und 2cm
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
#print(df_fence_filter)

#Cut off the Size Bins which can be tracked and therefore avoided
"""df = pd.merge(df, df_fence_filter)
df = df[df['d_repr']<df['d_min']]
df.reset_index(drop=True, inplace=True)"""

#Implement Risk Matrix
#Likelihood
conditions_likelihood = [
    df['annual_collision_p'].astype(float).lt(0.0001),
    df['annual_collision_p'].astype(float).ge(0.0001) & df['annual_collision_p'].astype(float).lt(0.001),
    df['annual_collision_p'].astype(float).ge(0.001) & df['annual_collision_p'].astype(float).lt(0.01),
    df['annual_collision_p'].astype(float).ge(0.01) & df['annual_collision_p'].astype(float).lt(0.1),
    df['annual_collision_p'].astype(float).ge(0.1)
]
choices_likelihood = [1, 2, 3, 4, 5]
df['likelihood'] = np.select(conditions_likelihood, choices_likelihood)

#Consequence
conditions_consequence = [
    df['N'].astype(float).lt(1e4),
    df['N'].astype(float).ge(1e4) & df['N'].astype(float).lt(1e5),
    df['N'].astype(float).ge(1e5) & df['N'].astype(float).lt(1e6),
    df['N'].astype(float).ge(1e6) & df['N'].astype(float).lt(1e7),
    df['N'].astype(float).ge(1e7) 
]
choices_consequence = [1, 2, 3, 4, 5]
df['consequence'] = np.select(conditions_consequence, choices_consequence)

#Effect
df["risk"] = df['likelihood'] * df['consequence']

#normalize the effect to a interval between 0 and 1
#df["effect"] = df["effect"]/df["effect"].max()

#print(df.to_string())

#==========================================================================================================================================================#

#Heatmap
df = df.pivot("size_bin", "sma", "risk")
#ax = plt.axes()
#fig, ax = plt.subplots(figsize=(17,5))
fig, ax = plt.subplots(figsize=(17,10))
#ax = sns.heatmap(df_plot, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df, annot=True, fmt = ".0f", cbar_kws={'label': "Risk"}, ax=ax)
ax.set_title("Risk = Likelihood" + r'$ \times $' + "Consequence", weight='bold')
ax.set_ylabel("Size Bin")
ax.set_xlabel("Altitude [km]")
#ax.set_xticks(size_bin)
ax.invert_yaxis()
fig.savefig("bin_single_future.pdf", format="pdf", bbox_inches="tight")
plt.show()

#==========================================================================================================================================================#

"""font = {'size'   : 15}
plt.rc('font', **font)

#2D charts
df_sma_filter = df[df['sma'] == 800]
df_sma_filter.reset_index(drop=True, inplace=True)
df_sma_filter = df_sma_filter.astype({"size_bin": int, "annual_collision_p": float, "effect": float})
print(df_sma_filter.to_string())
fig = plt.figure()"""

"""ax = fig.add_subplot(111) #121
x = df_sma_filter["size_bin"].to_list()
y = df_sma_filter["annual_collision_p"].to_list()
ax.bar(x,y, width=0.7, label = "h = 800km" + "\n" + "i = 87.75°")
ax.set_ylabel(r'$ACP_w$')
ax.set_xlabel("Size Bin")
ax.set_xticks(range(1,42, 2))
ax.set_title("Likelihood", weight='bold')"""

"""ax1 = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["risk"].to_list()
ax1.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 87.75°")
ax1.set_ylabel("Risk")
ax1.set_xlabel("Size Bin")
ax1.set_xticks(range(1,42, 2))
ax1.set_title("Risk = Likelihood" + r'$ \times $' + "Consequence", weight='bold')"""

"""ax2 = fig.add_subplot(111) #122
x1 = df_sma_filter["size_bin"].to_list()
y1 = df_sma_filter["risk"].to_list()
ax2.bar(x1,y1, width = 0.7, label = "h = 800km" + "\n" + "i = 87.75°")
ax2.set_ylabel("Risk")
ax2.set_xlabel("Size Bin")
ax2.set_xticks(range(1,42, 2))
ax2.set_title("Risk = Likelihood" + r'$ \times $' + "Consequence", weight='bold') #\cdot"""

"""fig.tight_layout()
fig.set_size_inches(15, 5)
ax1.legend()
#plt.yscale("log")
#fig.savefig("sustainability_rating_plots/Risk_Score.pdf", format="pdf", bbox_inches="tight")
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