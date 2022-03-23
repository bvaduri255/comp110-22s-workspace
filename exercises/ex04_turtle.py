"""EX04 - Draw a scene of the night sky :). The rectangle, triangle functions are supporter functions for the ground, sky, tree, stars, and moon. The radian to degree function helps with calculations for the triangle function. The stars and trees are drawn multiple times. Loops are used to draw the stars and rectangles. Fill color is used extensively to fill in all the shapes. Marker color is changed at every shape because I don't want the shapes to have a black outline."""

__author__ = "730489799"

from turtle import Turtle, done, tracer, update
import turtle
import math

turty: Turtle = Turtle()

turty.speed(0)
turtle.colormode(255)
screen_width: int = 800
screen_height: int = 600

turtle.screensize(screen_width, screen_height)


def rad_to_deg(radians: float) -> float:
    """Convert radians to degrees."""
    deg: float = radians * 180 / math.pi

    return deg


def draw_rectangle(turt: Turtle, height: int, width: int) -> None:
    """Draw rectangle with turtle given height and width."""
    i: int = 0

    while i < 2:
        turt.forward(width)
        turt.left(90)
        turt.forward(height)
        turt.left(90)
        i += 1


def draw_isotriangle(turt: Turtle, base: int, slant_height: int) -> None:
    """Draw an isoceles triangle. Math is used to calculate angles of rotation."""
    base_angle: float = rad_to_deg(math.acos((base / 2) / slant_height))
    apex_angle: float = 180 - 2 * base_angle
    turt.forward(base)
    turt.left(180 - base_angle)
    turt.forward(slant_height)
    turt.right(apex_angle + 180)
    turt.forward(slant_height)


def ground(turt: Turtle, x_coord: float, y_coord: float) -> None:
    """Draw the grass for the scene."""
    turt.penup()
    turt.goto(x_coord, y_coord)
    turt.pendown()
    turt.pencolor((0, 102, 0))
    turt.fillcolor((0, 102, 0))
    turt.begin_fill()
    draw_rectangle(turt, 150, screen_width)
    turt.end_fill()
    turt.goto(-400, -150)
    turt.pencolor((25, 51, 0))
    turt.fillcolor((25, 51, 0))
    turt.begin_fill()
    draw_rectangle(turt, 50, screen_width)
    turt.end_fill()


def sky(turt: Turtle, x_coord: float, y_coord: float) -> None:
    """Draw the night sky filling up the top majority of the screen."""
    turt.penup()
    turt.goto(x_coord, y_coord)
    turt.pendown()

    turt.pencolor((0, 0, 102))
    turt.fillcolor((0, 0, 102))
    turt.begin_fill()
    draw_rectangle(turt, screen_height - 200, screen_width)
    turt.end_fill()


def moon(turt: Turtle, x_coord: float, y_coord: float) -> None:
    """Draw a full moon in the night sky."""
    turt.penup()
    turt.goto(x_coord, y_coord)
    turt.pendown()

    turt.pencolor("white")
    turt.fillcolor("white")
    turt.begin_fill()
    turt.circle(50)
    turt.end_fill()


def star(turt: Turtle, x_coord: float, y_coord: float) -> None:
    """Draw a star with 5 points using loops."""
    points: int = 5

    turt.penup()
    turt.goto(x_coord, y_coord)
    turt.pendown()

    turt.pencolor("white")
    turt.fillcolor("white")
    turt.begin_fill()
    while points > 0:
        turt.forward(35)
        turt.right(144)
        points -= 1
    turt.end_fill()


def tree(turt: Turtle, x_coord: float, y_coord: float) -> None:
    """Draw a tree consisting of a rectangle for a trunk and triangle for the foliage."""
    turt.penup()
    turt.goto(x_coord, y_coord)
    turt.pendown()
    turt.setheading(0)

    turt.pencolor("brown")
    turt.fillcolor("brown")
    turt.begin_fill()
    draw_rectangle(turt, 50, 25)
    turt.end_fill()

    turt.pencolor((0, 102, 0))
    turt.fillcolor((0, 102, 0))
    turt.penup()
    turt.goto(x_coord - 10, y_coord + 50)
    turt.pendown()
    turt.begin_fill()
    draw_isotriangle(turt, 45, 80)
    turt.end_fill()


def main() -> None:
    """The entrypoint to draw the scene."""
    tracer(0, 0)
    ground(turty, -400, -300)
    sky(turty, -400, -100)
    moon(turty, -300, 175)
    star(turty, 250, 150)
    star(turty, 175, 200)
    star(turty, 0, 185)
    star(turty, -100, 250)
    star(turty, -250, 100)
    star(turty, -200, 200)
    tree(turty, -200, -100)
    tree(turty, 300, -100)
    tree(turty, 150, -100)
    update()
    done()


if __name__ == "__main__":
    main()