"""
File: <turtlestar.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Program will draw a star given number for points (odd numbers only) and length.>
"""
import turtle
Stephanie= turtle.Pen()

num_sidesinp= raw_input ("Please enter an odd number of sides:")
num_sides = int(num_sidesinp)
lengthinp = raw_input ("Please enter the natural number length:")
length = int(lengthinp)

for side in range(num_sides):

       Stephanie.forward(length)
       Stephanie.left(180.0-(180.0/num_sides))


# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Please hit <enter> to Exit...")
#Remove graphics window before exiting.
turtle. bye()
