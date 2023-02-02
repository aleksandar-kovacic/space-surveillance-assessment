import matplotlib.pyplot as plt
from pexpect import which

#plot declination or altitude on the x-axis: "dec" or "inc"
which_plot = "inc"

if which_plot=="inc":
    with open('MASTER_output_2022.txt', "r") as f:
        lines_2022 = f.readlines()

    flux_list_2022 = []
    altitude_list = []

    for i in range(2,len(lines_2022)):
        flux_list_2022.append(float(lines_2022[i][204:214]))
        altitude_list.append(float(lines_2022[i][1:12].strip()))

    flux_list_2036 = []
    with open('MASTER_output_2036.txt', "r") as f:
        lines_2036 = f.readlines()

    for i in range(2,len(lines_2036)):
        flux_list_2036.append(float(lines_2036[i][204:214]))


    plt.plot(altitude_list, flux_list_2022, label="MASTER 2022")
    plt.plot(altitude_list, flux_list_2036, label="MASTER 2036")
    plt.xlabel("Altitude [km]")
    plt.xticks(list(range(200,1300, 100)))
    save_name = "2022_2036_comparison.pdf"

if which_plot=="dec":
    with open('MASTER_output_declination_2036.txt', "r") as f:
        lines_dec_2036 = f.readlines()

    flux_list_dec_2036 = []
    altitude_list_dec = []

    for i in range(2,len(lines_dec_2036)):
        flux_list_dec_2036.append(float(lines_dec_2036[i][204:214]))
        altitude_list_dec.append(float(lines_dec_2036[i][1:12].strip()))
    
    plt.plot(altitude_list_dec, flux_list_dec_2036, label="MASTER 2036")
    plt.xlabel("Declination [°]")
    plt.xticks(list(range(-90, 105, 15)))
    save_name = "2036_declination.pdf"

plt.ylabel("Spatial density [1/km$^3$]")
plt.grid(which="both")
plt.legend()
plt.savefig(save_name, format = "pdf", dpi = 2000, bbox_inches = "tight")
plt.show()

