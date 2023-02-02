from matplotlib import pyplot as plt
import numpy as np
from configparser import ConfigParser
import pandas as pd

plt.rc('axes', axisbelow=True)

parameter_config = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
parameter_config.read("first_result_converging_acpd_binned_cov.ini")

covariance_matrix = np.reshape([float(i) for i in parameter_config.getlist('debris_uncertainty', 'covariance_matrix')], (36, 18))
covariance_matrix = covariance_matrix * float(parameter_config["debris_uncertainty"]["covariance_matrix_factor"])

sma = ["hp1", "hp2", "hp3", "hp4", "hp5", "hp6"] * 6
inc = ["i1", "i2", "i3", "i4", "i5", "i6"] 
e = ["e1, e2"]
size = ["s1", "s2", "s3"]


#Behalte nur die Spalten, die die Unsichrheit in Flugrichtung geben
keep_columns = [0, 3, 6, 9, 12, 15]
covariance_matrix = covariance_matrix[:,keep_columns] 

covariance_list = []
sma_list = []
inc_list = []

columns = 6
rows = 6
for j in range(columns):
    for i in range(rows):
        covariance_list.append(covariance_matrix[i][j])
        sma_list.append(sma[i])
        inc_list.append(inc[j])


df_at = pd.DataFrame(data = {"cov":covariance_list, "sma":sma_list, "inc": inc_list})
df_at = df_at[df_at["sma"] != "hp6"]

at = df_at["cov"][0:5]*1000
ct = df_at["cov"][0:5]*0.4*1000
r = df_at["cov"][0:5]*0.2*1000

X_axis = np.arange(len(df_at["sma"][0:5]))


"""plt.bar(X_axis - 0.2, df_at["cov"][0:5]*1000, width = 0.2, label= "Along-track")
plt.bar(X_axis + 0, ct, width = 0.2, label= "Cross-track")
plt.bar(X_axis + 0.2, r, width = 0.2, label= "Radial")
plt.xticks(X_axis, df_at["sma"][0:5])
plt.xlabel("Perigee altitude classes")
plt.ylabel("Uncertainty [m]")
plt.title("Uncertainty requirement to reduce" +"\n"+ "the sustainability score to 'Low'")
plt.grid(axis = "y")
plt.yticks(np.linspace(0, 500, 11))
plt.legend()
plt.savefig("first_result_converging_acpd_cov.pdf", dpi = 2000, format = "pdf", bbox_inches = "tight")
plt.show()"""

fig, ax = plt.subplots(figsize=(10,4.5))

deviation = 0.3
width = 0.3
decimal = 2
p1 = ax.bar(X_axis - deviation, at.round(decimal), width, label= "Along-track")
p2 = ax.bar(X_axis + 0, ct.round(decimal), width, label= "Cross-track")
p3 = ax.bar(X_axis + deviation, r.round(decimal), width, label= "Radial")

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel("Uncertainty [m]")
ax.set_xlabel("Perigee altitude classes")
#ax.set_title("Uncertainty requirement in order to reduce the sustainability score to 'Low'")
ax.set_title("Uncertainty requirement until the sustainability score converges")
ax.set_xticks(X_axis, df_at["sma"][0:5])
ax.legend()

# Label with label_type 'center' instead of the default 'edge'
ax.bar_label(p1)
ax.bar_label(p2)
ax.bar_label(p3)
#, label_type='center'
plt.grid(axis = "y")
#plt.savefig("first_result_converging_acpd_cov_bar.pdf", dpi = 2000, format = "pdf", bbox_inches = "tight")

plt.show()

