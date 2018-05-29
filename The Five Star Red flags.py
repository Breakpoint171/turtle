#__Author__:Administrator
#__date__:2018/5/29

import turtle
import math
# 660*440
flag_length = 660
flag_width = 440
turtle.color('red')
turtle.begin_fill()
turtle.up()
turtle.goto(-330,220)
turtle.down()
turtle.goto(330,220)
turtle.goto(330,-220)
turtle.goto(-330,-220)
turtle.goto(-330,220)
turtle.end_fill()
turtle.home()

# 画一个五角星
def star(x,y,angle,length):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(angle)
    distance = length * (1 + math.sin(18/360*math.pi*2))/math.cos(18/360*math.pi*2)
    turtle.fd(distance)
    turtle.color('yellow')
    turtle.rt(18)
    turtle.begin_fill()
    for i in range(5):
        turtle.rt(144)
        turtle.fd(2 * length + length * math.sin(18/360*math.pi*2) * 2)
    turtle.end_fill()

stars = {1:[-flag_length/3, flag_width/4, 90, flag_length/10/(1+math.sin(18/360*math.pi*2))],
         2:[-flag_length/6, 0.4*flag_width, math.asin(0.6)/(2*math.pi)*360+180, flag_length/10/(1+math.sin(18/360*math.pi*2))/3],
         3:[-flag_length/10, 0.3*flag_width, math.asin(1/7)/(2*math.pi)*360+180, flag_length/10/(1+math.sin(18/360*math.pi*2))/3],
         4:[-flag_length/10, 0.15*flag_width, -math.asin(1/7)/(2*math.pi)*360+180, flag_length/10/(1+math.sin(18/360*math.pi*2))/3],
         5: [-flag_length / 6, 0.05 * flag_width, -math.asin(0.6) / (2 * math.pi) * 360 + 180,
             flag_length / 10 / (1 + math.sin(18 / 360 * math.pi * 2)) / 3]}
for i in range(5):
    star(*stars[i+1])

turtle.exitonclick()






































