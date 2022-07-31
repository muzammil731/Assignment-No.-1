#Test Case 5

import doctest

def square(x):

    """
>>> square(9)
18
>>> square(14)
196
>>> square(8)
64
    """
    
    return x*x

doctest.testmod()
