import numpy as np
import matplotlib.pyplot as plt

# 400 evenly spaced x-values from -2pi to 2pi -> makes a smooth curve
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")

plt.title("sin and cos")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()      # shows the little box naming each curve
plt.grid(True)
plt.show()
