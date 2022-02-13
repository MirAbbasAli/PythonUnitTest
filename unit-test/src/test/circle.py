'''
Created on Feb 13, 2022

@author: abbas
'''
from math import pi

class Circle:
    def circle_area(self,radius):
        if type(radius) not in [int, float]:
            raise TypeError("Not a non negative real no.")
        if radius<0:
            raise ValueError("The radius cannot be negative")
        return pi*(radius**2)