import turtle
import math

screen = turtle.Screen()
screen.title("Interactive Turtle Pattern Generator")
screen.setup(width=900, height=700)
screen.colormode(255)

background_r = int(input("Enter background Red value (0-255): "))
background_g = int(input("Enter background Green value (0-255): "))
background_b = int(input("Enter background Blue value (0-255): "))

screen.bgcolor(background_r, background_g, background_b)

pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)

print("\n--- Turtle Pattern Generator ---")
print("1. Geometric Pattern")
print("2. Koch Snowflake")
print("3. Logarithmic Spiral")

choice = int(input("Enter your choice (1-3): "))

pen_color = input("Enter pen color (e.g., red, blue, cyan, white): ")
pen.color(pen_color)

if choice == 1:
    sides = int(input("Enter number of sides: "))
    length = int(input("Enter side length: "))

    for i in range(sides):
        pen.forward(length)
        pen.right(360 / sides)

        if i % 2 == 0:
            pen.left(30)

elif choice == 2:
    def koch_curve(length, depth):
        if depth == 0:
            pen.forward(length)
        else:
            koch_curve(length / 3, depth - 1)
            pen.left(60)
            koch_curve(length / 3, depth - 1)
            pen.right(120)
            koch_curve(length / 3, depth - 1)
            pen.left(60)
            koch_curve(length / 3, depth - 1)

    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()

    depth = int(input("Enter recursion depth (0-5): "))
    length = 400

    for i in range(3):
        koch_curve(length, depth)
        pen.right(120)

elif choice == 3:
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    turns = int(input("Enter number of spiral turns (1-10): "))
    a = 2
    b = 0.15

    for angle in range(turns * 360):
        theta = math.radians(angle)
        radius = a * math.exp(b * theta)

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        pen.goto(x, y)

else:
    print("Invalid choice!")

pen.hideturtle()
screen.mainloop()