# put your python code here
import string
keys = list(string.ascii_lowercase)
temp = {}
for letter in keys:
    temp[letter] = letter + letter
double_alphabet = temp