import matplotlib.pyplot as plt
import math as math
from vector import *
from line import *
from polygon import *


def getVertexSpeed(local_space_vertex, polygon):
    return polygon.speed + crossP(Vector(0,0,polygon.omega), local_space_vertex)

def getLocalSpaceVertex(global_space_vertex, polygon):
    return global_space_vertex - polygon.cm

def getVDotN(normal, polygon, local_space_vertex):
    vertex_speed = getVertexSpeed(local_space_vertex, polygon)
    return dotP(vertex_speed, normal)

# Oletetaan, että janan alkupisteen x komponentti on pienempi kuin loppuarvon,
# ja kappale törmää janan yläpuolelle
def getVertexInCollisionWithLine(polygon, line):
    global_space_verteces = polygon.getVertecesInGlobalSpace()
    for v in global_space_verteces:
        if (isPointBelowLine(v, line)):
            # v_dot_n < 0
            local_space_vertex = getLocalSpaceVertex(v, polygon)
            #print(getVDotN(line.getUnitNormal(), polygon, local_space_vertex))
            print(getVDotN(line.getUnitNormal(), polygon, local_space_vertex))
            if (getVDotN(line.getUnitNormal(), polygon, local_space_vertex) < 0):
                return v  # Palauta kärkipiste joka on törmännyt
    return None  # Palauta tyhjää jos ei törmäystä

def CalculateCollisionWithLine(line, polygon, global_space_vertex, e):
    # Lasketaan kärkipisteen sijainti paikallisessa avaruudessa
    local_space_vertex = getLocalSpaceVertex(global_space_vertex, polygon)
    
    # Impulssi kaava
    v_dot_n = getVDotN(line.getUnitNormal(), polygon, local_space_vertex)
    inv_m = 1 / polygon.m
    rp_x_n = crossP(local_space_vertex, line.getUnitNormal())
    denominator = inv_m + (rp_x_n.magnitude() ** 2) / polygon.j
    impulse = -(1 + e) * (v_dot_n / denominator)

    # Muuta monikulmion nopeus ja kulmanopeus
    polygon.speed = polygon.speed + line.getUnitNormal() * (impulse / polygon.m)
    polygon.omega = polygon.omega + rp_x_n.z * (impulse / polygon.j)

def isCollisionPolygon(p1, p2):
    edges = p1.getEdges()
    edges.extend(p2.getEdges())

    proj_normals = []
    for v in edges:
        proj_normals.append(v.getUnitNormalLeft())

    global_space_verteces_p1 = p1.getVertecesInGlobalSpace()
    global_space_verteces_p2 = p2.getVertecesInGlobalSpace()

    if (sat(proj_normals, global_space_verteces_p1, global_space_verteces_p2)):
        return True
    else:
        return False

def isOutside(x, a, b):
    return x < a or b < x

def sat(proj_normals, p1_verteces, p2_verteces):
    for n in proj_normals:
        p1_min = dotP(p1_verteces[0], n)
        p1_max = dotP(p1_verteces[0], n)
        for v in p1_verteces:
            x = dotP(v, n)
            if (x < p1_min):
                p1_min = x
            if (p1_max < x):
                p1_max = x
        p2_min = dotP(p2_verteces[0], n)
        p2_max = dotP(p2_verteces[0], n)
        for v in p2_verteces:
            x = dotP(v, n)
            if (x < p2_min):
                p2_min = x
            if (p2_max < x):
                p2_max = x

        if (isOutside(p2_min, p1_min, p1_max) and isOutside(p2_max, p1_min, p1_max)):
            return False
    return True

def isInsidePolygon(v, p_verteces):
    for i in range(len(p_verteces)):
            edge = p_verteces[(i + 1) % len(p_verteces)] - p_verteces[i]
            point = v - p_verteces[i]
            if (crossP(edge, point).z > 0):
                return False
    return True

def getCollidedVertex(p1, p2):
    p1_verteces = p1.getVertecesInGlobalSpace()
    p2_verteces = p2.getVertecesInGlobalSpace()
    for v in p1_verteces:
        if (isInsidePolygon(v, p2_verteces)):
            print("IS INSIDE")
            return v
    return None

def getPointDistanceFromEdge(point, edge_start, edge_end):
    numerator = abs((edge_end.x - edge_start.x) * (point.y - edge_start.y) - (point.x - edge_start.x) * (edge_end.y - edge_start.y))
    denominator = math.sqrt((edge_end.x - edge_start.x) ** 2 + (edge_end.y - edge_start.y) ** 2)
    return numerator / denominator
    

def getCollisionEdgeNormal(point, polygon):
    verteces = polygon.getVertecesInGlobalSpace()
    edge_d = getPointDistanceFromEdge(point, verteces[0], verteces[1])
    edge = verteces[1] - verteces[0]
    for i in range(len(verteces)):
        this_edge_d = getPointDistanceFromEdge(point, verteces[i], verteces[(i + 1) % len(verteces)])
        if (this_edge_d < edge_d):
            edge = verteces[(i + 1) % len(verteces)] - verteces[i]
            edge_d = this_edge_d
    return edge.getUnitNormalLeft()

#def impulseInPolygonCollision

def calculatePolygonCollision(p1, p2):
    poly_a = p1
    poly_b = p2
    point = getCollidedVertex(p1, p2)
    if (point == None):
        print("HERE")
        point = getCollidedVertex(p2, p1)
        poly_a = p2
        poly_b = p1

    print(point)
    edge_normal = getCollisionEdgeNormal(point, poly_b)
    print(edge_normal)

    
        
        
    

    
