import turtle

def paddle_move(paddle, dy):
    paddle.sety(paddle.ycor() + dy)


wn = turtle.Screen()
wn.title("Kai's Pong")
wn.bgcolor("black")
# custom dimensions for 4k screen
wn.setup(width=1600, height=1200)
wn.tracer(0)

# Paddle A
#initialize turtle
paddle_a = turtle.Turtle()

paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=10, stretch_len=2)
paddle_a.penup()
paddle_a.goto(-700, 0)

# Paddle A move
def paddle_a_up():
    paddle_move(paddle_a, 40)

def paddle_a_down():
    paddle_move(paddle_a, -40)


# Paddle B
paddle_b = turtle.Turtle()

paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=10, stretch_len=2)
paddle_b.penup()
paddle_b.goto(700, 0)

#Paddle B move
def paddle_b_up():
    paddle_move(paddle_b, 40)

def paddle_b_down():
    paddle_move(paddle_b, -40)


#Ball
ball = turtle.Turtle()

ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while True:
    
    wn.update()