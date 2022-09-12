# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

def extract_integers(mixed_list):
    newList = []
    for item in mixed_list:
        if type(item) == "number":
            newList = newList + item
    return newList

def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   