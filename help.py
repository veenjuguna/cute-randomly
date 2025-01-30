import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Ivy Njuguna Animation")

# Create a turtle to draw the text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()

# Function to draw the text
def draw_text(text, x, y, font_size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align="center", font=("Arial", font_size, "bold"))

# Function to animate the text
def animate_text():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(6):
        pen.clear()
        draw_text("Ivy Njuguna", 0, 0, 36, colors[i])
        time.sleep(0.5)

# Main loop
while True:
    animate_text()

# Keep the window open
turtle.done()