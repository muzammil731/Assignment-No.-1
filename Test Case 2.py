#Test Case 2

import doctest

def divide(x,y,):

    """
>>> divide(24,6)
2.0
>>> divide(150,10)
18.0
>>> divide(8,2)
4.0
    """
    
    return x/y 

doctest.testmod()
