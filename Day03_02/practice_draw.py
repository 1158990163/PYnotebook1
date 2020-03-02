"""import turtle
import math

turtle.setup(800,450,200,200)
turtle.pencolor('blue')
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(10)
turtle.fd(200)
turtle.seth(-45)
turtle.fd(200)
turtle.seth(90)
turtle.fd(200)
for i in range(40):
    turtle.fd(30)
    turtle.seth(10+i*10)
turtle.fd(10)
turtle.done()
"""
# China（ZhongGuo）

# Python--五星红旗Python--五星红旗Python--五星红旗Python--五星红旗Python--五星红旗

import turtle

import math


def draw_n_angle(aTurtle, size=50, num=5, color=None):
    if color:
        aTurtle.begin_fill()

        aTurtle.fillcolor(color)

    for i in range(num):  # hua yige wujiaoxing

        aTurtle.forward(size)

        aTurtle.left(360.0 / num)

        aTurtle.forward(size)

        aTurtle.right(2 * 360.0 / num)

    if color:
        aTurtle.end_fill()


def draw_5_angle(aTurtle=None, start_pos=(0, 0), end_pos=(0, 0), radius=0, color=None):
    aTurtle = aTurtle or turtle.Turtle()

    size = radius * math.sin(math.pi / 5) / math.sin(math.pi * 2 / 5)

    aTurtle.left(math.degrees(
        math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])))  # jisuan liangdian zhi jian de xieqingjiao

    aTurtle.penup()

    aTurtle.goto(start_pos)

    aTurtle.fd(radius)

    aTurtle.pendown()

    aTurtle.right(math.degrees(math.pi * 9 / 10))  # zhaodao wujiaoixngweizhi

    draw_n_angle(aTurtle, size, 5, color)  # huawujiaoxing`在这里插入代码片`


def draw_5_star_flag(times=20.0):
    width, height = 30 * times, 20 * times

    window = turtle.Screen()

    aTurtle = turtle.Turtle()

    aTurtle.hideturtle()

    aTurtle.speed(10)

    aTurtle.penup()

    aTurtle.goto(-width / 2, height / 2)

    aTurtle.pendown()

    aTurtle.begin_fill()

    aTurtle.fillcolor('red')

    aTurtle.fd(width)

    aTurtle.right(90)

    aTurtle.fd(height)

    aTurtle.right(90)

    aTurtle.fd(width)

    aTurtle.right(90)

    aTurtle.fd(height)

    aTurtle.right(90)

    aTurtle.end_fill()  # hua hongse qi

    draw_5_angle(aTurtle, start_pos=(-10 * times, 5 * times), end_pos=(-10 * times, 8 * times), radius=3 * times,
                 color='yellow')  # dawujiaoxing

    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]  # zidian

    for pos in stars_start_pos:
        draw_5_angle(aTurtle, start_pos=(pos[0] * times, pos[1] * times), end_pos=(-10 * times, 5 * times),
                     radius=1 * times, color='yellow')  # sigexiaowujiaoxing

    window.exitonclick()


if __name__ == '__main__':
    draw_5_star_flag()
