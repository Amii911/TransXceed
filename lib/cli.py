from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    print('Thanks for using my CLI')
    