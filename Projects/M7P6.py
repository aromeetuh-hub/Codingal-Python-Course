import turtle
screen = turtle.Screen()
screen.bgcolor = ("black")
screen.title = "Spiral turtle"

board = turtle.Turtle()
board.speed=("Fatest")
board.hideturtle()

colors = ["red", "pink", "orange", "gold", "green", "blue", "silver", "cyan"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)

board.penup
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(25):
    board .forward(130)
    board.right(144)
board.end_fill()


