# A programme to compute the six trigonometric ratios of an angle given in degrees."

import math
print ("")
degrees = 0.0
radians = 0.0
sin = 0.0
cos = 0.0
tan = 0.0
csc = 0.0
sec = 0.0
cot = 0.0

degrees = float(input("Please enter the angle in degrees:"))
print ("")
print("The angle in degrees is " , degrees)

def trig_ratios(degrees):
    radians = degrees * math.pi / 180.00
    print("The angle in radians is ", radians)
    print("")
    print ("The trigonometric ratios of the angle are:")
    print("")
    sin = math.sin(radians)
    print ("Sine = " , sin)
    cos = math.cos(radians)
    print ("Cosine = " , cos)
    tan = math.tan(radians)
    print ("Tangent = " , tan)
    csc = 1 / sin
    print ("Cosecant = " , csc)
    sec = 1 / cos
    print ("Secant = " , sec)
    cot = 1 / tan
    print ("Cotangent = " , cot)
    
trig_ratios(degrees)    

print("")



