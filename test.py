import turtle
import time
import random

# Creating screen:
screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
border = turtle.Turtle()
border.speed(0)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("red")
for _ in range(2):
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color("red")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=('Courier', 24, "bold"))


# Define how to move:
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard key movements:
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Generating random color to snake body:
turtle.colormode(255)#this sets the color mode to rgb
# Function to generate a random color
def get_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

# Main Loop
while True:
    screen.update()

    # If fruit and snake meet:
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)  # This generates random location for fruit to move
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # Adding length to snake:
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        random_color=get_random_color()
        new_fruit.color(random_color)
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Move the end segments first in reverse order
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    # Move segment 0 to where the snake is
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # Snake and border collision:
    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        screen.goto(0, 0)
        screen.write(
            "Game Over \n Your score is:{}".format(score),
            align="center",
            font=("Courier", 30, "bold"),
        )

    # Snake collisions
    for segment in old_fruit:
        if segment.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            screen.goto(0, 0)
            screen.write(
                "Game Over \n Your score is:{}".format(score),
                align="center",
                font=("Courier", 30, "bold"),
            )

    time.sleep(delay)

turtle.mainloop()  # Keep the window open
