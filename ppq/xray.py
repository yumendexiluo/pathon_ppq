import turtle


def draw_polygon(aTurtle, size=50, n=3):
    ''' 绘制正多边形

    args:
        aTurtle: turtle对象实例
        size: int类型，正多边形的边长
        n: int类型，是几边形
    '''
    for i in range(n):
        aTurtle.forward(size)
        aTurtle.left(360.0 / n)


def draw_circle(aTurtle=None, start_pos=(0, 0), size=20.0, color='black'):
    aTurtle = aTurtle or turtle.Turtle()
    aTurtle.begin_fill()
    aTurtle.fillcolor(color)
    aTurtle.penup()
    aTurtle.goto(start_pos)
    aTurtle.pendown()
    aTurtle.circle(size)
    aTurtle.end_fill()


def draw_fan(aTurtle=None, start_pos=(0, 0), left=0, redius2=23, redius3=113):
    aTurtle.penup()
    aTurtle.begin_fill()
    aTurtle.fillcolor('black')
    # 到初始点
    aTurtle.goto(start_pos)
    aTurtle.pendown()
    aTurtle.fd(redius3 - redius2)
    aTurtle.left(90)
    # 做弧
    aTurtle.circle(redius3, 60)
    aTurtle.left(90)
    aTurtle.fd(redius3 - redius2)
    aTurtle.left(120 - left)
    aTurtle.goto(start_pos)
    aTurtle.penup()
    aTurtle.end_fill()
    aTurtle.goto(0, 0)


def draw_x_ray(length=300, redius1=20, redius2=23, redius3=113):
    width, height = length, length
    # 初始化屏幕和海龟
    window = turtle.Screen()
    aTurtle = turtle.Turtle()
    aTurtle.hideturtle()
    aTurtle.speed(10)
    # 画黄色背景
    aTurtle.penup()
    aTurtle.goto(-width / 2, height / 2)
    aTurtle.pendown()
    aTurtle.begin_fill()
    aTurtle.fillcolor('yellow')
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.end_fill()

    aTurtle.penup()
    aTurtle.goto(0, 0)
    # 三个扇叶
    aTurtle.fd(redius2)
    draw_fan(aTurtle, start_pos=aTurtle.pos(), redius2=redius2, redius3=redius3)
    aTurtle.left(120)
    aTurtle.fd(redius2)
    draw_fan(aTurtle, start_pos=aTurtle.pos(), left=120, redius2=redius2, redius3=redius3)
    aTurtle.left(240)
    aTurtle.fd(redius2)
    draw_fan(aTurtle, start_pos=aTurtle.pos(), left=240, redius2=redius2, redius3=redius3)
    # 画圆
    aTurtle.color('yellow')
    draw_circle(aTurtle, start_pos=(0, -redius2), size=23, color='yellow')
    aTurtle.color('black')
    draw_circle(aTurtle, start_pos=(0, -redius1), size=redius1, color='black')
    # 点击关闭窗口
    window.exitonclick()


if __name__ == '__main__':
    draw_x_ray()
