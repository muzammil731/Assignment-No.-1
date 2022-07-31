#Test Case 4

import doctest

def greater(x,y):

    """
>>> greater(9,2)
True
>>> greater(143,8)
True
>>> greater(8,10)
True
    """
    
    return x>y 

doctest.testmod()
