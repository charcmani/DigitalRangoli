from turtle import *

speed(10000)

bgcolor('grey')
###############SET CUSOR#####################
x = 1
penup()
home()
sety(80)
pensize(1)
pendown()
#############################################
while x < 98:
    m=0.911
    n=61
    o=121
    fill(True)
    colormode(255)
    if x>30 and x<73:
        pencolor('black')
        fillcolor(102,0,0)
        m=1.111
    elif x>72:
        pencolor('black')
        fillcolor(204, 0, 0)
        m=1.211
    else:
        pencolor('black')
        fillcolor(255, 102, 102)
    fd(150)
    rt(61+m)
    fd(100)
    rt(121+m)
    fd(100)
    rt(61+m)
    fd(150)
    x=x+1
penup()
home()
sety(120)
pencolor(255, 102, 102)
pendown()
x = 1
while x < 300:
    y=x
    if x>150:
        y=150
        pencolor(102,0,0)
    fd(2+y)
    rt(150.911)
    x = x+1


###############SET CUSOR#####################
penup()
fill(False)
x=1
setx(-500)
pendown()
fill(True)
################################################
#2nd flower

while x < 73:
    m=0.911
    n=61
    o=121
    fill(True)
    colormode(255)
    if x>30 and x<73:
        pencolor('black')
        fillcolor(204, 153, 0)
        m=1.111
    elif x>72:
        pencolor('black')
        fillcolor(204, 153, 0)
        m=1.211
    else:
        pencolor('black')
        fillcolor(102,77,0)
    fd(75)
    rt(61+m)
    fd(50)
    rt(121+m)
    fd(50)
    rt(61+m)
    fd(75)
    x=x+1

setx(-483)
sety(162)
pencolor(230, 230, 0)
x = 1

while x < 150:
    y=x
    if x>60:
        y=60
        pencolor(102,77,0)
    fd(2+y)
    rt(150.911)
    x = x+1

###############SET CUSOR#####################
penup()
fill(False)
x=1
setx(500)
pendown()
fill(True)
#############################################3
#3rd flower

while x < 73:
    m=0.911
    n=61
    o=121
    fill(True)
    colormode(255)
    if x>30 and x<73:
        pencolor('black')
        fillcolor(45, 185, 45)
        m=1.111
    else:
        pencolor('black')
        fillcolor(25, 102, 25)
    fd(90)
    rt(61+m)
    fd(60)
    rt(121+m)
    fd(60)
    rt(61+m)
    fd(90)
    x=x+1

setx(504)
sety(196)
pencolor(45, 185, 45)
x = 1

while x < 150:
    y=x
    if x>70:
        y=70
        pencolor(25, 102, 25)

    fd(2+y)
    rt(150.911)
    x = x+1

###############SET CUSOR#####################
penup()
fill(False)
home()
x=1
setx(-495)
sety(-263)
pendown()
fill(True)
##########################################
#4th flower
while x < 112:
    m=0.111
    n=61
    o=121
    fill(True)
    colormode(255)
    if x>30 and x<73:
        pencolor('black')
        fillcolor(191, 0, 255)
        m=0.111
    elif x>72:
        pencolor('black')
        fillcolor(153, 0, 153)
        m=1.211
    else:
        pencolor('black')
        fillcolor(115, 0, 153)

    pensize=3
    circle(600,30+m)
    rt(-150.911)
    x=x+1
    circle(600,30+m)
setx(-490)
sety(-263)
pencolor('black')
x = 1

while x < 120:
    y=x
    if x>60:
        y=60
        pencolor(115, 0, 153)

    fd(2+y)
    rt(150.911)
    x = x+1

###############SET CUSOR#####################
penup()

fill(False)
home()
x=1
setx(495)
sety(-263)
pendown()
fill(True)
#######################################################
#5th flower
while x < 112:
    m=0.111
    n=61
    o=121
    fill(True)
    colormode(255)
    if x>30 and x<73:
        pencolor('black')
        fillcolor(191, 0, 255)
        m=0.111
    elif x>72:
        pencolor('black')
        fillcolor(153, 0, 153)
        m=1.211
    else:
        pencolor('black')
        fillcolor(115, 0, 153)

    pensize=3
    circle(600,30+m)
    rt(-150.911)
    x=x+1
    circle(600,30+m)
setx(500)
sety(-265)
pencolor('black')

x = 1
while x < 150:
    y=x
    if x>60:
        y=60
        pencolor(115, 0, 153)

    fd(2+y)
    rt(150.911)
    x = x+1

exitonclick()
