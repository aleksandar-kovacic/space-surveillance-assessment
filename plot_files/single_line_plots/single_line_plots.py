import pandas as pd
import matplotlib.pyplot as plt
from intersect import intersection
import numpy as np
df = pd.read_csv("SENTINEL3A_oldSSN_2022.csv")
#df['rel_risk_red'] = df['risk_red']/(df['risk_red']+df['rem_risk'])
df['rel_risk_red'] = df['risk_red']/(df['risk_red']+df['res_risk'])

print(df["rel_risk_red"].to_string())
print(df["f_risk_red"].to_string())
x=df["acpl"]
y=df["f_risk_red"]
y_man = df["man_rate"]

frr = 0.9
"""#line at fractional risk reduction = 90%
plt.hlines(y = frr, xmin = 1e-9, xmax = 1e-1, color = "red")

#calculate intersecting point of hoizontal line (90%) and acpl vs fractional risk reduction diagram
x2 = [1e-9, 1e-1]
y2 = [frr, frr]
a, b = intersection(np.array(x), np.array(y), np.array(x2), np.array(y2))
print(a[0])

#draw the line that determines the acpl value
plt.vlines(x=a[0], ymin = 0, ymax = 1, color = "red")

plt.plot(x, y)
#plt.vlines(x = 5e-5, ymin = 0, ymax = 1)
plt.xlabel("Accepted collision probability level")
plt.ylabel("Fractional risk reduction")
plt.xscale("log")
plt.grid(which = "both")
#plt.savefig("swarmB.pdf", dpi = 1000, bbox_inches="tight")
plt.show()"""

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(121)

#line at fractional risk reduction = 90%
ax.axhline(y = frr, color = "red")

#calculate intersecting point of hoizontal line (90%) and acpl vs fractional risk reduction diagram
x2 = [1e-9, 1e-1]
y2 = [frr, frr]
a, b = intersection(np.array(x), np.array(y), np.array(x2), np.array(y2))
print(a[0])
#a[0] replacement:
correction = 4e-5

#draw the line that determines the acpl value
ax.axvline(x=correction,color = "red")
ax.plot(x,y)

ax.set_xlabel("Accepted collision probability level")
ax.set_ylabel("Fractional risk reduction")
ax.set_xscale("log")
ax.set_xticks(np.logspace(-9,-1, 9))
ax.grid(which = "both")





ax2=fig.add_subplot(122)
#line at fractional risk reduction = 90%
ax2.axvline(x=correction,color = "red")


#calculate intersecting point of hoizontal line (90%) and acpl vs fractional risk reduction diagram
x2 = [correction, correction]
y2 = [0, 10000]
c, d = intersection(np.array(x), np.array(y_man), np.array(x2), np.array(y2))
print(d[0])
correction_2 = d[0]

#draw the line that determines the acpl value
ax2.axhline(y = correction_2, color = "red")
ax2.plot(x, y_man)
ax2.set_xlabel("Accepted collision probability level")
ax2.set_ylabel("Manoeuvre rate")
ax2.set_xscale("log")
ax2.set_xticks(np.logspace(-9,-1, 9))
ax2.grid(which = "both")

fig.suptitle("Sentinel-3A type mission in 500 km altitude")
#fig.savefig("500km_oldSSN_2022.pdf", dpi = 1500, bbox_inches="tight")
#plt.show()