from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np
import seaborn as sns

"""df = pd.read_csv("ares_output_pop_variation/old_0,0177/old_0,0177_ares_output_data.csv")
print(df)
df_acp_d_ref = pd.read_csv("ares_output_pop_variation/old_0,0177/old_0,0177_acp_d_ref_data.csv")
print(df_acp_d_ref)
df_sma = pd.read_csv("ares_output_pop_variation/old_0,0177/old_0,0177_sma_data.csv")
print(df_sma)

#Transform columns of dataframe into lists
acpl = df["acpl"].tolist()
f_rem_risk = df["f_rem_risk"].tolist()
f_res_risk = df["f_res_risk"].tolist()
f_risk_red = df["f_risk_red"].tolist()
false_alarm_rate = df["false_alarm_rate"].tolist()
man_rate = df["man_rate"].tolist()
rem_risk = df["rem_risk"].tolist()
res_risk = df["res_risk"].tolist()
risk_red = df["risk_red"].tolist()
annual_collision_p = df_acp_d_ref["annual_collision_p"].tolist()
d_ref = df_acp_d_ref["d_ref"].tolist()
sma = df_sma["sma"].tolist()

start = 0
end = 10
counter = 0
# Solange durchiterieren, bis man durch die gesammelten acpl Liste durchkommt (man hätte auch risk_red oder res_risk nehmen können, 
# da diese auch 10 Einträge haben)
while end <= len(acpl):
    x = acpl[start:end]
    y1 = res_risk[start:end]
    y2 = risk_red[start:end]
    y3 = rem_risk[start:end]
    plt.plot(x,y1,label = "Residual Risk " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    plt.plot(x,y2, label = "Risk Reduction " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    plt.plot(x,y3, label = "Remaining Risk " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    # "center left"
    plt.legend(loc="upper left", prop={'size': 8})
    plt.ylabel("Risk")
    plt.xlabel("Accepted Collision Probability Level")
    plt.xscale("log")
    plt.axvline(x=0.0001, color = "r", linestyle = "-")
    plt.axhline(y=0.0366, color = "y")
    plt.axvline(x=0.013, color = "y", linestyle = "-")
    plt.minorticks_on()
    # axis = "y"
    plt.grid(which = "both")
    start = start + 10
    end = end +10
    counter = counter + 1

start = 0
end = 10
counter = 0
# Solange durchiterieren, bis man durch die gesammelten acpl Liste durchkommt (man hätte auch risk_red oder res_risk nehmen können, 
# da diese auch 10 Einträge haben)
while end <= len(acpl):
    x = acpl[start:end]
    y1 = man_rate[start:end]
    #y2 = risk_red[start:end]
    plt.plot(x,y1, label = "Manoeuvre Rate vs ACPL " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    #plt.plot(x,y2, label = "Risk Reduction " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    # "center left" "upper center"
    plt.legend(loc="upper center", prop={'size': 8})
    plt.ylabel("Manoeuvre Rate")
    plt.xlabel("Accepted Collision Probability Level")
    plt.xscale("log")
    plt.axvline(x=0.0001, color = "r", linestyle = "-")
    plt.axvline(x=0.013, color = "y")
    plt.minorticks_on()
    # axis = "y"
    plt.grid(which = "both")
    plt.ylim(0,20)
    start = start + 10
    end = end + 10
    counter = counter + 1

start = 0
end = 10
counter = 0
# Solange durchiterieren, bis man durch die gesammelten acpl Liste durchkommt (man hätte auch risk_red oder res_risk nehmen können, 
# da diese auch 10 Einträge haben)
while end <= len(acpl):
    x = man_rate[start:end]
    y1 = res_risk[start:end]
    y2 = risk_red[start:end]
    y3 = rem_risk[start:end]
    plt.plot(x,y1, label = "Residual Risk " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    plt.plot(x,y2, label = "Risk Reduction " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    plt.plot(x,y3, label = "Remaining Risk " + "d_ref = " + str(d_ref[counter]) + "m " + str(sma[counter]) + "km")
    # "center left" "upper center"
    plt.legend(loc="upper right", prop={'size': 8})
    plt.ylabel("Risk")
    plt.xlabel("Manoeuvre Rate")
    plt.xlim(0,6)
    plt.minorticks_on()
    # axis = "y"
    plt.grid(which = "both")
    #plt.xscale("log")
    start = start + 10
    end = end +10
    counter = counter + 1

plt.show()"""



"""#plot heatmap
df = pd.read_csv("sma_inc_acpl/oldSSN_2.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df_new = df.loc[df['acpl'] == 0.0001]
print(df_new.to_string())

sns.set(rc = {'figure.figsize':(10,7)})
df_new = df_new.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_new,annot = True, fmt = ".1f", cbar_kws={'label': 'Manoeuvre Rate at ACPL = 0.0001'})
ax.set_title("Size > 1.0: Manoeuvre Rate of SWARM B type mission with" + "\n" + "Space Fence for the Reference Epoch 2016")
ax.set_ylabel("Scaling Factor")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()
plt.show()"""

"""#Plot Manoeuvre Rate ate Fractional Risk Reduction = 0.9
acpl_steps = 10
df = pd.read_csv("total_output.csv")
df['sma'] = df['sma'] - 6378.137
df['sma'] = df['sma'].round(0).astype("int")
df['rel_risk_red'] = df['risk_red']/(df['risk_red']+df['rem_risk'])
#df=df.loc[df['inc']==90]
#df=df.loc[df['sma']==600]
#df=df.loc[df['d_ref']==0.1]

start = 0
end = acpl_steps
i=0
index_collection = []

#Interpolate Section
a_new_list = []
b_new_list = []
sma_list = []
inc_list = []


while i < int(len(df)/acpl_steps):
    df_new = df[start:end]
    
    #findet die Zeile, die am nächsten an 0.9 ist. (Bsp: 0.89 würde vor 0.93 bevorzugt werden, da 0.89 näher an 0.9 liegt)
    #result_index = df_new['f_risk_red'].sub(0.9).abs().idxmin()
    
    #findet die Zeile, die gerade >90% ist
    #result_index = df_new[df_new['f_risk_red'].lt(0.9)].index[0]-1

    #findet die Zeile die gerade >90% ist
    result_index = df_new.loc[df_new['f_risk_red'].gt(0.9), 'f_risk_red'].idxmin()

    #Interpolate Section
    a = [df_new.at[result_index + 1, "f_risk_red"], df_new.at[result_index, "f_risk_red"]]
    b = [df_new.at[result_index + 1, "man_rate"], df_new.at[result_index, "man_rate"]]
    a_new = 0.9
    b_new = np.interp(a_new, a, b)
    a_new_list.append(a_new)
    b_new_list.append(b_new)
    sma_list.append(df_new.at[result_index, "sma"])
    inc_list.append(df_new.at[result_index, "inc"])
    

    start = start + acpl_steps
    end = end + acpl_steps
    i=i+1
    index_collection.append(result_index)
print(index_collection)
df2 = df.reindex(index_collection)
print(df.to_string())
print(df2[0:3].to_string())

#Interpolate Section
df_interpolated = pd.DataFrame(list(zip(a_new_list, b_new_list, sma_list, inc_list)), columns = ["f_risk_red", "man_rate", "sma", "inc"])
print(df_interpolated[0:3].to_string())
df_interpolated = df_interpolated.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df_interpolated, cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) = 90%'})
ax.set_title("Manoeuvre Rate of SWARM B type mission with" + "\n" + "old SSN for the Reference Epoch 2016")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()"""


"""df2 = df2.pivot("inc", "sma", "man_rate")
ax = plt.axes()
ax = sns.heatmap(df2, cbar_kws={'label': 'Manoeuvre Rate at Relative Risk Reduction (f_risk_red) > 90%'})
ax.set_title("Manoeuvre Rate of SWARM B type mission with" + "\n" + "old SSN for the Reference Epoch 2016")
ax.set_ylabel("Inclination [°]")
ax.set_xlabel("Altitude [km]")
ax.invert_yaxis()"""

#plt.show()



