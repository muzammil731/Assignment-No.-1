#Test Case 3

import doctest

def mod(x,y):

    """
>>> mod(9,2)
1
>>> mod(143,8)
5
>>> mod(68,10)
4
    """
    
    return x%y 

doctest.testmod()
