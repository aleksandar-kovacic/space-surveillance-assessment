"""import numpy as np

R = 6378.137
h_pi = [350, 550, 800, 2000, 25000]
e = [0.1, 0.9]


for j in range(len(h_pi)):
    sma_list = []
    for i in range(len(e)):
        a = (h_pi[j] + R)/(1-e[i])
        sma_list.append(int(round(a,0)))
    print("hp1 ≤ "+ str(h_pi[j]) + "    " + str(sma_list[0])+ " ≤ "+ str(sma_list[1]))"""