from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Sketch")
screen.tracer(0)

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()