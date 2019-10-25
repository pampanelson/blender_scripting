import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi,voronoi_plot_2d
import random

arr = []

for i in range(20):
    for j in range(20):
        x = random.random() + i
        y = random.random() + j
        point = [x,y]
        arr.append(point)

points = np.array(arr)
# points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],[2, 0], [2, 1], [2, 2]])
# print(points)
vor = Voronoi(points)




# Mark the Voronoi vertices.
# plt.plot(vor.vertices[:,0], vor.vertices[:, 1], 'ko', ms=8)
print(vor.ridge_vertices)

for vpair in vor.ridge_vertices:
    if vpair[0] >= 0 and vpair[1] >= 0:
        v0 = vor.vertices[vpair[0]]
        v1 = vor.vertices[vpair[1]]
        # Draw a line from v0 to v1.
        plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k', linewidth=2)
        print(str(v0) + " " + str(v1))


# voronoi_plot_2d(vor)
plt.show()