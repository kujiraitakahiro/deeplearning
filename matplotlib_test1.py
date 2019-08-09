#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
X = np.arange(-11,11,0.1)
Y1 = np.sin(X)
Y2 = np.cos(X)
plt.plot(X,Y1,label="sin")
plt.plot(X,Y2,linestyle="--",label="cos")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend()
plt.title('sin & cos graphs')
plt.show()
