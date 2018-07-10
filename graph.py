from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def cuboid_data(o, size=(1, 1, 1)):
    X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
         [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
         [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
         [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
         [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
         [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
    X = np.array(X).astype(float)
    for i in range(3):
        X[:, :, i] *= size[i]
    X += np.array(o)
    return X


def plotCubeAt(positions, sizes=None, colors=None, **kwargs):
    if not isinstance(colors, (list, np.ndarray)): colors = ["C0"] * len(positions)
    if not isinstance(sizes, (list, np.ndarray)): sizes = [(1, 1, 1)] * len(positions)
    g = []
    for p, s, c in zip(positions,sizes,colors):
        g.append(cuboid_data(p, size=s))
    return Poly3DCollection(np.concatenate(g),
                            facecolors=np.repeat(colors, 6, axis=0), **kwargs)


def plot(positions, colors, sizes):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('equal')

    pc = plotCubeAt(positions, sizes, colors=colors, edgecolor="k")
    ax.add_collection3d(pc)

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])

    ax.set(xlabel='x', ylabel='y', zlabel='z')

    plt.show()


def plotBoxes(boxes, bin):
    positions = []
    sizes = []
    colors = []
    patches=[]
    boxtypes = []
    for box in boxes:
        positions.append(box.position)
        sizes.append(box.size)
        colors.append(box.color)
        if box.boxtype not in boxtypes:
            boxtypes.append(box.boxtype)
            patches.append(mpatches.Patch(color=box.color, label='Caja ' + box.boxtype.type))

    positions = np.array(positions)
    sizes = np.array(sizes)
    colors = np.array(colors)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('equal')

    pc = plotCubeAt(positions, sizes, colors=colors, edgecolor="k")
    ax.add_collection3d(pc)

    ax.set_xlim([0, bin.size[0]])
    ax.set_ylim([0, bin.size[1]])
    ax.set_zlim([0, bin.size[2]])

    ax.set(xlabel='x', ylabel='y', zlabel='z')
    ax.set_aspect('auto')

    red_patch = mpatches.Patch(color='red', label='The red data')

    legend = ax.get_legend()
    ax.legend(handles=patches)
    ax.view_init(azim=45)
    plt.show()
    # rotate the axes and update
    # for angle in range(0, 360):
    #     ax.view_init(20, angle)
    #     plt.draw()

