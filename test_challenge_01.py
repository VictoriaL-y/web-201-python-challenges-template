# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count_vowels = 0
    for letter in word:
        if letter == 'a' or 'e' or 'i' or 'o' or 'u': 
            count_vowels = count_vowels + 1
    return count_vowels

def test_challenge_01_happy_case(): 
     assert count_vowels('Kaleidoscope') == 12   