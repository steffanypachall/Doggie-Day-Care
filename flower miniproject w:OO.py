import turtle

def draw_square(pen, x_pos, y_pos, colorName, forwardLength):
    # Setting x,y position
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

def flower_center(pen, x_pos, y_pos):
    # Setting x,y position
    pen.penup()
    pen.setx(x_pos)
    pen.sety(y_pos)
    pen.pendown()

    # Setting speed and shape
    pen.shape("turtle")
    pen.speed(9)

    # Setting color)
    pen.color("yellow")

    # Draw circle
    pen.circle(10)

def flower_stem(pen, x_pos, y_pos):
    # Setting x,y position
    pen.penup()
    pen.setx(x_pos)
    pen.sety(y_pos)
    pen.pendown()

    # Setting shape and speed
    pen.shape("turtle")
    pen.speed(9)

    # Setting color
    pen.color("darkgreen")

    # Draw stem
    pen.right(90)
    pen.forward(85)

def draw_picture():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    # Draw sun
    pen = turtle.Turtle()
    for i in range(36):
        draw_square(pen, -135, 190, "yellow", 75)
        pen.right(10)
    for i in range(36):
        draw_square(pen, -135, 190, "orange", 25)
        pen.right(10)
    # Draw purple flower
    for i in range(36):
        draw_square(pen, -175, -155, "purple", 45)
        pen.right(10)
    for i in range(36):
        flower_center(pen,-175, -155)
        pen.right(10)
    flower_stem(pen, -175, -190)
    # Draw pink flower
    for i in range(36):
        draw_square(pen, 0, -155, "hotpink", 45)
        pen.right(10)
    for i in range(36):
        flower_center(pen, 0, -155)
        pen.right(10)
    pen.right(270)
    flower_stem(pen, 0, -190)
    # Draw red flower
    for i in range(36):
        draw_square(pen, 175, -155, "red", 45)
        pen.right(10)
    for i in range(36):
        flower_center(pen, 175, -155)
        pen.right(10)
    pen.right(270)
    flower_stem(pen, 175, -190)
    
    window.extinctionclick()

draw_picture()
