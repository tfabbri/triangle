import triangle
import triangle.plot
import matplotlib.pyplot as plt

box1 = triangle.get_data('bbox.1')
triangle.plot.plot(plt.axes(), **box1)
plt.show()