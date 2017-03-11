import turtle

base_dia = 200
base_angle = 120

def triangle_drawa(some_turtle,dia):  # Drawing First big Triangle
    some_turtle.fill(True)
    for i in range(0,3):
        some_turtle.fd(dia)
        some_turtle.left(base_angle)
    some_turtle.fill(False)

def triangle_drawb(some_turtle,dia): # Drawing inner Triangle
    some_turtle.left(60)
    some_turtle.fill(True)
    for i in range(0,3):
        some_turtle.fd(dia)
        some_turtle.left(base_angle)
    some_turtle.fill(False)
    some_turtle.right(60)

def draw_triangle():
    # Window setting
    window = turtle.Screen()
    window.bgcolor("orange")

    # Turtle setting function
    alex = turtle.Turtle()
    alex.color("black","green")
    alex.speed(5)
    alex.shape("turtle")

    # Drawing big triangle
    triangle_drawa(alex,base_dia)

    # Drawing inner triangle
    for j in range(0,3):
        # Turtle setting
        alex.color("black","white")

        # Drawing
        for i in range(1,8):
            if (i%2 == 0):
                if(i%4 == 0):
                    innerdia = base_dia / 2
                    alex.fd(base_dia/8)
                    triangle_drawb(alex, innerdia)
                else:
                    innerdia = base_dia / 4
                    alex.fd(base_dia/8)
                    triangle_drawb(alex, innerdia)
            else:
                innerdia = base_dia / 8
                alex.fd(base_dia/8)
                triangle_drawb(alex, innerdia)
        alex.fd(base_dia / 8)
        alex.left(base_angle)
    window.exitonclick()

draw_triangle()