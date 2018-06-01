#__Author__:Administrator
#__date__:2018/5/30


import turtle

turtle.setup(800,600)
turtle.speed(0)
turtle.dot(5)


turtle.up()
turtle.pensize(4)
# 这里7.19主要时让废柴以y轴左右对称，可不加
turtle.goto(-100+7.19,100)
turtle.hideturtle() # 隐藏画笔
turtle.color('red','orange')  # 设置画笔颜色和填充颜色
turtle.begin_fill()
turtle.down()

angle = 90
turtle.setheading(angle)
for i in range(150):
    turtle.fd(0.6)
    angle -= 0.2
    turtle.setheading(angle)

angle -= 25

for i in range(30):

    turtle.fd(0.3)
    angle -= 0.5
    turtle.setheading(angle)

for i in range(22):
    angle -= 3
    turtle.fd(0.3)
    turtle.setheading(angle)

for i in range(70):
    turtle.fd(0.7)
    angle -= 0.1
    turtle.setheading(angle)

turtle.up()
x,y = turtle.pos()
turtle.goto(x-15,y-5)
angle1 = 20
turtle.down()
turtle.setheading(angle1)
for i in range(40):
    turtle.fd(2)
    angle1 -= 1
    turtle.setheading(angle1)

# 右耳朵
turtle.up()
turtle.goto(x+50,y)
turtle.down()
for i in range(70):
    turtle.setheading(-angle)
    angle += 0.1
    turtle.fd(0.7)

for i in range(22):
    angle += 3
    turtle.fd(0.3)
    turtle.setheading(-angle)

for i in range(30):
    turtle.fd(0.3)
    angle += 0.5
    turtle.setheading(-angle)

angle += 25
for i in range(150):
    turtle.fd(0.6)
    angle += 0.2
    turtle.setheading(-angle)

# 脸部
angle = -115
turtle.up()
turtle.goto(-100+8,104)
turtle.down()
turtle.end_fill()
turtle.begin_fill()
for i in range(42):
    turtle.setheading(angle)
    turtle.fd(1)
    angle += 0.3
angle2 = -130
for i in range(100):
    turtle.setheading(angle2)
    turtle.fd(0.4)
    angle2 += 0.4
distance = 0.5
for i in range(60):
    turtle.fd(distance)
    distance += 0.0702
    angle2 += 1.5
    turtle.setheading(angle2)
x,y = turtle.pos()

for i in range(60):
    turtle.fd(distance)
    distance -= 0.0702
    angle2 += 1.5
    turtle.setheading(angle2)

for i in range(100):
    turtle.fd(0.4)
    angle2 += 0.4
    turtle.setheading(angle2)

for i in range(44):
    turtle.setheading(-angle)
    turtle.fd(1)
    angle -= 0.3
turtle.end_fill()

# 画胳膊
turtle.up()
turtle.goto(-61,y+10)
angle = -120
turtle.down()
turtle.begin_fill()
for i in range(50):
    turtle.setheading(angle)
    turtle.fd(1.2)
    angle += 0.3

for i in range(20):
    turtle.fd(1.9)
    angle += 110/20
    turtle.setheading(angle)

xx,yy = turtle.pos()
turtle.goto(-xx,yy)
angle = -angle
for i in range(20):
    turtle.setheading(angle)
    turtle.fd(1.9)
    angle += 110/20

for i in range(50):
    turtle.fd(1.2)
    angle += 0.3
    turtle.setheading(angle)

turtle.end_fill()

# 画身体
turtle.up()
turtle.goto(-45,y+7)
turtle.down()
angle = -115
turtle.begin_fill()
for i in range(200):
    turtle.fd(0.7)
    angle += 0.25
    turtle.setheading(angle)

# 画脚
angle = -140
for i in range(25):
    turtle.fd(0.8)
    angle += 2
    turtle.setheading(angle)
distance = 0.1
for i in range(40):
    turtle.fd(distance)
    distance += 0.07
    angle += 4.5
    turtle.setheading(angle)

turtle.fd(20)
turtle.setheading(0)
turtle.fd(32)

turtle.setheading(-90)
turtle.fd(20)
angle = -90
for i in range(40):
    angle += 4.5
    turtle.setheading(angle)
    distance -= 0.07
    turtle.fd(distance)

for i in range(25):
    angle += 2
    turtle.setheading(angle)
    turtle.fd(0.8)

angle = 65
for i in range(200):
    turtle.fd(0.7)
    angle += 0.25
    turtle.setheading(angle)

turtle.end_fill()

turtle.up()
turtle.goto(-10,-100)

angle = -30
turtle.down()
distance = 1
for i in range(65):
    turtle.setheading(angle)
    turtle.fd(distance)
    distance += 0.04
    angle -= 7

for i in range(20):
    turtle.fd(1.91)
    angle -= 7
    turtle.setheading(angle)

turtle.exitonclick()