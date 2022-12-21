from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270



class Snake():
    def __init__(self):
        self.snake_lenght = []
        self.create_snake()
        self.head = self.snake_lenght[0]


    def reset(self):
        for segment in self.snake_lenght:
            segment.goto(300, 300)

        self.snake_lenght.clear()
        self.create_snake()
        self.head = self.snake_lenght[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)


    def add_square(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.speed(1)
        self.snake_lenght.append(new_turtle)

    def increase_square(self):
        last_position = self.snake_lenght[-1].position()

        self.add_square(last_position)

    def movement(self):
        for squares in range(len(self.snake_lenght) - 1, 0, -1):
            new_x = self.snake_lenght[squares - 1].xcor()
            new_y = self.snake_lenght[squares - 1].ycor()
            self.snake_lenght[squares].goto(new_x, new_y)
        self.snake_lenght[0].forward(MOVE_DISTANCE)

    def set_right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)

    def set_up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def set_left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def set_down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def distance(self, food):
        return self.head.distance(food)


