import turtle
def funtime(x, s):
    r = 0
    g = 255
    b = 0
    for i in range(x):
        turtle.colormode(255)
        turtle.color(r,g,b)
        r = r + 1
        g = g - 1
        b = b + 1
        turtle.speed(.1)
        turtle.forward(s)
        turtle.goto (0,0)
        turtle.right(1)
        if r >= 255:
           r = r - 1
        if g <= 0:
           g = g + 1
        if b >= 255:
           b = b - 1 
    for n in range(x):
        
        turtle.forward(s + 30)
        turtle.goto(0,0)
        turtle.left(1)
funtime(360, 100)
