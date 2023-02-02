from turtle import color
import numpy as np
import matplotlib.pyplot as plt

h_list = np.logspace(2, 4.5563, 10000)

#optical settings
d_ref_optical = 0.7/1000
h_ref_optical = 36000
exp_optical = -0.5

#radar settings
lambda_radar = 0.3/1000
d_ref_radar = 0.32/1000
h_ref_radar = 2000
exp_radar = 2

#collect the values in the loop
d_min_final_list=[]
#these values can be used to plot the d_min_radar, d_min_optical and d_rcs line individually
d_min_radar_line = []
d_min_optical_line = []
d_rcs_line = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar*((h_list[i]/h_ref_radar)**exp_radar)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar**2)*((h_list[i]/h_ref_radar)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #convert d_min_final to cm for better illustration
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list.append(d_min_final)
    #needed to plot the individual lines
    d_min_radar_line.append(d_min_radar*1000*100)
    d_min_optical_line.append(d_min_optical*1000*100)
    d_rcs_line.append(d_rcs*1000*100)

###########################################################################################################################

#values for Space Fence radar equation
lambda_radar_SF = 0.15/1000
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
    
    #convert d_min_final to cm for better illustration
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_SF.append(d_min_final)


"""lambda_radar_1 = 0.3/1000
d_ref_radar_1 = 0.3/1000 #0.26 kommt genau auf 400km und 2cm
h_ref_radar_1 = 2000
exp_radar_1 = 2.0
d_min_final_list_1 = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_1*((h_list[i]/h_ref_radar_1)**exp_radar_1)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_1**2)*((h_list[i]/h_ref_radar_1)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_1)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #convert d_min_final to cm for better illustration
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_1.append(d_min_final)

lambda_radar_2 = 0.3/1000
d_ref_radar_2 = 0.17/1000 #0.26 kommt genau auf 400km und 2cm
h_ref_radar_2 = 2000
exp_radar_2 = 2.0
d_min_final_list_2 = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_2*((h_list[i]/h_ref_radar_2)**exp_radar_2)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_2**2)*((h_list[i]/h_ref_radar_2)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_2)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #convert d_min_final to cm for better illustration
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_2.append(d_min_final)

lambda_radar_3 = 0.13/1000
d_ref_radar_3 = 0.08/1000 #0.26 kommt genau auf 400km und 2cm
h_ref_radar_3 = 2000
exp_radar_3 = 2.0
d_min_final_list_3 = []

for i in range(len(h_list)):

    d_min_radar = d_ref_radar_3*((h_list[i]/h_ref_radar_3)**exp_radar_3)
    d_min_optical = d_ref_optical*((h_list[i]/h_ref_optical)**-0.5)

    d_min = min(d_min_radar, d_min_optical)

    sigma = (1/4)*(np.pi)*(d_ref_radar_3**2)*((h_list[i]/h_ref_radar_3)**4)
    d_rcs = (sigma*(4/9)*(((lambda_radar_3)**4)/(np.pi**5)))**(1/6)

    d_min_final = max(d_min, d_rcs)
    
    #convert d_min_final to cm for better illustration
    d_min_final = d_min_final * 1000 * 100
    
    d_min_final_list_3.append(d_min_final)
"""

plt.plot(h_list, d_min_final_list[0:len(h_list)], label = "$D_{ref}$ = " + str(d_ref_radar*1000) + " m, " + "$\u03BB$ = " + str(lambda_radar*1000) + " m (current SSN)")
plt.plot(h_list, d_min_final_list_SF[0:len(h_list)], label = "$D_{ref}$ = " + str(d_ref_radar_SF*1000) + " m, " + "$\u03BB$ = " + str(lambda_radar_SF*1000) +" m (SSN with SF)")
#plt.plot(h_list, d_min_final_list_1[0:len(h_list)], label = "$D_{ref}$ = " + str(d_ref_radar_1*1000) + " m, " + "$\u03BB$ = " + str(lambda_radar_1*1000) +" m")
#plt.plot(h_list, d_min_final_list_2[0:len(h_list)], label = "$D_{ref}$ = " + str(d_ref_radar_2*1000) + " m, " + "$\u03BB$ = " + str(lambda_radar_2*1000) +" m")
#plt.plot(h_list, d_min_final_list_3[0:len(h_list)], label = "$D_{ref}$ = " + str(d_ref_radar_3*1000) + " m, " + "$\u03BB$ = " + str(lambda_radar_3*1000) +" m")
#plt.vlines(x=2000, ymin = 1, ymax = 32, color = "red")
#plt.hlines(y=32, xmin = 100, xmax = 2000, color = "red")
plt.yscale("log")
plt.xscale("log")
plt.legend(loc="lower right", prop={'size': 8})
plt.ylabel("Minimum detectable diamater d [cm]")
plt.xlabel("Altitude h [km]")

#plt.axhline(y=3.1, color = "r", linestyle = "-")
#plt.axvline(x=500, color = "r", linestyle = "-")
#plt.axhline(y=10, color = "y", linestyle = "-")
#plt.axvline(x=2000, color = "y", linestyle = "-")
#plt.axhline(y=1, color="g", linestyle="-")

#plt.axhline(y=1, color = "r", linestyle = "-")
#plt.axvline(x=300, color = "r", linestyle = "-")

plt.minorticks_on()
plt.grid(which = "both")

"""
#zum plotten der einzelnen Geraden
h_list_first = [100,900]
h_list_second = [900,5000]
h_list_third = [5000, 30000]
plt.plot(h_list_first, d_min_radar_line)
plt.plot(h_list_second, d_min_optical_line)
plt.plot(h_list_third, d_rcs_line)
plt.yscale("log")
plt.xscale("log")"""

#plt.savefig("../sustainability_rating/requirement_plots/i=90°_radar_equation_emr.pdf", dpi = 2500, bbox_inches = "tight", format = "pdf")
plt.savefig("ssn_equation.pdf", dpi = 2500, bbox_inches = "tight", format = "pdf")
plt.show()