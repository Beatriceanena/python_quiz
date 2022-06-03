import math
#A Circle instance accepts attribute radius (r)
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr

class Circle:
    def __init__(self,r):
        self.r= r

    def area(self,a):
        self.a=a
        A = math.pi* (self.r**2) 
        return A  
    def Circumference(self):
        C= 2* math.pi *self.r
        return C   

# A Square instance accepts the attribute side (a)
#It has method area that returns the area (A) of the square using the formula A=a2
#It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square: 
    def __init__(self,a):
        self.a=a
         
    def area(self):
        A= self.a*self.a
        return A

    def Perimeter(self):
        P= 4*self.a
        return P    


#A Rectangle instance accepts two sides of a rectangle (w,l)
#It has method to calculate the area (A) of the rectangle using the formula A=wl
#It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
         
    
    def area(self):
        A= self.w * self.l
        return A

    def Perimeter(self):
        P= 2*(self.l + self.w)
        return P



            
#A Sphere Instance accepts the radius of the sphere (r)
#It has a method to calculate the surface area (A) using the formula A=4πr2
#It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,r):
        self.r=r

    def surface_area(self):
        A= 4*math.pi*(self.r**2)
        return A

    def volume(self):
        V= 4/3*(math.pi*self.r**3)
        return V

    