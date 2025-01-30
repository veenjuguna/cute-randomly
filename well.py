import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle named "pretty"
pretty = turtle.Turtle()
pretty.shape("turtle")
pretty.color("purple")

# Draw a pretty flower
pretty.speed(10)
for _ in range(36):
    pretty.circle(100)
    pretty.right(10)

# Hide the turtle and display the window
pretty.hideturtle()
turtle.done()