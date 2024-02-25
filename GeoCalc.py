# GeoCalc - A programme that calculates areas and volumes of geometrical shapes

import math
print ('GeoCalc - Calculate Area or Volume')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('')
print ('Please choose the number for the desired shape:')
print ('1. Cube')
print ('2. Sphere')
print ('3. Rectangular Pyramid')
print ('4. Rectangular Prism')
print ('5. Triangular Prism')
print ('6. Cone')
shape = int(input())
#float pi = 3.1415927

if shape == 1:
    print ('Please enter the type of calculation desired:')
    print ('1. Area')
    print ('2. Volume')
    calc = int(input())
    if calc == 1:
        length = int(input ('Please enter the length of the side of the cube in metres:'))
        area = length * length * 6
        print ('The surface area of the cube is ', area, ' m^2')
    else:
        length = int(input ('Please enter the length of the side of the cube in metres:'))
        volume = length * length * length
        print ('The volume of the cube is ', volume, ' m^3')

if shape == 2:
    print ('Please enter the type of calculation desired:')
    print ('1. Area')
    print ('2. Volume')
    calc = int(input())
    if calc == 1:
        radius = int(input ('Please enter the radius of the sphere in metres:'))
        area = 4 * math.pi * radius**2
        print ('The surface area of the sphere is ', area, ' m^2')
    else:
        radius = int(input ('Please enter the radius of the sphere in metres:'))
        volume = 4/3 * math.pi * radius**3
        print ('The volume of the sphere is ', volume, ' m^3')

if shape == 3:
    print ('Please enter the type of calculation desired:')
    print ('1. Area')
    print ('2. Volume')
    calc = int(input())
    if calc == 1:
        h = int(input ('Please enter the height of the rectangular pyramid in metres:'))
        w = int(input ('Please enter the width of the base of the rectangular pyramid in metres:'))
        l = int(input ('Please enter the length of the base of the rectangular pyramid in metres:'))

        area = l * w + w*math.sqrt(h**2 + l**2/4) + l*math.sqrt(h**2 + w**2/4) 
        print ('The surface area of the rectangular prism is ', area, ' m^2')
    else:
        radius = int(input ('Please enter the radius of the sphere in metres:'))
        volume = 4/3 * math.pi * radius**3
        print ('The volume of the sphere is ', volume, ' m^3')


