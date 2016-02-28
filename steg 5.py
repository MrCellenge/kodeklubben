from turtle import*
speed(1)
shape("turtle")

def dashforward(length):
  for num in range(8):
    forward(length/16)
    penup()
    forward(length/16)
    pendown()

def dashpoly(sides,length):
    angle=360/sides

    for n in range(sides):
        dashforward(length)
        right(angle)

pencolor('red')
dashpoly(4,100)
right(180)
pencolor('blue')
dashpoly(3,150)
