from turtle import Screen
from paddle import Paddle
from mode import Mode
from ball import Ball
import time
from scoreboard import Score

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


m=Mode()
ch=m.choose_mode()

paddle=Paddle()
ball=Ball()
score=Score()

screen.listen()
screen.onkey(paddle.player1moveup,"Up")
screen.onkey(paddle.player1movedown,"Down")

if ch == 'v':
    screen.onkey(paddle.player2moveup,"w")
    screen.onkey(paddle.player2movedown,"s")


game_is_on=True


while game_is_on:
    time.sleep(ball.bspeed)
    screen.update()
    ball.move()

    if ch != 'v':  # If computer mode is selected
        paddle.computer(ball)

    #collicion with wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #collision with paddle
    if ball.distance(paddle.paddle1[2])<50 and ball.xcor()>320 or ball.distance(paddle.paddle2[2]) <50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()
       

        


    if ball.xcor() < -380 :
        ball.reset_position()
        score.r_point()
        
        
    
screen.exitonclick()