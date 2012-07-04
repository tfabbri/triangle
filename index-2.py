from triangle.plot import plot
from numpy import *
import matplotlib.pyplot as plt

pts = array(((0,0), (1,0), (1, 1), (0, 1)))
plot(plt, pts, maxarea=0.1)
plt.show()