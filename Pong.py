import turtle

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

# Paddle B


#Ball


# Main game loop
while True:
    wn.update()
    wn.exitonclick()
