"""import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
#d_repr = [0.01024, 0.01180, 0.01486, 0.01870, 0.02355, 0.02964, 0.03732, 0.04698, 0.05915, 0.07446, 0.09374, 0.11801, 0.14857, 0.18704, 0.23547, 0.29643, 0.37319, 0.46982, 0.59146, 0.74461, 0.93740, 1.18012, 1.48569, 1.87037, 2.35465, 2.96433, 3.73187, 4.69815, 5.91462, 7.44607, 9.37404, 11.80122, 14.85686, 18.70368, 23.54653, 29.64333, 37.31874, 46.98151, 59.14622, 74.46068, 91.30008]
d_repr = np.logspace(-2, 2, 1000)

roh = 2.7 #Aluminum
debris_mass_list = []

for i in range(len(d_repr)):
    M_small = 3.35*1e-1*((d_repr[i]*100)**3)*roh
    M_1 = 1.3*1e-1*((d_repr[i]*100)**2.28)*roh
    M_2 = 1.18*1e+2*((d_repr[i]*100)**2)*roh
    d_2 = 59.67
    d_1 = 5

    if (d_repr[i]*100) <= 0.26:
        debris_mass = M_small
    if (d_repr[i]*100) > 0.26 and (d_repr[i]*100) <= 5:
        debris_mass = M_1
    if (d_repr[i]*100) > 5 and (d_repr[i]*100) <= 59.67:
        debris_mass = (   ((d_2-(d_repr[i]*100))/(d_2-d_1))*M_1 +  (((d_repr[i]*100)-d_1)/(d_2-d_1))*M_2) * roh
    if (d_repr[i]*100) > 59.67:
        debris_mass = M_2
    debris_mass_list.append(debris_mass/1000)

plt.plot(d_repr, debris_mass_list)
plt.yscale("log")
plt.xscale("log")
plt.minorticks_on()
plt.grid(which = "both")
plt.ylabel("Mass [kg]")
plt.xlabel("Characteristic length d_repr [m]")
plt.show()"""

"""import numpy as np
#19: 100er Schritt
#37: 50er Schritte
#73: 25er Schritte
x = np.linspace(200,2000,73) 
print(x)"""
