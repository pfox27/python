#!/usr/bin/env python3
#
#  U2L4Activity1.py
#  
#  Copyright 2025 Paul Fox <paulfox@Paul-Fox-MacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# This programme asks the user to input a number and then outputs the sqaure root of that number. 


import math
number = float(input("Please enter a number: "))
absoluteNumber = abs(number)
squareRoot = math.sqrt(absoluteNumber)
print("The final outcome is: ", squareRoot)






	





import sys


def main(args):
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
