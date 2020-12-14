import numpy as np
num=90
with open('./02PWM/Duty'+str(num)+'.csv', "r") as f:
    csv = f.read()
    csv_line = csv.splitlines()[1:]
    with open("temp.csv", "w") as temp:
        for line_ in csv_line:
            temp.writelines(line_+"\n")
data = np.loadtxt("temp.csv", delimiter=",").T
T=[]
if data[1][0]>1.5:
    flg=True
else:
    flg=False
nflag=False
for i in range(len(data[1])):
    if flg==True:
        if data[1][i]<0.01:
            if not (nflag):
                T.append(data[0][i])
                nflag=True
        if data[1][i]>3.00:
            if nflag:
                T.append(data[0][i])
                nflag=False
    if not flg:
        if data[1][i] > 3.00:
            if not (nflag):
                T.append(data[0][i])
                nflag = True
        if data[1][i] < 0.01:
            if nflag:
                T.append(data[0][i])
                nflag = False
T_div=np.array(np.diff(T)-0.01)
print(T_div)
