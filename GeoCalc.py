# GeoCalc - A programme that calculates areas and volumes of geometrical shapes

import math
shape = 10

while (shape !=1 and shape !=2 and shape !=3 and shape !=4 and shape !=5 and shape !=6):

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
	if (shape !=1 and shape !=2 and shape !=3 and shape !=4 and shape !=5 and shape !=6):
		print ('You have not entered a valid choice, please choose an integer between 1 and 6 inclusive.')

#float pi = 3.1415927

if shape == 1:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            length = float(input ('Please enter the length of the side of the cube in metres:'))
            area = length * length * 6
            print ('The surface area of the cube is ', area, ' m^2')
        else:
            length = float(input ('Please enter the length of the side of the cube in metres:'))
            volume = length * length * length
            print ('The volume of the cube is ', volume, ' m^3')

elif shape == 2:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            radius = float(input ('Please enter the radius of the sphere in metres:'))
            area = 4 * math.pi * radius**2
            print ('The surface area of the sphere is ', area, ' m^2')
        else:
            radius = float(input ('Please enter the radius of the sphere in metres:'))
            volume = 4/3 * math.pi * radius**3
            print ('The volume of the sphere is ', volume, ' m^3')

elif shape == 3:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            h = float(input ('Please enter the height of the rectangular pyramid in metres:'))
            w = float(input ('Please enter the width of the base of the rectangular pyramid in metres:'))
            l = float(input ('Please enter the length of the base of the rectangular pyramid in metres:'))

            area = l * w + w*math.sqrt(h**2 + l**2/4) + l*math.sqrt(h**2 + w**2/4)
            print ('The surface area of the rectangular pyramid is ', area, ' m^2')
        else:
            h = float(input ('Please enter the height of the rectangular pyramid in metres:'))
            w = float(input ('Please enter the width of the base of the rectangular pyramid in metres:'))
            l = float(input ('Please enter the length of the base of the rectangular pyramid in metres:'))
            volume = 1/3 * l * w * h
            print ('The volume of the rectangular pyramid is ', volume, ' m^3')

elif shape == 4:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            h = float(input ('Please enter the height of the rectangular prism in metres:'))
            w = float(input ('Please enter the width of the rectangular prism in metres:'))
            l = float(input ('Please enter the length of the rectangular prism in metres:'))

            area = h * l * 4 + w * h * 2
            print ('The surface area of the rectangular prism is ', area, ' m^2')
        else:
            h = float(input ('Please enter the height of the rectangular prism in metres:'))
            w = float(input ('Please enter the width of the rectangular prism in metres:'))
            l = float(input ('Please enter the length of the rectangular prism in metres:'))
            volume = l * w * h
            print ('The volume of the rectangular prism is ', volume, ' m^3')

elif shape == 5:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            h = float(input ('Please enter the height of the triangular prism in metres:'))
            w = float(input ('Please enter the width of the base of the triangular prism in metres:'))
            l = float(input ('Please enter the length of the base of the triangular prism in metres:'))

            area = w * h + 3 * (l * math.sqrt(h**2 + w**2/4))
            print ('The surface area of the triangular prism is ', area, ' m^2')
        else:
            h = float(input ('Please enter the height of the triangular prism in metres:'))
            w = float(input ('Please enter the width of the base of the triangular prism in metres:'))
            l = float(input ('Please enter the length of the base of the triangular prism in metres:'))
            volume = 1/2 * w * h * l
            print ('The volume of the triangular prism is ', volume, ' m^3')

elif shape == 6:
        print ('Please enter the type of calculation desired:')
        print ('1. Area')
        print ('2. Volume')
        calc = int(input())
        if calc == 1:
            h = float(input ('Please enter the height of the cone in metres:'))
            r = float(input ('Please enter the radius of the base of the cone in metres:'))

            area = math.pi * r**2 + math.pi * r * math.sqrt(h**2 + r**2)

            print ('The surface area of the cone is ', area, ' m^2')
        else:
            h = float(input ('Please enter the height of the cone in metres:'))
            r = float(input ('Please enter the radius of the base of the cone in metres:'))
         
            volume = 1/3 * math.pi * r**2 * h
            print ('The volume of the cone is ', volume, ' m^3')




