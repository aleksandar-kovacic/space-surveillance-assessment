import matplotlib.pyplot as plt
from pexpect import which

with open('MASTER_output_2036_inc_sma.txt', "r") as f:
    lines_2022 = f.readlines()

flux_list_2022 = []
altitude_list = []

for i in range(2,len(lines_2022)):
    flux_list_2022.append(float(lines_2022[i][204:214]))
    altitude_list.append(float(lines_2022[i][0:12].strip()))


plt.bar(altitude_list, flux_list_2022, label="MASTER 2036", width = 100)
plt.xlabel("Semi-major axis [km]")
#plt.xticks([1000, 10000, 100000])
save_name = "sma_flux_plot.pdf"

plt.ylabel("Flux [1/km$^3$y]")
plt.grid(which="both")
plt.legend()
#plt.savefig(save_name, format = "pdf", dpi = 2000, bbox_inches = "tight")
plt.show()

