import turtle
import time
import random


snake = turtle.Turtle()
snake.shape('square')
wn = turtle.Screen()
wn.setup(600, 600)
wn.title("test")
wn.bgcolor("gold")
wn.title("Snake Game")

border = turtle.Turtle()
border.hideturtle()
border.pensize(5)
border.penup()
border.goto(250,250)
border.pendown()
border.setheading(270)
for i in range(4):
    border.forward(500)
    border.right(90)


def snake_move():
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction == 'Up':
        snake.goto(x+20,y)

    elif snake.direction == 'Up':
        snake.goto(x+20,y)

    elif snake.direction == 'Up':
        snake.goto(x+20,y)

    elif snake.direction == 'Up':
        snake.goto(x+20,y)


while True:
    snake_move()






turtle.done()