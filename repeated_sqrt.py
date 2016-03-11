"""
File: <repeated_sqrt.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Determining round off errors and applying square root function.>
"""
from math import sqrt
for n in range(1,60):
   r = 2.0
for i in range(n):
   r = sqrt(r)      #variable r is equal to the square root of r
for i in range(n):
   r = r**2    #r^2
print '%d times sqrt and **2: %.16f' % (n,r)



from math import sqrt
for n in range(1,25):
   r = 2.0
for i in range(n):
   r = sqrt(r)
for i in range(n):
   r = r**2   #r^2
print '%d times sqrt and **2: %.16f' % (n,r)
#The program takes the range of (0,60) and sets the value to 2.0. It takes
#the square root of a number n times then squares number n times. In the end
#the result is the same number you started with. The loop repeats 59 times
#which results in a round off error or bug.
