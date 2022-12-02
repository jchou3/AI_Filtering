import numpy as np
import matplotlib.pyplot as plt

data = np.array(
    [[.0013158, .013158, .025],
    [.02368, .236842, .45],
    [.23684, 0, .013158]], np.float32
)

# plt.ion()

fig = plt.imshow(data, cmap = 'autumn', interpolation = 'none', aspect = 'equal')
plt.title("Heat Map")

plt.draw()
plt.pause(2)

data2 = np.array(
    [
        [0, .0001, .002],
        [.002, .04, .697],
        [.249, 0, .00077]
    ]
)

# plt.imshow(data2, cmap = 'autumn', interpolation = 'none', aspect = 'equal')

fig.set_data(data2)
plt.draw()
plt.pause(2)


data3 = np.array(
    [
        [0, 0, 0],
        [0, .004, .006],
        [.02, 0, .96]
    ]
)

fig.set_data(data3)
plt.draw()
plt.pause(2)

data4 = np.array(
    [
        [0, 0, 0],
        [0, .0002, 0],
        [.0012, 0, .99]
    ]
)

fig.set_data(data4)
plt.show()

# plt.show()
