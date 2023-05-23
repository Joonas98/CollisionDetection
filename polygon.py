import matplotlib.pyplot as plt
import math as math
from vector import *
from line import *
from collision import *
from constants import *

class Polygon:
    def __init__(self, cm, verteces, mass, speed, rotation, omega, rotational_inertia):
        self.m = mass
        self.cm = cm
        self.verteces = verteces
        self.speed = speed
        self.omega = omega
        self.rotate(rotation)
        self.j = rotational_inertia
        self.collided = False
    def getVertecesInGlobalSpace(self):
        verteces = []
        for v in self.verteces:
            verteces.append(self.cm + v)
        return verteces
    def getEdges(self):
        edges = []
        for i in range(len(self.verteces)):
            edges.append(self.verteces[i]*(-1) + self.verteces[(i + 1) % len(self.verteces)])
        return edges
    def draw(self):
        x_list = []
        y_list = []
        global_space_verteces = self.getVertecesInGlobalSpace()
        for v in global_space_verteces:
            x_list.append(v.x)
            y_list.append(v.y)
        x_list.append(global_space_verteces[0].x)
        y_list.append(global_space_verteces[0].y)
        plt.plot(x_list, y_list)
    def rotate(self, rotation):
        for v in self.verteces:
            x_start = v.x
            y_start = v.y
            v.x = x_start * math.cos(rotation) - y_start * math.sin(rotation)
            v.y = x_start * math.sin(rotation) + y_start * math.cos(rotation)            
    def update(self):
        # Nopeus
        if (self.collided):
            self.collided = False
        else:
            # Laske painovoiman vaikutus nopeuteen
            self.speed.y = self.speed.y - self.m * g * dt
        
        # Rotaatio
        d_rotation = self.omega * dt
        self.rotate(d_rotation)

        # Paikka
        self.cm = self.cm + self.speed * dt




