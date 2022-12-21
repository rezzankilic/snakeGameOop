class Move:
    def movement(self):
        game_is_on = True
        while game_is_on:
        screen.update()

        for squares in range(len(snake_lenght)-1, 0, -1):
            new_x = snake_lenght[squares-1].xcor()
            new_y = snake_lenght[squares-1].ycor()
            snake_lenght[squares].goto(new_x, new_y)
        snake_lenght[0].forward(20)
        snake_lenght[0].left(90)
        time.sleep(1)