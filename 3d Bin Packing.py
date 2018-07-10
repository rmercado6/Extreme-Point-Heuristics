import graph
from Classes import BoxType, Box, Bin, ExtremePoint
from Entrada import entrada
import math

entrada = entrada()

# bin = Bin(size=(2.5, 2.5, 2.5))
# bin = Bin()
bin = entrada[0]
print(bin)
weight = 0
volume = 0

boxtypes = entrada[1]
maxboxes = []
boxes = []
nboxes = entrada[2]
to_graph_boxes = []
eps = [(0, 0, 0)]

maxv = bin.volume
maxw = bin.maxWeight


# boxtypes.append(BoxType('A', 100, rand.randint(20, 30), (1, 0.75, 0.25)))
# nboxes.append(20)
# boxtypes.append(BoxType('B', 10, rand.randint(20, 30), (1, 1, 1)))
# nboxes.append(9)
# boxtypes.append(BoxType('C', 5600000, rand.randint(5, 10), (0.25, 0.25, 1.25)))
# nboxes.append(30)

sorted_box_types = sorted(boxtypes, key=lambda boxtype: boxtype.gm, reverse=True)

for box_type in boxtypes:
    nmaxw = math.floor(bin.maxWeight/box_type.weight)
    nmaxv = math.floor(bin.volume/box_type.volume)
    if nmaxw > nmaxv:
        maxboxes.append(nmaxv)
    else:
        maxboxes.append(nmaxw)
    maxv -= box_type.volume * maxboxes[-1]
    maxw -= box_type.weight * maxboxes[-1]

numberbox = {}

for sorted_box_type in sorted_box_types:
    numberbox[sorted_box_type.type] = 0

for sorted_box_type in sorted_box_types:
    for i in range(len(boxtypes)):
        if sorted_box_type.type == boxtypes[i].type:
            for j in range(nboxes[i]):
                volume = 0
                weight = 0
                if j <= maxboxes[i] and volume + sorted_box_type.volume <= bin.volume and weight + sorted_box_type.weight <= bin.maxWeight:
                    boxes.append(Box(sorted_box_type.type + ' - ' + str(j + 1), boxtypes[i]))
                    volume += sorted_box_type.volume
                    weight += sorted_box_type.weight
                    numberbox[sorted_box_type.type] += 1
                else:
                    break
print(boxtypes)

volume = 0
weight = 0

# for nbox in numberbox:
#     print(str(nbox) + ': ' + str(numberbox[nbox]))

boxes = sorted(boxes, key=lambda box: box.boxtype.volume, reverse=True )

# print(nboxes)

plotted = False

for box in boxes:

    eps = sorted(eps, key=lambda ep: (ep[0], ep[2], ep[1]))

    if weight + box.boxtype.weight <= bin.maxWeight and volume + box.boxtype.volume <= bin.volume:

        plotted = False

        for ep in eps:

            size_condition = False

            for ep2 in eps:
                if ep2 != ep:
                    if ep[1] == ep2[1] and ep[2] == ep2[2]:
                        if ep[0] + box.size[0] > ep2[0]:
                            size_condition = True
                            break
                    elif ep[0] == ep2[0] and ep[2] == ep2[2]:
                        if ep[1] + box.size[1] > ep2[1]:
                            size_condition = True
                            break

            if ep[0] + box.size[0] <= bin.size[0] and \
                ep[2] + box.size[2] <= bin.size[2] and \
                ep[1] + box.size[1] <= bin.size[1] and not size_condition:
                box.position = ep

                n = eps.count((ep[0] + box.size[0], ep[1] + box.size[1], ep[2] + box.size[2]))

                if eps.count((ep[0] + box.size[0], ep[1] + box.size[1], ep[2] + box.size[2])) < 1:
                    eps.append((ep[0] + box.size[0], ep[1] + box.size[1], ep[2] + box.size[2]))
                else:
                    eps.remove((ep[0] + box.size[0], ep[1] + box.size[1], ep[2] + box.size[2]))

                if eps.count((ep[0] + box.size[0], ep[1], ep[2])) < 1:
                    eps.append((ep[0] + box.size[0], ep[1], ep[2]))
                else:
                    eps.remove((ep[0] + box.size[0], ep[1], ep[2]))

                if eps.count((ep[0] + box.size[0], ep[1] + box.size[1], ep[2])) < 1:
                    eps.append((ep[0] + box.size[0], ep[1] + box.size[1], ep[2]))
                else:
                    eps.remove((ep[0] + box.size[0], ep[1] + box.size[1], ep[2]))

                if eps.count((ep[0] + box.size[0], ep[1], ep[2] + box.size[2])) < 1:
                    eps.append((ep[0] + box.size[0], ep[1], ep[2] + box.size[2]))
                else:
                    eps.remove((ep[0] + box.size[0], ep[1], ep[2] + box.size[2]))

                if eps.count((ep[0], ep[1] + box.size[1], ep[2] + box.size[2])) < 1:
                    eps.append((ep[0], ep[1] + box.size[1], ep[2] + box.size[2]))
                else:
                    eps.remove((ep[0], ep[1] + box.size[1], ep[2] + box.size[2]))

                if eps.count((ep[0], ep[1], ep[2] + box.size[2])) < 1:
                    eps.append((ep[0], ep[1], ep[2] + box.size[2]))
                else:
                    eps.remove((ep[0], ep[1], ep[2] + box.size[2]))

                if eps.count((ep[0], ep[1] + box.size[1], ep[2])) < 1:
                    eps.append((ep[0], ep[1] + box.size[1], ep[2]))
                else:
                    eps.remove((ep[0], ep[1] + box.size[1], ep[2]))

                eps.remove(ep)

                weight += box.boxtype.weight
                volume += box.boxtype.volume
                to_graph_boxes.append(box)
                # graph.plotBoxes(to_graph_boxes, bin)
                plotted = True
            if plotted: break

graph.plotBoxes(to_graph_boxes, bin)
print('weight: ' + str(weight) + '/' + str(bin.maxWeight))
print('volume: ' + str(volume) + '/' + str(bin.volume))


