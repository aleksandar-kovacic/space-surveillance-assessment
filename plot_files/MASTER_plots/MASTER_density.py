import matplotlib.pyplot as plt



with open('MASTER_altitude_density.txt', "r") as f:
    lines = f.readlines()

density_list = []
altitude_list = []

for i in range(2,len(lines)):
    density_list.append(float(lines[i][205:216]))     #204:214
    altitude_list.append(float(lines[i][0:12].strip()))

print(density_list)

plt.plot(altitude_list, density_list, label="MASTER 2022"+"\n"+"Size interval: [0.01 m; 100 m]")
plt.xlabel("Altitude [km]")
plt.xticks(list(range(-90, 105, 15)))
save_name = "MASTER_2022_altitude_density.pdf"

plt.ylabel("Spatial density [1/km$^3$]")
plt.xscale("log")
plt.grid(which="both")
plt.legend()
plt.savefig(save_name, format = "pdf", dpi = 2000, bbox_inches = "tight")
plt.show()
