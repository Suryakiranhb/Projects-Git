import turtle

wn=turtle.Screen()
wn.title("Pong by SK")
wn.bgcolor("purple")
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a=0
score_b=0


# raq A
raq_a= turtle.Turtle()
raq_a.speed(0)
raq_a.shape("square")
raq_a.color("white")
raq_a.shapesize(stretch_wid=5,stretch_len=1)
raq_a.penup()
raq_a.goto(-350,0)


# raq B
raq_b= turtle.Turtle()
raq_b.speed(0)
raq_b.shape("square")
raq_b.color("white")
raq_b.shapesize(stretch_wid=5,stretch_len=1)
raq_b.penup()
raq_b.goto(350,0)

# pong 
pong= turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.color("white")
pong.penup()
pong.goto(0,0)
pong.dx=0.1
pong.dy=-0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,-260)
pen.write("CONTROLS:    P1: W/S P2:Up/Down", align="Center",font=("Impact",28,"normal"))
pen.goto(0,260)
pen.write("Left: Go!       Right: Go!", align="Center",font=("Impact",24,"normal"))



# Functions
def raq_a_up():
    y=raq_a.ycor()
    y+=40
    raq_a.sety(y)

def raq_a_down():
    y=raq_a.ycor()
    y-=40
    raq_a.sety(y)


def raq_b_up():
    y=raq_b.ycor()
    y+=40
    raq_b.sety(y)

def raq_b_down():
    y=raq_b.ycor()
    y-=40
    raq_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(raq_a_up, "w")
wn.onkeypress(raq_a_down,"s")
wn.onkeypress(raq_b_up, "Up")
wn.onkeypress(raq_b_down,"Down")

# Main game loop

while True:
    wn.update()

    # Move the pong
    pong.setx(pong.xcor()+pong.dx)
    pong.sety(pong.ycor()+pong.dy)

    # Border Check
    if pong.ycor()>290:
        pong.sety(290)
        pong.dy*=-1

    if pong.ycor()<-290:
        pong.sety(-290)
        pong.dy*=-1
    
    if pong.xcor()>390:
        pong.goto(0,0)
        pong.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("LEFT: {}       RIGHT: {}".format(score_a,score_b), align="Center",font=("Impact",22,"normal"))


    if pong.xcor()<-390:
        pong.goto(0,0)
        pong.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("LEFT: {}       RIGHT: {}".format(score_a,score_b), align="Center",font=("Impact",22,"normal"))


    # raq and pong coll
    if (pong.xcor()>340 and pong.xcor()<350) and (pong.ycor()<raq_b.ycor()+40 and pong.ycor()>raq_b.ycor()-40):
        pong.setx(340)
        pong.dx*=-1

    if (pong.xcor()<-340 and pong.xcor()>-350) and (pong.ycor()<raq_a.ycor()+40 and pong.ycor()>raq_a.ycor()-40):
        pong.setx(-340)
        pong.dx*=-1