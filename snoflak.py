from turtle import*

shape("turtle")
shapesize(2)
bgcolor('green')
color('red')
speed(11)

def en(lengde):
    forward(lengde)


def to(lengde):
    en(lengde/3)
    left(60)
    en(lengde/3)
    right(120)
    en(lengde/3)
    left(60)
    en(lengde/3)

def tre(lengde):
    to(lengde/3)
    left(60)
    to(lengde/3)
    right(120)
    to(lengde/3)
    left(60)
    to(lengde/3)

def fjell(lengde,dybde):
    if dybde ==1:
        forward(lengde)
        return

    fjell(lengde/3,dybde-1)
    left(60)
    fjell(lengde/3,dybde-1)
    right(120)
    fjell(lengde/3,dybde-1)
    left(60)
    fjell(lengde/3,dybde-1)

def snoflak(lengde,dybde):
    for i in range(3):
        fjell(lengde,dybde)
        right(120)

snoflak(270,6)


