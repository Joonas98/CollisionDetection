import math as math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ']'
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    def getUnitNormalLeft(self):
        return Vector(-self.y / self.magnitude(), self.x / self.magnitude(), 0)
    def getUnitNormalRight(self):
        return Vector(self.y / self.magnitude(), -self.x / self.magnitude(), 0)

def dotP(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def crossP(a, b):
    return Vector(a.y * b.z - b.y * a.z, a.z * b.x - b.z * a.x, a.x * b.y - b.x * a.y)
