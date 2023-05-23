import matplotlib.pyplot as plt
import math as math
from matplotlib import animation
from matplotlib.patches import Polygon
from vector import *
from line import *
from polygon import *
from collision import *
from constants import *

#Remember to install matplotlib:
#python -m pip install -U matplotlib

stopAtPolygons = True #Stop simulation when polygons collide?
t_max = 5 #Steps = this value * 1000
e = 1
polygons = []
lines = []

#Create polygons
polygons.append(Polygon(Vector(-20,30,0), [Vector(-3,0,0),Vector(0,6,0),Vector(3,0,0)], 1, Vector(0,0,0), 0, pi, 1))
polygons.append(Polygon(Vector(-40,25,0), [Vector(-3,0,0),Vector(0,6,0),Vector(3,0,0)], 1, Vector(20,0,0), 0, pi, 1))

#Create lines to collide with
line1 = Line(Vector(0,-12,0), Vector(50,35,0))
line1.draw()
lines.append(line1)

line2 = Line(Vector(0,-12,0), Vector(-60,20,0))
line2.draw()
lines.append(line2)

print(getPointDistanceFromEdge(Vector(2,3,0), Vector(2,5,0), Vector(7,6,0)))

######################################################################
edges = polygons[0].getEdges()
normals = []
for v in edges:
    normals.append(v.getUnitNormalLeft())
    print(v)

for n in normals:
    print(n)

t = 0
i = 0

while (t < t_max):
    #Collision detection
    for p in polygons:
        for l in lines:
            v = getVertexInCollisionWithLine(p, l)
            if (v != None):
                p.collided = True
                CalculateCollisionWithLine(l, p, v, e)


    if isCollisionPolygon(polygons[0], polygons[1]) and stopAtPolygons is True:
        print(polygons[0].verteces[0], polygons[1].verteces[0])
        print("COLLISION")
        calculatePolygonCollision(polygons[0], polygons[1])
        break

    #Updating polygon transform and speeds            
    for p in polygons:
        p.update()

    #Drawing 
    if (i % 1 == 0):
        for p in polygons:
            p.draw()

            
    i += 1
    t += dt

plt.axis([-50, 50, -50, 50])
plt.show()
