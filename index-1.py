import triangle
import triangle.plot
import matplotlib.pyplot as plt
import numpy as np
pts = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
segments = triangle.convex_hull(pts)
triangle.plot.plot(plt.axes(), vertices=pts, segments=segments)
plt.show()