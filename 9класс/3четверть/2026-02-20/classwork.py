import numpy as np
import matplotlib.pyplot as plt


xarr = []
yarr = []
a = 0
b = 0
n = 0
while a != 1488 and b != 1488:
    xarr.append(a)
    yarr.append(b)
    n+=1
    str =input()
    a = int(str.split(";")[0])
    b= int(str.split(";")[1])

print(xarr)
print(yarr)

def l(i, x):
    prod= 1.0
    for j in range(len(xarr)):
        if j!= i:
            prod *= (x-xarr[j])/(xarr[i]-xarr[j])
    return prod
def L(x):
    s = 0.0
    for i in range(len(xarr)):
        s+=yarr[i]*l(i, x)

    return s


x_p = np.linspace(0, 10, 100)
y_p = [L(x) for x in x_p]


# y = np.cos(x)
# y2 = np.sin(x)
#
plt.plot(x_p, y_p)
# plt.plot(x, y2)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
#
#
plt.show()