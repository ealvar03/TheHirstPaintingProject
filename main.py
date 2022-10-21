import turtle as t
import random
from turtle import Screen

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
              (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def generate_random_colour():
    """
    Thi function will generate a random colour from the list above every time the function is called
    :return: It returns the tuple randomly selected from the 'color_list', in rgb sequence, where
    'random_colour = (r = number, g = number, b = number)'
    """
    random_colour = random.choice(color_list)
    return random_colour


# Draw 10 random coloured dots, of a size = 20, with a pace between each = 50, in 10 rows
if __name__ == '__main__':
    paint = t.Turtle()
    screen = Screen()
    paint.speed("fastest")
    screen.colormode(255)
    paint.penup()
    total_length = 10  # Total dots per row
    paint.setposition(-200, -200)  # Set an initial position to begin
    pace = 50  # Separation between dots
    for i in range(10):
        total_dots = 0
        while total_dots < total_length:
            paint.dot(20, generate_random_colour())  # Dot sized set to 20
            paint.penup()
            paint.fd(50)
            total_dots += 1
        paint.setposition(-200, paint.ycor() + pace)  # Increase +50 for the y coordinate
    screen.exitonclick()
