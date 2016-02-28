from turtle import*

shape('turtle')
shapesize(2)
bgcolor('green')
color('red')
speed(11)

def trekant(lengde,dybde):
    if dybde<=1:
        pendown()
        for i in range(3):
            forward(lengde)
            left(120)
        penup()
        return

    trekant(lengde/2,dybde-1)
    forward(lengde/2)
    trekant(lengde/2,dybde-1)
    left(120)
    forward(lengde/2)
    right(120)
    trekant(lengde/2,dybde-1)
    right(120)
    forward(lengde/2)
    left(120)

trekant(270,10)
