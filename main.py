from turtle import Screen
from paddle import Paddle
from scoreboard import Half, Scoreboard
import time
from ball import Ball

screen = Screen()
scoreboard = Scoreboard()
line = Half()
screen.bgcolor("black")
screen.title("Pong_Game")
screen.setup(width=800, height=600)
screen.tracer(0)
scoreboard.write_score()
line.draw()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.r_go_up, "Up")
screen.onkey(r_paddle.r_go_down, "Down")
screen.onkey(l_paddle.l_go_up, "w")
screen.onkey(l_paddle.l_go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (ball.xcor() > 320 or ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.increase1()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.increase2()
        ball.reset_position()

scoreboard.game_over()
screen.exitonclick()
