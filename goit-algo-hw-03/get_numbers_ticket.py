import random

# generating a sorted list of unique random numbers
def get_numbers_ticket(min:int, max:int, quantity:int)->list[int]:
    """
    Function parameters:
    min - the minimum possible number in the set (not less than 1).
    max - the maximum possible number in the set (not more than 1000).
    quantity - the number of numbers to be selected (a value between min and max).

    The function generates the specified number of unique numbers in the specified range.
    The function returns a list of randomly selected, sorted numbers. The numbers in the set must not be repeated. 
    If the parameters do not meet the specified constraints, the function returns an empty list. 
    """
   
    if min < 1 or max > 1000 or min >= max:
        return ['/']
    available = max - min + 1

    if quantity <= 0 or quantity > available:
        return ['/']
    
    return sorted(random.sample(range(min, max + 1), quantity))




print(get_numbers_ticket(10, 1000, 5))
print(get_numbers_ticket(0, 1000, 12))
print(get_numbers_ticket(0, 1001, 5))
print(get_numbers_ticket(10, 1005, 17))
print(get_numbers_ticket(-55, 125, 7))
print(get_numbers_ticket(10, 4, 5))
print(get_numbers_ticket(10, 14, 6 ))

