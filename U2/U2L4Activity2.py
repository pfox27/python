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

# This programme asks the user to input a decimal number and then outputs just the decimal portion. 

import math
number1 = float(input("Please enter an integer: "))
number1 = math.fabs(number1)
number1 = number1 - int(number1) 
number2 = float(input("Please enter an integer: "))
number2 = math.fabs(number2)
number2 = number2 - int(number2)
number3 = float(input("Please enter an integer: "))
number3 = math.fabs(number3)
number3 = number3 - int(number3)
print("The minimum value entered is: ", min(number1, number2, number3))






	



