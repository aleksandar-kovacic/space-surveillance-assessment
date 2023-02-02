from configparser import ConfigParser
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint
parameter_config = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
parameter_config.read("cov_3_new.ini")
_R_EARTH = 6378.137
covariance_matrix = np.reshape([float(i) for i in parameter_config.getlist('debris_uncertainty', 'covariance_matrix')], (36, 18))
#sma = list(np.array([float(i) for i in parameter_config.getlist('parameters', 'altitude')]) + _R_EARTH)
#inc = [float(i) for i in parameter_config.getlist('parameters', 'inc')]

sma = ["h$_{p1}$", "h$_{p2}$", "h$_{p3}$", "h$_{p4}$", "h$_{p5}$", "h$_{p6}$"] * 6
inc = ["i1", "i2", "i3", "i4", "i5", "i6"] 
inc = ["i$_1$", "i$_2$", "i$_3$", "i$_4$", "i$_5$", "i$_6$"]
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


df = pd.DataFrame(data = {"cov":covariance_list, "sma":sma_list, "inc": inc_list})
df = df[df["sma"] != "h$_{p6}$"]


sns.set(rc = {'figure.figsize':(7,5)})
df = df.pivot("inc", "sma", "cov")
ax = plt.axes()
#ax = sns.heatmap(df, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df, annot=True, fmt = ".2f", cbar_kws={'label': 'Uncertainty along-track [km]'})
ax.set_title("Required uncertainty to approx. reach one manoeuvre at a fractional" + "\n" + "risk reduction of 90 %. Spacecraft uncertainty set to 1 m." + "\n" + "New SSN for epoch 2036")
ax.set_ylabel("Inclination class")
ax.set_xlabel("Perigee altitude class")
ax.invert_yaxis()
plt.savefig("cov_3_new_regions.pdf" ,dpi = 1500, bbox_inches = "tight")

plt.show()

"""import numpy as np
a = list(np.around(np.linspace(0.01,0.33, 12),2))
#particle_min_size
b = a[0:len(a)-1]
#particle_max_size
c = a[1:len(a)]

d_repr_list = []
for i in range(len(b)):
    y = (c[i]+b[i])/2
    d_repr_list.append(y)
#d_repr
d_repr_list = list(np.around(d_repr_list,9))

print(b)
print(c)
print(d_repr_list)
"""
