import turtle as turt

#declare player score variables and assign zero
player1score = 0
player2score = 0

#set window props
window = turt.Screen()
window.title("Pong")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

#create paddles left
left_paddle = turt.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)

#create paddles right
right_paddle = turt.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)

#create ball
ball = turt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

#create scorecard
pen = turt.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=("Verdana", 18, "normal"))


#paddle movement left
def leftpadup():
    y = left_paddle.ycor()
    y = y+90
    left_paddle.sety(y)

def leftpaddown():
    y = left_paddle.ycor()
    y = y-90
    left_paddle.sety(y)


#paddle movement left
def rightpadup():
    y = right_paddle.ycor()
    y = y+90
    right_paddle.sety(y)

def rightpaddown():
    y = right_paddle.ycor()
    y = y-90
    right_paddle.sety(y)


window.listen()
window.onkeypress(leftpadup, 'w')
window.onkeypress(leftpaddown, 's')
window.onkeypress(rightpadup, "Up")
window.onkeypress(rightpaddown, 'Down')

while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #ball bounds
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    #ball bounds
    if (ball.xcor())<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        player2score=player2score+1
        pen.clear()
        pen.write("Player 1:{}      Player 2:{}".format(player1score,player2score),align='center', font=('Verdana', 18, 'normal'))

    #handling contact behaviour
    if (ball.xcor()<-340) and (ball.xcor()<350) and (ball.ycor()<right_paddle.ycor()+40 and ball.ycor()>right_paddle.ycor()-40):
        ball.setx(340)
        ballxdirection = ballxdirection*-1

    if (ball.xcor()>-340) and (ball.xcor()<-350) and (ball.ycor()<left_paddle.ycor()+40 and ball.ycor()>left_paddle.ycor()-40):
        ball.setx(-340)
        ballxdirection = ballxdirection*-1