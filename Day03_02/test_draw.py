import turtle

#setup后两个可选
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")

#seth改变运行方向
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)

#以曲线运行去往目标circle(r,range)
turtle.circle(16, 180)
#以直线去往目标
turtle.fd(40*2/3)
turtle.goto(100,100)
turtle.bk(-200)
turtle.done()