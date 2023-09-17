import random
import turtle
import time


screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("CatchTheTurtle")

turtle.mode("logo")

turtle.tracer(0)
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.shape("turtle")
my_turtle.shapesize(2, 2, 2)
my_turtle.penup()

timer = 20
timer_turtle = turtle.Turtle()
timer_turtle.color("blue")
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.setposition(0, 240)
timer_turtle.pendown()
timer_turtle.write(f"TIME = {timer}", move=False, align='left', font=('Arial', 15, 'normal'))

score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.setposition(0, 200)
score_turtle.pendown()
score_turtle.write(f"Score = {score}", move=False, align='left', font=('Arial', 15, 'normal'))


def timer_display():
    timer_turtle.clear()
    timer_turtle.write(f"TIME = {timer}", move=False, align='left', font=('Arial', 15, 'normal'))


def on_click(x, y):
    global score
    score += 1

    score_display()


def score_display():

    score_turtle.clear()
    score_turtle.write(f"Score = {score}", move=False, align='left', font=('Arial', 15, 'normal'))


def move_turtle(x, y):

    my_turtle.goto(x, y)


turtle.tracer(1)

x_positions = [-120, -60, 0, 60, 120]
y_positions = [-120, -60, 0, 60, 120]


while timer >= 0:

    random_number_x = random.randint(0, len(x_positions)-1)
    random_number_y = random.randint(0, len(y_positions)-1)
    random_x = x_positions[random_number_x]
    random_y = y_positions[random_number_y]
    move_turtle(random_x, random_y)

    my_turtle.showturtle()
    time.sleep(0.5)
    my_turtle.onclick(on_click, 1, False)
    my_turtle.hideturtle()
    time.sleep(0.5)

    timer_display()

    timer -= 1

timer_turtle.clear()
timer_turtle.write(timer_turtle.write("GAME OVER!", move=False, align='left', font=('Arial', 15, 'normal')))


screen.mainloop()
