"""
File: <turtlepoly.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Program will draw a polygon given number of sides and length.>
"""
import turtle

# Ask user for input here.
num_sides_inp = raw_input("Please enter a number of sides: ")
num_sides = int(num_sides_inp)
side_len_inp = raw_input("Please enter a length: ")
side_len = int(side_len_inp)
# Now create a graphics window.
t = turtle.Pen()

for side in range(num_sides):
   t.forward(side_len)
   t.left(360.0/num_sides)
# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Please hit <enter> to quit...")

# Now remove the graphics window before exiting.
turtle.bye()
