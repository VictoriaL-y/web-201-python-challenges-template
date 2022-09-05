# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".

def duplicate_characters(str):
    newWord = ""
    for letter in str:
        newWord = newWord + letter * 2
    return newWord

def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'