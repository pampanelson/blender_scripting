import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi,voronoi_plot_2d
import random

arr = []

for i in range(9):
    x = random.random() + i
    y = random.random() + i
    point = [x,y]
    arr.append(point)

points = np.array(arr)
print(points)
vor = Voronoi(points)


# fig = plt.figure()

# # Mark the Voronoi vertices.
# plt.plot(vor.vertices[:,0], vor.vertices[:, 1], 'ko', ms=8)

# for vpair in vor.ridge_vertices:
#     if vpair[0] >= 0 and vpair[1] >= 0:
#         v0 = vor.vertices[vpair[0]]
#         v1 = vor.vertices[vpair[1]]
#         # Draw a line from v0 to v1.
#         plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k', linewidth=2)


voronoi_plot_2d(vor)
plt.show()