import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
import numpy as np

a = np.array([[0.8, 2.4, 2.5, 3.9],
              [2.4, 0.0, 4.0, 1.0],
              [1.1, 2.4, 0.8, 4.3],
              [0.6, 0.0, 0.3, 0.0],
              [0.7, 1.7, 0.6, 2.6]])
cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['#ff3d3d', 'yellow', '#74ff52'])
norm = matplotlib.colors.TwoSlopeNorm(vcenter=2.3, vmin=a.min(), vmax=a.max())

fig, ax = plt.subplots()
img = ax.imshow(a, interpolation='none', cmap=cmap, norm=norm)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
plt.colorbar(img, ax=ax)
plt.tight_layout()
plt.show()
