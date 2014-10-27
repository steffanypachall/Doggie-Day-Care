import turtle

def draw_square(pen, x_pos, y_pos, colorName, forwardLength):
    # setting x,y position
    pen.penup()
    pen.setx(x_pos)
    pen.sety(y_pos)
    pen.pendown()

    # setting speed and shape
    pen.shape("turtle")
    pen.speed(9)

    # Set color
    pen.color(colorName)

    # Draw square
    for i in range(4):
     pen.forward(forwardLength)
     pen.right(90)

#def draw_square(haru,):
    #for i in range(4):
     #haru.penup()
     #haru.setx(-135)
     #haru.sety(190)
     #haru.pendown()
     #haru.forward(25)
     #haru.right(90)

#def draw_sun(sun):
    #for i in range(3):
     #sun.penup()
     #sun.setx(-135)
     #sun.sety(190)
     #sun.pendown()
     #sun.right(120)
     #sun.forward(75)

#def purple_flower(purple):
    #purple.penup()
    #purple.setx(-175)
    #purple.sety(-155)
    #purple.pendown()
    #for i in range(4):
     #purple.forward(45)
     #purple.right(90)

def flower_center(x_pos, y_pos):
    pen = turtle.Turtle()
    # Set setting x,y position
    pen.penup()
    pen.setx(x_pos)
    pen.sety(y_pos)
    pen.pendown()
    # set shape and speed
    pen.shape("turtle")
    pen.speed(9)
    # set color
    pen.color("yellow")
    # draw circle
    pen.circle(10)
    #center.penup()
    #center.setx(-175)
    #center.sety(-155)
    #center.pendown()
    #center.circle(10)

def flower_stem(x_pos, y_pos):
    pen = turtle.Turtle()
    # Set x,y position
    pen.penup()
    pen.setx(x_pos)
    pen.sety(y_pos)
    pen.pendown()
    # Set shape and Speed
    pen.shape("turtle")
    pen.speed(9)
    # Set color
    pen.color("darkgreen")
    # draw stem
    pen.right(90)
    pen.forward(85)
    #stem.penup()
    #stem.setx(-175)
    #stem.sety(-190)
    #stem.pendown()
    #stem.right(90)
    #stem.forward(85)

#def pink_flower(pink):
    #pink.penup()
    #pink.setx(0)
    #pink.sety(-155)
    #pink.pendown()
    #for i in range(4):
     #pink.forward(45)
     #pink.right(90)

#def pink_flower_center(pollen):
    #pollen.penup()
    #pollen.setx(0)
    #pollen.sety(-155)
    #pollen.pendown()
    #pollen.circle(10)

#def pink_flower_stem(green):
    #green.penup()
    #green.setx(0)
    #green.sety(-190)
    #green.pendown()
    #green.right(90)
    #green.forward(85)

#def red_flower(red):
    #red.penup()
    #red.setx(175)
    #red.sety(-155)
    #red.pendown()
    #for i in range(4):
     #red.forward(45)
     #red.right(90)

#def red_flower_center(rcenter):
    #rcenter.penup()
    #rcenter.setx(175)
    #rcenter.sety(-155)
    #rcenter.pendown()
    #rcenter.circle(10)

#def red_flower_stem(gstem):
    #gstem.penup()
    #gstem.setx(175)
    #gstem.sety(-190)
    #gstem.pendown()
    #gstem.right(90)
    #gstem.forward(85)
    
    

def draw_picture():
    window = turtle.Screen()
    window.bgcolor("lightblue")
# Draw Sun
    pen = turtle.Turtle()
    for i in range(36):
     draw_square(pen, -135, 190, "yellow", 75)
     pen.right(10)
    for i in range(36):
     draw_square(pen, -135, 190, "orange", 25)
     pen.right(10)
    #sun = turtle.Turtle()
    #sun.shape("turtle")
    #sun.color("yellow")
    #sun.speed(9)
    #for i in range(36):
      #draw_sun(sun)
      #sun.right(10)
    #haru = turtle.Turtle()
    #haru.shape("turtle")
    #haru.color("orange")
    #haru.speed(9)
    #for i in range(36):
        #draw_square(haru)
        #haru.right(10)
    #purple = turtle.Turtle()
   # purple.shape("turtle")
    #purple.color("purple")
    #purple.speed(9)
    #for i in range(36):
        #purple_flower(purple)
        #purple.right(10)
    #center = turtle.Turtle()
    #center.shape("turtle")
    #center.color("yellow")
    #center.speed(9)
    #for i in range(36):
        #flower_center(center)
        #center.right(10)
    #stem = turtle.Turtle()
    #stem.shape("turtle")
    #stem.color("green")
    #stem.speed(9)
    #flower_stem(stem)
    #pink = turtle.Turtle()
    #pink.shape("turtle")
    #pink.color("hotpink")
    #pink.speed(9)
    #for i in range(36):
        #pink_flower(pink)
        #pink.right(10)
    #pollen = turtle.Turtle()
    #pollen.shape("turtle")
    #pollen.color("yellow")
    #pollen.speed(9)
    #for i in range(36):
        #pink_flower_center(pollen)
        #pollen.right(10)
    #green = turtle.Turtle()
    #green.shape("turtle")
    #green.color("green")
    #green.speed(9)
    #pink_flower_stem(green)
    #red = turtle.Turtle()
    #red.shape("turtle")
    #red.color("red")
    #red.speed(9)
    #for i in range(36):
        #red_flower(red)
        #red.right(10)
    #rcenter = turtle.Turtle()
    #rcenter.shape("turtle")
    #rcenter.color("yellow")
    #rcenter.speed(9)
    #for i in range(36):
        #red_flower_center(rcenter)
        #rcenter.right(10)
    #gstem = turtle.Turtle()
    #gstem.shape("turtle")
    #gstem.color("green")
    #gstem.speed(9)
    #red_flower_stem(gstem)


    window.extinctionclick()

draw_picture()
