import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from intersect import intersection

df = pd.read_csv("SENTINEL3A/SENTINEL3A_newSSN_pop_2022.csv")
plt.plot(df["acpl"], df["f_rem_risk"])
plt.plot(df["acpl"], df["f_res_risk"])
plt.xscale("log")
plt.show()