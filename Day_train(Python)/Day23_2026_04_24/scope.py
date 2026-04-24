def function_one():
    a = 1 
    print("a:" , a)
    def function_two():
        b = 2
        print("a:" , a)
        print("b:" , b)
    function_two()
function_one()

from math import e
def function_three():
    print(e)
    print(round(e))
function_three()