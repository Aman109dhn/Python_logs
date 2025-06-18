import math
class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"Vector3D({self.x},{self.y},{self.z})"
    
    def __eq__(self, value):
        if self.x==value.x and self.y==value.y and self.z==value.z:
            return True
        else:
            return False

    def __repr__(self):
        return f"Vector3D(x={self.x},y={self.y},z={self.z})"
    
    def __add__(self,sec):
        return Vector3D(self.x+sec.x,self.y+sec.y,self.z+sec.z)
    
    def __mul__(self,sec):
        if isinstance(sec,Vector3D):
            return self.x*sec.x+self.y*sec.y+self.z*sec.z
        else:
            return Vector3D(self.x*sec,self.y*sec,self.z*sec)
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)


v1 = Vector3D(3,4,5)
v2 = Vector3D(6,7,8)
print(v1)
print(str(v1))
print(repr(v1))
print(v1==v2)
print(v1+v2)
print(v1 * v2) #dot product
print(v1 * 2) #scalar multiplication
print(v2 * 2) #scalar multiplication
print(v1.magnitude())




