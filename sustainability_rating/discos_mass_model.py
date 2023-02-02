from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

font = {'size'   : 12}

plt.rc('font', **font)

col_list = ["height", "mass", "depth", "diameter", "span", "width", "objectClass", "mass"]
df = pd.read_excel("discos_database_re-entry_epoch_2016-11-01.xlsx", usecols = col_list)
#df = pd.read_excel("discos_database_complete.xlsx", usecols = col_list)

df.dropna(subset = ["mass"], inplace=True)
df["d_repr"] = df[["height", "depth", "width", "diameter", "span"]].max(axis=1)
df.dropna(subset = ["d_repr"], inplace=True)

df = df.loc[df['objectClass'].isin(['Rocket Body'])]
print(len(df))

#If "discos_database_complete.xlsx" is read. Deletes unrealistic values
#df = df[df["mass"] < 100000]
#df = df[df["d_repr"] < 2500]

df.reset_index(drop=True, inplace=True)


# Abhishek Bhatia's data & scatter plot.
# https://stackoverflow.com/questions/32536226/log-log-plot-linear-regression
input_X = df["d_repr"].to_list()
input_X = np.array(input_X) #[:, np.newaxis]

output_Y = df["mass"].to_list()
output_Y = np.array(output_Y) #[:, np.newaxis]

X = np.array(input_X)
y = np.array(output_Y)

d_repr = np.logspace(-2,2,1000)
#d_repr = np.array([0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008])
#Source: https://stackoverflow.com/questions/50516862/scipy-curve-fit-returns-multiple-lines
def func(X, a, b):
    # a * np.power(X, b) very good, R_2 = 0.31
    #return a*X**(2*b) #R_2=0.29 very good
    # a * np.exp(-b * X) + c  not good
    # a+b*X-c*np.exp(-d*X) not good
    return a * np.power(X, b)

popt, pcov = curve_fit(func, X, y)

# calculate R2 value. The higher R2 (0-100%) the better the model. https://stackoverflow.com/questions/19189362/getting-the-r-squared-value-using-curve-fit
residuals = y - func(X, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
print(r_squared)
print(popt)


xaj = np.array(d_repr) #np.logspace(-2, 2, 1000)
yaj = func(xaj, *popt)



"""roh_aluminum = 2700
sphere_mass_list = []
for i in range(len(d_repr)):
    sphere_mass = (4/3)*roh_aluminum*np.pi*(d_repr[i]/2)**3
    sphere_mass_list.append(sphere_mass)"""

#d_repr in [m]
#density in [kg/m^3]
roh = 2.8*((d_repr*100)**(-0.74)) * 1000
sphere_mass = (4/3)*roh*np.pi*(d_repr/2)**3
sphere_mass_list = sphere_mass.tolist()

debris_mass_list = []
for i in range(len(d_repr)):
    debris_mass_list.append(min(yaj[i], sphere_mass_list[i]))
plt.plot(d_repr, debris_mass_list, label = "Combined curve")

#plt.scatter(X,y, label = 'DISCOS data', s = 10)
#plt.plot(xaj, yaj, label = 'Best fit to DISCOS data', color = "r")
#plt.plot(d_repr, sphere_mass_list, label = "Mass of sphere",  color = "g")
plt.legend()
plt.xlabel(r"$d_{\mathrm{repr, i}}$" + " [m]")
plt.ylabel(r"$m_{\mathrm{combined}}$" + " [kg]")
#plt.ylabel("m [kg]")

plt.xscale("log")
plt.yscale("log")

plt.minorticks_on()
plt.grid(which = "both")

plt.savefig("sustainability_rating_plots/mass_distribution_combined.pdf", format="pdf", bbox_inches="tight")
plt.show()

