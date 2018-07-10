import random as rand
from math import sqrt


class Box:

    def __init__(self, index, boxtype, pos=(0, 0, 0)):
        self.index = index
        self.boxtype = boxtype
        self.size = boxtype.size
        self.position = pos
        self.color = boxtype.color

    def __repr__(self):
        string = 'Box no. ' + str(self.index)
        string += '\ntype: ' + self.boxtype.type
        string += '\nsize: ' + str(self.size)
        string += '\nPosition: ' + str(self.position)
        string += '\nColor: ' + str(self.color) + '\n'

        return string


class BoxType:

    def __init__(self, type, benefit, weight, size=(1, 1, 1)):
        self.type = str(type)
        self.size = size
        self.color = [rand.random(), rand.random(), rand.random()]
        self.benefit = benefit
        self.weight = weight
        self.volume = size[0] * size[1] * size[2]
        self.bw = benefit/weight
        self.bv = benefit/self.volume
        self.gm = sqrt(self.bw * self.bv)

    def __repr__(self):
        string = 'Box Type ' + self.type
        string += '\nsize: ' + str(self.size)
        string += '\nbenefit: ' + str(self.benefit)
        string += '\nweight: ' + str(self.weight)
        string += '\nvolume: ' + str(self.volume)
        string += '\nb/w: ' + str(self.bw)
        string += '\nb/v: ' + str(self.bv)
        string += '\nGeometric mean: ' + str(self.gm) + '\n'
        return string


class Bin:

    def __init__(self, size=(200, 1400, 300), name='Main Container'):
        self.name = name
        self.size = size
        self.maxWeight = rand.randint(10, 20) * 100
        self.volume = size[0] * size[1] * size[2]

    def __repr__(self):
        string = 'Container ' + self.name
        string += '\nsize: ' + str(self.size)
        string += '\nMax Weight: ' + str(self.maxWeight)
        string += '\nvolume: ' + str(self.volume) + '\n'
        return string
