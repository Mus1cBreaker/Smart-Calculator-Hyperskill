# put your python code here
# from collections import deque


def brackets_checker(code_string):
    brackets = []
    for letter in code_string:
        if letter == "(":
            brackets.append(letter)
        elif letter == ")":
            if len(brackets) > 0:
                brackets.pop()
            else:
                return "ERROR"
    if len(brackets) > 0:
        return "ERROR"
    return "OK"


code_input = input()

# brackets = deque()
print(brackets_checker(code_input))
