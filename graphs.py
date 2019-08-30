import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, .1)
y = np.sin(x)
z = np.cos(x)
t = np.tan(x)
zero = [0 for i in range(len(x))]

plt.title('One Period Trig Functions Plot')
plt.plot(x,y, label='Sin(x)')
plt.plot(x,z, label='Cos(x)')
plt.plot(x,t, label='Tan(x)')
plt.hlines(y = 0, xmin=0, xmax=2*np.pi, linestyles='--')
plt.legend()
plt.show()
