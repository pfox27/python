# A programme that uses a function to draw a box with turtle graphics

import turtle
bob = turtle.Turtle()
length = 260.0

def square(t,l):
    print(t)

    for i in range (4):
        t.fd(l)
        t.lt(90)

    turtle.mainloop()

square(bob, length)
