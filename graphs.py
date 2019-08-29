import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, .25*np.pi)
y = np.sin(x)
z = np.cos(x)
zero = [0 for i in range(len(x))]

plt.title('One Period Trig Functions Plot')
plt.plot(x,y)
plt.plot(x,z)
plt.hlines(y = 0, xmin=0, xmax=2*np.pi, linestyles='--')
plt.show()