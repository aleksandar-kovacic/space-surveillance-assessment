from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np
import seaborn as sns
from intersect import intersection

def interpolated_intercept(x, y1, y2):
    """Find the intercept of two curves, given by the same x data"""

    def intercept(point1, point2, point3, point4):
        """find the intersection between two lines
        the first line is defined by the line between point1 and point2
        the first line is defined by the line between point3 and point4
        each point is an (x,y) tuple.

        So, for example, you can find the intersection between
        intercept((0,0), (1,1), (0,1), (1,0)) = (0.5, 0.5)

        Returns: the intercept, in (x,y) format
        """    

        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]

            x = Dx / D
            y = Dy / D
            return x,y

        L1 = line([point1[0],point1[1]], [point2[0],point2[1]])
        L2 = line([point3[0],point3[1]], [point4[0],point4[1]])

        R = intersection(L1, L2)

        return R

    idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0)
    xc, yc = intercept((x[idx], y1[idx]),((x[idx+1], y1[idx+1])), ((x[idx], y2[idx])), ((x[idx+1], y2[idx+1])))
    return xc,yc





#Plot Manoeuvre Rate at Fractional Risk Reduction = 0.9
acpl_steps = 10
#df = pd.read_csv("total_output.csv")
df = pd.read_csv("../plot_files/requirement_plots/cov_2.csv")
df["sma"] = [6378.137+300]*len(df)
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df['inc'] = df['inc'].round(0).astype("int")

start = 0
end = acpl_steps
i=0

f_risk_red_list = []
man_rate_list = []
sma_list = []
inc_list = []

#print(df.to_string())

while i < int(len(df)/acpl_steps):
    df_new = df[start:end]

    x  = np.array(df_new["man_rate"])
    y1 = np.array(df_new["f_risk_red"])
    y2 = np.array([0.9]*len(df_new[0:acpl_steps]))

    idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0)

    # new method!
    xc, yc = interpolated_intercept(x,y1,y2)
    print(xc)
    
    f_risk_red_list.append(yc[0][0])
    man_rate_list.append(xc[0][0])
    
    sma_list.append(df_new.at[start, "sma"])
    inc_list.append(df_new.at[start, "inc"])

    start = start + acpl_steps
    end = end + acpl_steps
    i=i+1

df_total_output = pd.DataFrame(
        data = {"f_risk_red": f_risk_red_list, "man_rate": man_rate_list, "sma": sma_list, "inc": inc_list}
    )
print(df_total_output)

sns.set(rc = {'figure.figsize':(9,7)})
df_total_output = df_total_output.pivot("inc", "sma", "man_rate")
ax = plt.axes()
#ax = sns.heatmap(df_total_output, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax = sns.heatmap(df_total_output, annot=True, fmt = ".2f", cbar_kws={'label': 'Manoeuvre rate at fractional risk reduction = 90%'})
ax.set_title("Manoeuvre rate of Sentinel-3A type mission with" + "\n" + "new SSN for the epoch 2022")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
#plt.savefig("cov_2.pdf" ,dpi = 1500, bbox_inches = "tight")

plt.show()