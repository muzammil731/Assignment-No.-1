#Test Case 1

import doctest

def multiply(x,y,z):

    """
>>> multiply(2,3,4)
24
>>> multiply(1,5,2)
8
>>> multiply(7,8,2)
100
    """
    
    return x*y*z 

doctest.testmod()
