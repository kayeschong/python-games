import turtle
import random
import time


class Paddle(turtle.Turtle):
    def __init__(self, xcor, ycor=0, shape="square", color="white"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=10, stretch_len=2)
        self.shape(shape)
        self.color(color)
        self.setx(xcor)
        self.sety(ycor)

    def move_vertical(self, dy):
        self.sety(self.ycor() + dy)

    def up(self):
        self.move_vertical(100)

    def down(self):
        self.move_vertical(-100)


class Ball(turtle.Turtle):
    def __init__(self, shape="circle", color="white"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.shape(shape)
        self.color(color)
        self.setheading(random.randrange(0, 360))

    def reset(self):
        self.goto(0, 0)
        self.setheading(random.randrange(-60, 60) + random.randrange(0, 2) * 180)


wn = turtle.Screen()
wn.title("Kai's Pong")
wn.bgcolor("black")
# Scale for 4k screen
wn.setup(width=1600, height=1200)
wn.tracer(0)

# Paddles
paddle_a = Paddle(-750)
paddle_b = Paddle(750)

# Ball
ball = Ball()

# useful variables
height = wn.window_height()
width = wn.window_width()
left_border = -width // 2
right_border = width // 2
top_border = height // 2
bottom_border = -height // 2
width_a = paddle_a.shapesize()[0] * 20
length_a = paddle_a.shapesize()[1] * 20
width_b = paddle_b.shapesize()[0] * 20
length_b = paddle_b.shapesize()[1] * 20

score_a = 0
score_b = 0

# Player Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 0.4 * height)
scoreboard.write("Player A: {0}    Player B: {1}".format(score_a, score_b), align="center",
                 font=("Arial", 24, "normal"))

# Enable paddle movements
wn.listen()


def a_up():
    if paddle_a.ycor() + width_a / 2 < height / 2:
        paddle_a.up()


def a_down():
    if paddle_a.ycor() - width_a / 2 > -height / 2:
        paddle_a.down()


def b_up():
    if paddle_b.ycor() + width_b / 2 < height / 2:
        paddle_b.up()


def b_down():
    if paddle_b.ycor() - width_b / 2 > -height / 2:
        paddle_b.down()


wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")

# bonus cheats, mouse left, middle, right click/ drag controls objects

wn.onscreenclick(ball.goto, 2)
paddle_a.ondrag(paddle_a.goto)
paddle_b.ondrag(paddle_b.goto, 3)

# Game variables

flash_color = "red"
speed = 10
# Main game loop

while True:
    wn.update()
    time.sleep(0.012)
    angle = ball.heading()

    # move the ball
    ball.forward(speed)

    # check 90 degrees

    # check border
    if ball.ycor() > top_border - 20:
        ball.sety = top_border - 20
        ball.setheading(360 - angle)
    elif ball.ycor() < bottom_border + 20:
        ball.sety = bottom_border + 20
        ball.setheading(360 - angle)
    elif ball.xcor() > right_border:
        ball.reset()
        # Player 1 scores
        score_a += 1
        scoreboard.clear()
        scoreboard.write("Player A: {0}    Player B: {1}".format(score_a, score_b), align="center",
                         font=("Arial", 24, "normal"))
        # increase speed
        speed += 0.1
    elif ball.xcor() < left_border:
        ball.reset()
        # Player 2 scores
        score_b += 1
        scoreboard.clear()
        scoreboard.write("Player A: {0}    Player B: {1}".format(score_a, score_b), align="center",
                         font=("Arial", 24, "normal"))
        # increase speed
        speed += 0.1
    # check paddle A

    paddle_a.color("white")
    paddle_b.color("white")
    if paddle_a.ycor() - width_a / 2 - 10 < ball.ycor() < paddle_a.ycor() + width_a / 2 + 10:
        if paddle_a.xcor() + 10 < ball.xcor() < paddle_a.xcor() + 30:  # if hit front
            paddle_a.color(flash_color)
            ball.setx = int(paddle_a.xcor()) + 60
            ball.setheading(180 - ball.heading())
            speed += 0.05
        elif paddle_a.xcor() - 30 < ball.xcor() < paddle_a.xcor() + 10:  # if hit verticals
            paddle_a.color(flash_color)
            ball.setx = int(paddle_a.xcor())
            ball.setheading(360 - ball.heading())

    if paddle_b.ycor() - width_b / 2 - 10 < ball.ycor() < paddle_b.ycor() + width_b / 2 + 10:
        if paddle_b.xcor() - 30 < ball.xcor() < paddle_b.xcor() - 10:
            paddle_b.color(flash_color)
            ball.setx = int(paddle_b.xcor()) - 60
            ball.setheading(180 - ball.heading())
            speed += 0.05
        elif paddle_b.xcor() - 10 < ball.xcor() < paddle_b.xcor() + 30:
            paddle_b.color(flash_color)
            ball.setx = int(paddle_b.xcor())
            ball.setheading(360 - ball.heading())
