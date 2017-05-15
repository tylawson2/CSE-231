import math
class Vector(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def __str__(self):
        returnstr = "vector. x value: {:.2f}, y value: {:.2f}".format(self.__x, self.__y)
        return returnstr
    def __repr__(self):
        returnstr = "vector. x value: {:.2f}, y value: {:.2f}".format(self.__x, self.__y)
        return returnstr
    def __add__(self, vector):
        add = Vector(self.__x + vector.__x, self.__y + vector.__y)
        return add
    def __sub__(self, vector):
        sub = Vector(self.__x - vector.__x, self.__y - vector.__y)
        return sub
    def __mul__(self, something):
        if type(something) == float or type(something) == int:
            mult = Vector(self.__x*something, self.__y*something)
        else:
            mult = (self.__x*something.__x)+(self.__y*something.__y)
        return mult
    def __rmul__(self, something):
        if type(something) == float or type(something) == int:
            mult = Vector(self.__x*something, self.__y*something)
        else:
            mult = (self.__x*something.__x)+(self.__y*something.__y)
        return mult
    def __eq__(self, vector):
        same = False
        if self.__x == vector.__x and self.__y == vector.__y:
            same = True
        return same
    def magnitude(self):
        return math.hypot(self.__x, self.__y)
    def unit(self):
        if self.magnitude() == 0:
            raise ValueError("cannot convert zero magniture vector to a unit vector")
        #mag = self.__mul__(1/self.magnitude())
        ang = math.acos(self.__x/self.magnitude())
        self.__x = math.cos(ang)
        self.__y = math.sin(ang)

a = Vector(1, 1)
print(a)
a.unit()
print(a)

a = Vector(1,1)
print(a)

b = a + a
print(b)

f = a - a
print(f)

c = a * 2
d = 2 * c
print(c)  
print(d)

e = c * d
print(e)

print(a.magnitude())

f.unit()
print(f)