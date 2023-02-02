from cmath import log
from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
df = pd.read_csv("total_output.csv")
a_new_list = []
b_new_list = []

a = [0.894569, 0.953352]
b = [0.713567,1.927550]
a_new = 0.9
b_new = np.interp(a_new, a, b)

print(b_new)

#Darstellen wie die Interpolation performt

c = df["f_risk_red"][0:10].to_list()
v = df["man_rate"][0:10].to_list()

plt.plot(c,v)
plt.ylabel("Manoeuvre Rate")
plt.xlabel("Fractional Reduced Risk")

plt.axhline(y=4.02806, color = "r", linestyle = "-")
plt.axvline(x=0.872011, color = "r", linestyle = "-")

plt.show()"""




"""fig = plt.figure()
ax = fig.add_subplot(111)

df = pd.read_csv("total_output.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df['rel_risk_red'] = df['risk_red']/(df['risk_red']+df['rem_risk'])

x1=np.array(df["f_risk_red"][0:10].to_list())
y1=np.array(df["man_rate"][0:10].to_list())
x2=np.array([0.9, 0.9])
y2=np.array([-5, 40])

from intersect import intersection

x, y = intersection(x1, y1, x2, y2)

plt.plot(x1, y1, c="r")
plt.plot(x2, y2, c="g")
plt.plot(x, y, "*k")
plt.ylabel("Manoeuvre Rate")
plt.xlabel("Fractional Risk Reduction")
print(x,y)
plt.show()"""

scaling_factor_table = np.array([
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

scaling_factor_table = np.reshape(scaling_factor_table, (36,6))

scaling_factor = 0.2
scaling_factor_table[0:4, 0:6] = scaling_factor
scaling_factor_table[12:16, 0:6] = scaling_factor
scaling_factor_table[24:28, 0:6] = scaling_factor
print(scaling_factor_table)
