import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import subprocess
from decimal import Decimal, Context
import math
from matplotlib.font_manager import FontProperties

def decimal_normalize(f):
    """数値fの小数点以下を正規化し、文字列で返す"""
    def _remove_exponent(d):
        return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
    a = Decimal.normalize(Decimal(str(f)))
    b = _remove_exponent(a)
    r, i = math.modf(b)
    r = r*10
    r = int(r)
    i = int(i)
    if r == 0:
        return str(b)
    else:
        return str(i)+"_"+str(r)


i=input()
j=input()
k=input()
with subprocess.Popen("シミュレーション.bat", stdin=subprocess.PIPE) as fv:
     fv.communicate((str(i)+"\n"+str(j)+"\n"+str(k)).encode("utf-8"))
     fv.wait()
with open("p"+decimal_normalize(i)+"+i"+decimal_normalize(j)+"+d"+decimal_normalize(k)+".csv", "r") as f:
    csv = f.read()
    csv_line = csv.splitlines()[5:]
    with open("temp.csv", "w") as temp:
        for line_ in csv_line:
            temp.writelines(line_+"\n")
data = np.loadtxt("temp.csv", delimiter=",").T
fig = plt.figure()
plt.grid(True)
#fp = FontProperties(fname=r'C:\WINDOWS\Fonts\msgothic.ttf', size=14)
plt.xlabel("Time [s]")
plt.ylabel("Vertical angle [rad]")

ax = fig.add_subplot(1, 1, 1)
ax.plot(data[0], data[2], color="red",label="response")
ax.plot(data[0], data[1], color="blue",label="target")

plt.savefig("./img/p"+decimal_normalize(i)+"+i" +decimal_normalize(j)+"+d"+decimal_normalize(k)+".png")
os.remove("temp.csv")
