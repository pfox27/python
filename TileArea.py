# This programme takes the dimensions of a room from the user and calculates the number of tiles to be used for the floor.

import os

os.system('clear')

print('')
print('Tile Number Calculator')
print('~~~~~~~~~~~~~~~~~~~~~~')
print('')

import math
length = float(input('Please enter the length of the room, in metres: '))
width = float(input('Please enter the width of the room, in metres: '))

area = length * width
print('The area of the room is ')
print(str(area) + ' m.')


tileSide = float(input('Please enter the length of one side of the square tile to be used: '))


tileArea = tileSide**2

numberOfTiles = area/tileArea

print('The number of tiles needed for the floor entered is ')
print(numberOfTiles)


