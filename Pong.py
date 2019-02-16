import turtle

class Paddle(turtle.Turtle):
    def __init__(self, xcor, shape="square", color="white"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.shape(shape)
        self.color(color)
        self.setx(xcor)

    def move_vertical(self, dy):
        self.sety(self.ycor() + dy)

    def up(self):
        self.move_vertical(40)

    def down(self):
        self.move_vertical(-40)


wn = turtle.Screen()
wn.title("Kai's Pong")
wn.bgcolor("black")
# custom dimensions for 4k screen
wn.setup(width=1600, height=1200)
wn.tracer(0)

# Paddle A
#initialize turtle
paddle_a = Paddle(-700)

# Paddle B
paddle_b = Paddle(700)


#Ball
ball = turtle.Turtle()

ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()

wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.up, "Down")

# Main game loop
while True:
    
    wn.update()