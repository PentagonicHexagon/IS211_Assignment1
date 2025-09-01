def list_divide(numbers, divide=2):
    elements = 0
    for n in numbers:
        if n % divide == 0:
            elements += 1
    return elements

class ListDivideException(Exception):
    pass

def test_list_divide():
    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException("Failed")
    if list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException("Failed")
    if list_divide([30,54,63,98,100], 10) != 2:
        raise ListDivideException("Failed")
    if list_divide([]) != 0:
        raise ListDivideException("Failed")
    if list_divide([1,2,3,4,5], 1) != 5:
        raise ListDivideException("Failed")
    
test_list_divide()