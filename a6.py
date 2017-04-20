import pandas as pd
from pylab import *
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("husl")
sns.set()

#pandas reads throughput.csv 
df=pd.read_csv("mm.csv")
u1=df['U'].values.tolist()
rt1=df['R'].values.tolist()
plt.xlabel("Utilization")
plt.ylabel("Response Time")
plt.title("c * M/M/1 Queue")
plt.plot(u1, rt1)
fig = plt.gcf()
plt.show()

df1=pd.read_csv("mmc.csv")
u2=df1['U'].values.tolist()
rt2=df1['R'].values.tolist()
plt.xlabel("Utilization")
plt.ylabel("Response Time")
plt.title("M/M/c Queue")
plt.plot(u2, rt2)
fig = plt.gcf()
plt.show()