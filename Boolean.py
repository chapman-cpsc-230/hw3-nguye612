"""
File: <booleans.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Translating Boolean expressions.>
"""
C = 41
#The value of C is 41.
C == 40
#False, Value is 41.
C != 40 and C < 41
#True, The value of C is not equal to 40 and is less than 41.
C != 40 or C < 41
#True, The value of C is either not equal to 40 or less than 41.
not C == 40
#True, The value of C is not equal to 40
not C > 40
#False The value of C is not greater than 40
C <= 41
#True, The value is less than 41.
not False
#True
True and False
#False
False or True
#The result is True.
False or False or False
#The result is False
True and True and False
#The result is False
False == 0
#True
True == 0
#False
True == 1
#True
