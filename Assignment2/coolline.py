import numpy as np
import matplotlib.pyplot as plt

x = np.arange (0., 10.0, .2)

plt.plot(x, x**2 + x*2+ 2, "g--")
plt.plot(x, x**3, "r^")
plt.plot(x, x*4 -3, "b")
plt.xlabel("My Inputs")
plt.ylabel("My Outputs")
plt.title("Best Graph")
plt.show()