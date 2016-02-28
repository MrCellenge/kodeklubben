from turtle import*
from random import randrange,choice
colors=['red','blue','green','purple','yellow','lime']


def poly(sides,length):
    angle=360/sides

    for n in range(sides):
        forward(length)
        right(angle)

for count in range(10):
    pencolor(choice(colors))
    right(randrange(0,360))
    penup()
    forward(randrange(20,100))
    pendown()
    poly(randrange(3,9),randrange(10,30))
