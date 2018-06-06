import turtle
from random import randint
turtle.hideturtle()
turtle.colormode(255)
text = ['金','榜','题','名']
def fun():
    turtle.clear()
    turtle.up()
    turtle.home()
    turtle.fd(-120)
    turtle.down()
    for i in range(4):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        turtle.pencolor(r,g,b)
        turtle.write(text[i], align="center",
                    font=("Courier", 50, "bold"))
        turtle.up()
        turtle.fd(70)
        turtle.down()
    turtle.ontimer(fun,300)
fun()
turtle.mainloop()



