import turtle
turtle.colormode(255)
turtle.bgcolor('white')
yang = turtle.Turtle()
yin = turtle.Turtle()
turtle.tracer(0)
yang.speed(0)
yin.speed(0)

white = 0, 0, 0
black = 255, 255 ,255

for times in range (360):
    yin.color(white)
    yin.begin_fill()
    yin.circle(152)
    yin.end_fill()
    yin.left(1)

for times in range (180):
    yin.color(white)
    yin.begin_fill()
    yin.circle(150)
    yin.left(181)
    yin.end_fill()

for times in range (180):
    yang.color(black)
    yang.begin_fill()
    yang.circle(150)
    yang.left(1)
    yang.end_fill()

for times in range (2):
    yin.color(white)
    yin.begin_fill()
    yin.circle(150)
    yin.left(1)
    yin.end_fill()

for times in range (1):
    yang.penup()
    yang.right(115)
    yang.forward(140)
    yang.pendown()
    yang.begin_fill()
    yang.color(white)
    yang.circle(50)
    yang.end_fill()

for times in range (1):
    yang.penup()
    yang.right(180)
    yang.forward(280)
    yang.pendown()
    yang.begin_fill()
    yang.color(black)
    yang.circle(50)
    yang.end_fill()


