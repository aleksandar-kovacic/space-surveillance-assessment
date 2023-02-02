import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings
from scipy.optimize import curve_fit
#warnings.simplefilter(action='ignore', category=UserWarning)

"""col_list = ["length", "height", "depth", "Satcat.TotMass [kg]"]
df = pd.read_excel("database/5.03.02_Population.xlsm", usecols=col_list)
df["characteristic_length"] = (df["length"]+df["height"]+df["depth"])/3
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

input_X = df["characteristic_length"].to_list()
input_X = np.array(input_X)[:, np.newaxis]

output_Y = df["Satcat.TotMass [kg]"].to_list()
output_Y = np.array(output_Y)[:, np.newaxis]

X = np.array(input_X)
y = np.array(output_Y)
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))

d_repr_test = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
d_repr_test = np.array(d_repr_test)[:, np.newaxis]
d_repr_pred = reg.predict(d_repr_test)
print(d_repr_pred)

plt.scatter(input_X, output_Y, s = 1)
plt.plot(d_repr_test, d_repr_pred, color="black", linewidth=1)
plt.xlabel("d_repr [m]")
plt.ylabel("mass [kg]")
plt.show()

print(d_repr_pred.ravel().tolist())

#print(np.array(input_X)[:, np.newaxis].shape)
#print(np.array(df["Satcat.TotMass [kg]"].to_list())[:, np.newaxis].shape)"""

#===========================================================================================================================================================#

"""roh_max = 4700
roh_star = 2700
d_roof = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
m_circle = 2.6010410e-4
m_star = 1.4137210e-3
p=1.13
mass_list = []

for i in range(len(d_roof)):
    if (d_roof[i]*100) <= ((roh_star * m_circle)/(roh_max*m_star))**(1/3):
        m_roof = (roh_max/roh_star) * ((d_roof[i]*100) ** (1/3))
    else:
        m_roof = (d_roof[i]*100) ** (2*p)
    mass = m_roof * m_star
    mass_list.append(mass)

print(mass_list)

plt.plot(d_roof, mass_list)
plt.xlabel("reference diameter [m]")
plt.ylabel("mass [kg]")
plt.yscale("log")
plt.xscale("log")
plt.minorticks_on()
plt.grid(which = "both")
#plt.show()"""

#===========================================================================================================================================================#

"""col_list = ["Object type", "Mass", "Diameter", "Span"]
df = pd.read_excel("database/SDDB_without_LEO_bLEO_DB_test_vollständig.xlsx", usecols=col_list)
#df = df[df["Object type"] == "DEBRIS"]
#df = df[df["Object type"] != "PAYLOAD"]
df = df[df["Mass"] != 0]
print(df)
plt.scatter(df["Span"], df["Mass"])
plt.xlabel("Diameter [m]")
plt.ylabel("Mass [kg]")
plt.show()
"""
"""col_list = ["Object type", "Mass", "Diameter", "Span", "length", "depth", "height", "objectClass"]
df = pd.read_excel("database/SDDB_without_LEO_bLEO_DB_test_vollständig.xlsx", usecols=col_list)
#df = df[df["Object type"] != "DEBRIS"]
df = df[df["length"] != 0]
df = df[df["height"] != 0]
df = df[df["depth"] != 0]
df = df[df["Mass"] != 0]

#object_list = ["Rocket Body","Rocket Body","Rocket Mission Related Object","Payload","Payload Debris", "Payload Mission Related Object"]
#object_list = ["Rocket Body"]
#df = df[df["objectClass"].isin(object_list)]

df["characteristic_length"] = (df["length"]+df["height"]+df["depth"])/3
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

input_X = df["characteristic_length"].to_list()
input_X = np.array(input_X)[:, np.newaxis]

output_Y = df["Mass"].to_list()
output_Y = np.array(output_Y)[:, np.newaxis]

X = np.array(input_X)
y = np.array(output_Y)
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))

d_repr_test = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
d_repr_test = np.array(d_repr_test)[:, np.newaxis]
d_repr_pred = reg.predict(d_repr_test)
print(d_repr_pred)

plt.scatter(input_X, output_Y, s = 1)
plt.plot(d_repr_test, d_repr_pred, color="black", linewidth=1)
plt.xlabel("d_repr [m]")
plt.ylabel("mass [kg]")
plt.show()

#print(d_repr_pred.ravel().tolist())
#print(df["characteristic_length"].min())"""

#Mass-diameter funtion
"""d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
roh = 2.7 #Aluminum
debris_mass_list = []

for i in range(len(d_repr)):
    M_small = 3.35*1e-1*((d_repr[i]*100)**3)*roh
    M_1 = 1.3*1e-1*((d_repr[i]*100)**2.28)*roh
    M_2 = 1.18*1e+2*((d_repr[i]*100)**2)*roh
    d_2 = 59.67 #59.67
    d_1 = 5 #5

    if (d_repr[i]*100) <= 0.26:
        debris_mass = M_small
    if (d_repr[i]*100) > 0.26 and (d_repr[i]*100) <= 5:
        debris_mass = M_1
    if (d_repr[i]*100) > 5 and (d_repr[i]*100) <= 59.67:
        debris_mass = (   ((d_2-(d_repr[i]*100))/(d_2-d_1))*M_1 +  (((d_repr[i]*100)-d_1)/(d_2-d_1))*M_2   ) * roh
    if (d_repr[i]*100) > 59.67:
        debris_mass = M_2
    debris_mass_list.append(debris_mass)

plt.plot(d_repr, debris_mass_list)
plt.xlabel("d_repr [m]")
plt.ylabel("debris mass [g]")
plt.xscale("log")
plt.yscale("log")
plt.show()"""

"""#Currently implemented mass diameter model
d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
d_repr_empirical = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
#d_repr_empirical = np.logspace(-4,2, 900)

def mass_diameter_function(d_repr_empirical):
    d_repr = d_repr_empirical
    roh = 4 #2.7 Aluminum
    debris_mass_list = []

    for i in range(len(d_repr)):
        M_small = 3.35*1e5*((d_repr[i])**3)*roh
        M_1 = 4.71*1e3*((d_repr[i])**2.28)*roh
        M_2 = 1.18*1e+4*((d_repr[i])**2)*roh
        d_2 = 59.67/100 #59.67
        d_1 = 5/100 #5

        if (d_repr[i]*100) <= 0.26:
            debris_mass = M_small
        elif (d_repr[i]*100) > 0.26 and (d_repr[i]*100) <= 5:
            debris_mass = M_1
        elif (d_repr[i]*100) > 5 and (d_repr[i]*100) <= 59.67:
            debris_mass = (   ((d_2-(d_repr[i]))/(d_2-d_1))*M_1 +  (((d_repr[i])-d_1)/(d_2-d_1))*M_2   ) * roh
        elif (d_repr[i]*100) > 59.67:
            debris_mass = M_2
        debris_mass_list.append(debris_mass/1000)
    
    return debris_mass_list


def mass_diameter_regression(d_repr):
    col_list = ["Object type", "Mass", "Diameter", "Span", "length", "depth", "height", "objectClass"]
    df = pd.read_excel("database/SDDB_without_LEO_bLEO_DB_test_vollständig.xlsx", usecols=col_list)
    #df = df[df["Object type"] != "DEBRIS"]
    df = df[df["length"] != 0]
    df = df[df["height"] != 0]
    df = df[df["depth"] != 0]
    df = df[df["Mass"] != 0]

    object_list = ["Rocket Body","Rocket Body Debris","Rocket Mission Related Object","Payload","Payload Debris", "Payload Mission Related Object"]

    df = df[df["objectClass"].isin(object_list)]
    df["characteristic_length"] = (df["length"]+df["height"]+df["depth"])/3
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    input_X = df["characteristic_length"].to_list()
    input_X = np.array(input_X)[:, np.newaxis]

    output_Y = df["Mass"].to_list()
    output_Y = np.array(output_Y)[:, np.newaxis]

    X = np.array(input_X)
    y = np.array(output_Y)
    reg = LinearRegression().fit(X, y)
    #print(reg.score(X, y))

    d_repr_test = d_repr
    d_repr_test = np.array(d_repr_test)[:, np.newaxis]
    d_repr_pred = reg.predict(d_repr_test)
    #print(d_repr_pred)

    #print(d_repr_pred.ravel().tolist())
    #print(df["characteristic_length"].min())
    return d_repr_pred



debris_mass_list = mass_diameter_function(d_repr_empirical)

d_repr_pred_list_collection = []
d_repr_pred = mass_diameter_regression(d_repr)
d_repr_pred_list = d_repr_pred.ravel().tolist()
for i in range(len(d_repr_pred_list)):
    d_repr_pred_list_collection.append(i)

merged_list = debris_mass_list[0:16] + d_repr_pred_list_collection[16:42]

roh_aluminum = 4000
debris_mass_list_test = []
for i in range(len(d_repr)):
    debris_mass = (4/3)*roh_aluminum*np.pi*(d_repr[i]/2)**3
    debris_mass_list_test.append(debris_mass)

plt.plot(d_repr_empirical, debris_mass_list)
plt.plot(d_repr[18:42], d_repr_pred_list_collection[18:42], color="black")
plt.plot(d_repr, d_repr_pred_list_collection)
plt.plot(d_repr, merged_list)
plt.plot(d_repr, debris_mass_list_test)
plt.xlabel("d_repr [m]")
plt.ylabel("debris mass [kg]")
plt.xscale("log")
plt.yscale("log")
plt.show()"""

d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
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
d_repr_1 = np.array([0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008])
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
        if (m*v_rel**2)/(2*M) < 40000:
            P = M + m
        else:
            P = m * v_rel
    #elif m > M:
    elif d_repr[i] > span:
        if (M*v_rel**2)/(2*m) < 40000:
            P = M + m
        else:
            P = M * v_rel
    N = 0.1*(P**0.75)*(L_c**(-1.71))
    N_list.append(N)

size_bin = range(1,42)
plt.bar(size_bin, N_list, width = 0.3)
plt.xticks(range(1,42,2))
#plt.yscale("log")
plt.show()

