"""
The Watevarr Collision Engine V1.0
by Nicholas Lau
email: nicho.lau95@gmail.com
License: MIT
"""
import math

class point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y

def get_higher_lower(p0,p1):
    if p0.getx() > p1.getx():
        return p0,p1
    else:
        return p1,p0

class point3d(point):
    def __init__(self,x=0,y=0,z=0):
        self.__init__(x,y)
        self.z=z

class line(object):
    def __init__(self,p0,p1):
        self.p0 = p0
        self.p1 = p1
    def getpoints(self, div):
        higher, lower = get_higher_lower(self.p0,self.p1)
        gradient = (higher.gety() - lower.gety()) / (higher.getx() - lower.getx())
        length = math.sqrt((higher.getx() - lower.getx())**2 + (higher.gety() - lower.gety())**2)
        points = []
        for x in range(div):
            points.append(point(lower.getx() + x*(higher.getx() - lower.getx())/div,
                                x * gradient *(higher.getx() - lower.getx())/div + lower.gety()))
        return points

class line3d(line):
    def getpoints(self, div):
        return
        #implement 3d version

class rect(object):
    def __init__(self,p0,p1):
        if p0.getx() < p1.getx():
            self.left = p0.getx()
            self.right = p1.getx()
        else:
            self.left = p1.getx()
            self.right = p0.getx()
        if p0.gety() > p1.gety():
            self.top = p0.gety()
            self.bottom = p1.gety()
        else:
            self.top = p1.gety()
            self.bottom = p0.gety()
    def pointin(self,p):
        x = p.getx()
        y = p.gety()
        if x <= self.right and x >= self.left and y <= self.top and y >= self.bottom:
            return True
        else:
            return False
    def colrect(self,aRect):
        if ((aRect.left > self.left and aRect.left < self.right) or (aRect.right > self.left and aRect.right < self.right)) and ((aRect.top < self.top and aRect.top > self.bottom) or(aRect.bottom < self.top and aRect.bottom > self.bottom)):
            return True
        else:
            return False
    def colline(self,l,div):
        for p in l.getpoints(div):
            #print(str(p.getx())+", "+str(p.gety()))
            if self.pointin(p):
                return True
        return False

if __name__ == "__main__":
    """
    print("Well hello there...")
    print("Testing the engine:")
    aPoint = point(5,5)
    bPoint = point(1,1)
    cPoint = point(9,9)
    aRect = rect(bPoint,cPoint)
    if aRect.pointin(aPoint):
        print("Successful: point in rect")
    else:
        print("Failure: point in rect")
    dPoint = point(-1,3)
    aLine = line(dPoint, aPoint)
    if aRect.colline(aLine, 16):
        print("Successful: line rect collision")
    else:
        print("Failure: line rect collision")"""
