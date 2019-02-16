import turtle
import random

class Paddle(turtle.Turtle):
    def __init__(self, xcor, ycor=0, shape="square", color="white"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=10, stretch_len=2)
        self.shape(shape)
        self.color(color)
        self.setx(xcor)

    def move_vertical(self, dy):
        self.sety(self.ycor() + dy)

    def up(self):
        self.move_vertical(60)

    def down(self):
        self.move_vertical(-60)

class Ball(turtle.Turtle):
    def __init__(self, shape="circle", color="white"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.shape(shape)
        self.color(color)
        self.setheading(random.randrange(0,360))
    
    def reset(self):
        self.goto(0,0)        
        self.setheading(random.randrange(0,360))


wn = turtle.Screen()
wn.title("Kai's Pong")
wn.bgcolor("black")
wn.setup(width=1600, height=1200)
wn.tracer(0)

# Paddle A
paddle_a = Paddle(-750)

# Paddle B
paddle_b = Paddle(750)

print(paddle_a.shapesize())

# Ball
ball = Ball()
#TODO Score/ Player display

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

speed = 1
# Main game loop
while True:
    wn.update()

    # move the ball
    ball.forward(speed)
    # check border
    if ball.ycor() > 580:
        ball.sety = 580
        dir = ball.heading()
        ball.setheading(360 - dir)
    elif ball.ycor() < -580:
        ball.sety = -580
        dir = ball.heading()
        ball.setheading(360 - dir)
    elif ball.xcor() > 800:
        ball.reset()
        # Player 1 scores
        # increase speed
        speed *= 1.05
    elif ball.xcor() < -800:
        ball.reset()
        # Player 2 scores
        # increase speed
        speed *= 1.05
    # check paddle A
    if paddle_a.xcor() - 20 < ball.xcor() < paddle_a.xcor() + 20:
        if paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
            ball.setx = -700
            ball.setheading(180 - ball.heading())
    # TODO check size of paddles
    if paddle_b.xcor() - 20 < ball.xcor() < paddle_b.xcor() + 20:
        if paddle_b.ycor() - 80 < ball.ycor() < paddle_b.ycor() + 80:
            ball.setx = 700
            ball.setheading(180 - ball.heading())



