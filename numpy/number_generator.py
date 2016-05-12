# This script shows you how to generate numbers e.g. for grid search cross
# validation parameter tuning

import matplotlib.pyplot as plt
import numpy as np

start = 0
end = 10
# Gives you 50 numbers from 1 to 1000 evenly spaced in a log scale
numbers0 = np.logspace(start, end)

# gives you 13 numbers from 0.01 to 1000 evenly spaced in a log scale
numbers1 = np.logspace(-2, 10, 13)

plt.plot(numbers0)
plt.plot(numbers1)
plt.show()
