import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(200):
		# pen.speed(200-i)
		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)
        

# Defining method to draw a full heart
def heart():
	# pen.speed(200)

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-85, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('white')

	# Write the specified text in
	# specified font style and size
	pen.write("Aami tumaake bhalo baashi", font=(
	"Verdana", 9
        , "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()
