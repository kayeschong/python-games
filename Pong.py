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
        self.move_vertical(80)

    def down(self):
        self.move_vertical(-80)


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
        self.setheading(random.randrange(-60, 60) + random.randrange(0, 1) * 90)


wn = turtle.Screen()
wn.title("Kai's Pong")
wn.bgcolor("black")
# Scale for 4k screen
wn.setup(width=1600, height=1200)
wn.tracer(0)

# Paddle A
paddle_a = Paddle(-750)

# Paddle B
paddle_b = Paddle(750)

print(paddle_a.shapesize())

# Ball
ball = Ball()
# TODO Score/ Player display

# Enable paddle movements
wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.down, "Down")

# bonus cheats, mouse left, middle, right click/ drag controls objects

wn.onscreenclick(ball.goto, 2)
paddle_a.ondrag(paddle_a.goto)
paddle_b.ondrag(paddle_b.goto, 3)

# Game variables
height = wn.window_height()
width = wn.window_width()
left_border = -width//2
right_border = width//2
top_border = height//2
bottom_border = -height//2


speed = 10
# Main game loop

while True:
    wn.update()
    time.sleep(0.015)
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
        # increase speed
        speed *= 1.02
    elif ball.xcor() < left_border:
        ball.reset()
        # Player 2 scores
        # increase speed
        speed *= 1.02
    # check paddle A

    paddle_a.color("white")
    paddle_b.color("white")
    if paddle_a.ycor() - 110 < ball.ycor() < paddle_a.ycor() + 110:
        if paddle_a.xcor() + 20 < ball.xcor() < paddle_a.xcor() + 30:  # if hit front
            paddle_a.color("red")
            ball.setx = int(paddle_a.xcor()) + 50
            ball.setheading(180 - ball.heading())
            speed *= 1.01
        elif paddle_a.xcor() - 30 < ball.xcor() < paddle_a.xcor() - 20:  # if hit back
            paddle_a.color("red")
            ball.setx = int(paddle_a.xcor()) - 50
            ball.setheading(180 - ball.heading())
        elif paddle_a.xcor() - 20 < ball.xcor() < paddle_a.xcor() + 20:  # if hit verticals
            paddle_a.color("red")
            ball.setx = int(paddle_a.xcor())
            ball.setheading(360 - ball.heading())
    # TODO check size of paddles

    if paddle_b.ycor() - 110 < ball.ycor() < paddle_b.ycor() + 110:
        if paddle_b.xcor() - 30 < ball.xcor() < paddle_b.xcor() - 20:
            paddle_b.color("red")
            ball.setx = int(paddle_b.xcor()) - 50
            ball.setheading(180 - ball.heading())
            speed *= 1.01
        elif paddle_b.xcor() + 20 < ball.xcor() < paddle_b.xcor() + 30:
            paddle_b.color("red")
            ball.setx = int(paddle_b.xcor()) + 50
            ball.setheading(180 - ball.heading())
        elif paddle_b.xcor() -20 < ball.xcor() < paddle_b.xcor() + 20:
            paddle_b.color("red")
            ball.setx = int(paddle_b.xcor())
            ball.setheading(360 - ball.heading())
