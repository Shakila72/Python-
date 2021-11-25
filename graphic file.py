import turtle
turtle.speed(0)
turtle.bgcolor("black")
for i in range(15):
    for colours in ("red", "magenta","blue","cyan","green","yellow","white"):
        turtle.color(colours)
        turtle.pensize(4)
        turtle.left(5)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
