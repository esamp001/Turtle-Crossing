import turtle

# Create a turtle instance
my_turtle = turtle.Turtle()

# Function to draw the letter H
def draw_H(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Left vertical line
    turtle_instance.right(180)
    turtle_instance.forward(50)   # Move down to the middle
    turtle_instance.right(90)
    turtle_instance.forward(50)   # Draw middle line
    turtle_instance.left(90)
    turtle_instance.forward(50)   # Move up to the right vertical
    turtle_instance.right(180)
    turtle_instance.forward(100)  # Right vertical line
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to draw the letter A
def draw_A(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(75)
    turtle_instance.forward(100)  # Left slant
    turtle_instance.right(150)
    turtle_instance.forward(100)  # Right slant
    turtle_instance.right(105)
    turtle_instance.forward(40)   # Cross bar
    turtle_instance.penup()
    turtle_instance.right(75)

# Function to draw the letter P
def draw_P(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Vertical line
    turtle_instance.right(90)
    turtle_instance.forward(50)   # Move to the right
    turtle_instance.circle(-25, 180)  # Draw half circle
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to draw the letter Y
def draw_Y(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(75)
    turtle_instance.forward(50)   # Left upper line
    turtle_instance.right(150)
    turtle_instance.forward(50)   # Right upper line
    turtle_instance.right(105)
    turtle_instance.forward(50)   # Vertical line
    turtle_instance.penup()
    turtle_instance.right(75)

# Function to draw the letter M
def draw_M(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Left vertical line
    turtle_instance.right(150)
    turtle_instance.forward(100)  # Right slant
    turtle_instance.left(120)
    turtle_instance.forward(100)  # Left slant
    turtle_instance.right(150)
    turtle_instance.forward(100)  # Right vertical line
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to draw the letter O
def draw_O(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.circle(50)  # Draw a circle for O
    turtle_instance.penup()

# Function to draw the letter N
def draw_N(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Left vertical line
    turtle_instance.right(150)
    turtle_instance.forward(115)  # Diagonal line
    turtle_instance.left(150)
    turtle_instance.forward(100)  # Right vertical line
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to draw the letter T
def draw_T(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.forward(70)   # Top line
    turtle_instance.backward(35)  # Move back to center
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Vertical line
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to draw the letter S
def draw_S(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.circle(30, 180)  # Top half
    turtle_instance.circle(-30, 180)  # Bottom half
    turtle_instance.penup()

# Function to draw the letter R
def draw_R(turtle_instance):
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(100)  # Vertical line
    turtle_instance.right(90)
    turtle_instance.forward(50)   # Move to the right
    turtle_instance.circle(-25, 180)  # Draw half circle
    turtle_instance.right(150)
    turtle_instance.forward(50)   # Diagonal line
    turtle_instance.penup()
    turtle_instance.right(90)

# Function to set position for drawing each letter
def set_position(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

# Set up the turtle
my_turtle.speed(1)  # Adjust speed (1 is slow, 10 is fast)
turtle.bgcolor("black")  # Set background color
my_turtle.color("white")  # Set turtle color

# Draw each letter with specific positions
set_position(-150, 0)  # Position for H
draw_H(my_turtle)

set_position(-70, 0)  # Position for A
draw_A(my_turtle)

set_position(-40, 0)  # Position for P
draw_P(my_turtle)

set_position(-10, 0)  # Position for P
draw_P(my_turtle)

set_position(20, 0)  # Position for Y
draw_Y(my_turtle)

set_position(-150, -50)  # Position for M
draw_M(my_turtle)

set_position(-80, -50)  # Position for O
draw_O(my_turtle)

set_position(-40, -50)  # Position for N
draw_N(my_turtle)

set_position(0, -50)  # Position for T
draw_T(my_turtle)

set_position(30, -50)  # Position for H
draw_H(my_turtle)

set_position(80, -50)  # Position for S
draw_S(my_turtle)

set_position(110, -50)  # Position for A
draw_A(my_turtle)

set_position(160, -50)  # Position for R
draw_R(my_turtle)

set_position(210, -50)  # Position for Y
draw_Y(my_turtle)

# Finish
my_turtle.hideturtle()  # Hide the turtle cursor
turtle.done()  # Keep the window open
