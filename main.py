import time
from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

score_board = ScoreBoard()

food = Food()

screen.listen()

screen.onkey(snake.set_right, "Right")
screen.onkey(snake.set_up, "Up")

screen.onkey(snake.set_left, "Left")
screen.onkey(snake.set_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    snake.movement()
    time.sleep(0.1)


    if snake.distance(food) < 15:
        food.create_food()
        score_board.score_count()
        snake.increase_square()
        print(snake.head.xcor())

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()


    for squares in snake.snake_lenght[1:]:
        if snake.head.distance(squares) < 7:
            score_board.reset()
            snake.reset()

















































screen.listen()














screen.exitonclick()