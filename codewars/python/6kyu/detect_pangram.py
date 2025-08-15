'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(st):
    # Brute force
    # Iterate over string array
    # Need to keep track of the words in the sentence. 

    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    
    for letter in st:
       if letter.lower() in alphabet:
           alphabet[letter.lower()] += 1

    for _, val in alphabet.items():
        if val <= 0: return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog."))
# is_pangram("Cwm fjord bank glyphs vext quiz")
# is_pangram("Pack my box with five dozen liquor jugs.")
# is_pangram("How quickly daft jumping zebras vex.")
# is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ")