from turtle import*

def poly(sides,length):
    angle=360/sides

    for n in range(sides):
        forward(length)
        right(angle)

pencolor('red')
poly(4,100)
right(180)
pencolor('blue')
poly(3,150)
