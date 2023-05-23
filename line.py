import matplotlib.pyplot as plt
import math as math
from vector import *

class Line:
    def __init__(self, start, end):
        if(start.x < end.x):
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
    def draw(self):
        x_list = [self.start.x, self.end.x]
        y_list = [self.start.y, self.end.y]
        plt.plot(x_list, y_list)
    def slope(self):
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
    def asVector(self):
        return self.end - self.start
    def getUnitNormal(self):   
        return self.asVector().getUnitNormalLeft()

def isPointBelowLine(v, line):
    # Vertex x position is between line min and max x values
    if (line.start.x <= v.x and v.x <= line.end.x):
        # Is below slope/line
        # We must first calculate the point where the line cuts y axis
        line_cut_y_axis = line.slope() * (-line.start.x) + line.start.y
        if (v.y < line.slope() * v.x + line_cut_y_axis):
            return True
    return False
