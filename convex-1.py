import triangle
import triangle.plot
from numpy import *
import matplotlib.pyplot as plt

face = triangle.get_data('face.1')
triangle.plot.plot(plt.axes(), **face)
plt.show()