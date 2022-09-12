# Supermarket billing: Write a function in python that 
# takes a shopping list (dictionary of items and price) and returns the total.
# extension: apply discount accordingly:
# if total is greater than 50 Euros 5% discount.
# if total is greater than 60 Euros 6% discount.
# if total is greater than 70 Euros 7% discount and so on.

def calculate_bill(shopping_list):
    total = 0
    for x in shopping_list:
        total = total + shopping_list[x]
    if total > 70:
        total = round((total * 0.93), 3)
    elif total > 60:
        total = round((total * 0.94), 3)
    elif total > 50:
        total = round((total * 0.95), 3)
    else: 
        total = total
    return total

def test_challenge_07_happy_case_1(): 
    shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == 43.4
def test_challenge_07_happy_case_2(): 
    shopping_list = {'apples':11.20, 'bananas':12.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == round((53.4 * 0.95), 3)
def test_challenge_07_happy_case_3(): 
    shopping_list = {'apples':11.20, 'bananas':22.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == round((63.4 * 0.94), 3)
def test_challenge_07_happy_case_4(): 
    shopping_list = {'apples':11.20, 'bananas':32.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == round((73.4 * 0.93), 3)
