# write your code here
from collections import deque


def solve_power(*operands):
    return operands[1] ** operands[0]


def solve_division(*operands):
    return operands[1] / operands[0]


def solve_multiplication(*operands):
    return operands[1] * operands[0]


def solve_subtraction(*operands):
    return operands[1] - operands[0]


def solve_addition(*operands):
    return sum(operands)


def has_substitution(our_string):
    for key in _variables:
        if key in our_string:
            return True
    return False


def has_power(our_string):
    if "^" in our_string:
        return True
    return False


def has_addition(our_string):
    if "+" in our_string:
        return True
    return False


def has_subtraction(our_string):
    if "-" in our_string:
        return True
    return False


def has_multiplication(our_string):
    if "*" in our_string:
        return True
    return False


def has_division(our_string):
    if "/" in our_string:
        return True
    return False


def has_numbers(our_string):
    return any(char.isdigit() for char in our_string)


def find_arithmetic(our_string):
    if has_addition(our_string):
        return True
    if has_subtraction(our_string):
        return True
    if has_multiplication(our_string):
        return True
    if has_division(our_string):
        return True
    if has_power(our_string):
        return True
    return False


def solve_input(_input):
    try:
        if _input == "":
            return []
        elif _input.startswith("/"):
            if _input == "/exit" or _input == "/help":
                solve_command(_input)
                return _input
            else:
                raise Exception("Unknown command")
        elif "=" in _input or not find_arithmetic(_input):
            if not normal_identifier(_input):
                raise Exception("Invalid identifier")
            if not normal_variables(_input):
                raise Exception("Unknown variable")
            if "=" in _input and not normal_assignment(_input):
                raise Exception("Invalid assignment")
            if "=" not in _input:
                print(_variables[_input])
                return _input
            if "=" in _input:
                solve_assignment(_input.split("="))
                return _input
        elif not normal_expression(_input):
            raise Exception("Invalid expression")
        answer = solve_postfix(to_postfix(compose_equation(_input)))
        print(answer)
        return answer
    except Exception as e:
        print(str(e))
        return []


def normal_identifier(_input):
    for letter in _input.split("=")[0]:
        if not (91 > ord(letter) > 64 or 123 > ord(letter) > 96 or ord(letter) == 32):
            return False
    return True


def normal_variables(_input):
    if "=" not in _input and _input not in _variables:
        return False
    elif "=" in _input and (_input.split("=")[1].split()[0] not in _variables and not has_numbers(_input)):
        return False
    return True


def normal_assignment(_input):
    for letter in _input.split("=")[1]:
        if(not (58 > ord(letter) > 47 or ord(letter) == 32) or _input.count("=") > 1) and (not _input.split("=")[1].split()[0] in _variables):
            return False
        if("=" in _input) > 1:
            return False
    return True


def normal_expression(_input):
    if _input.endswith("+") or _input.endswith("-") or _input.endswith("*") or _input.endswith("/") or _input.endswith("^"):
        return False
    if not find_arithmetic(_input):
        return False
    if _input.count("(") != _input.count(")"):
        return False
    previous_element = ""
    for element in _input:
        if (element == "*" or element == "/") and (previous_element == "*" or previous_element == "/"):
            return False
        if (element not in operators and not element.isdecimal() and element not in _variables) and element != " ":
            return False
        previous_element = element
    return True


def solve_command(_input):
    global flag
    if _input == "/exit":
        flag = False
    elif _input == "/help":
        print("The program calculates the sum, subtraction, multiplication, division and power of numbers and variables")


def solve_assignment(_input):
    global _variables
    if _input[1].split()[0] in _variables:
        _variables[_input[0].split()[0]] = _variables[_input[1].split()[0]]
    else:
        _variables[_input[0].split()[0]] = _input[1].split()[0]


def compose_equation(_input_eq):
    number = ""
    sign = ""
    _e = 0
    equation = []
    while _e in range(len(_input_eq)):
        if _input_eq[_e] != " ":
            if _input_eq[_e] == "-" and (_input_eq[_e+1] and _input_eq[_e+1].isdecimal()) and ((_input_eq[_e-1] and _input_eq[_e-1] == " ") and (_input_eq[_e-2] and _input_eq[_e-2] in operators)) or _e == 0:
                number += _input_eq[_e]
            elif _input_eq[_e] == "(" or _input_eq[_e] == ')':
                if "-" in sign and len(sign) % 2 == 0:
                    equation.append("+")
                elif len(sign) != 0:
                    equation.append(sign[0])
                elif len(number) != 0:
                    equation.append(number[0])
                number = ""
                sign = ""
                equation.append(_input_eq[_e])
            elif _input_eq[_e] not in operators:
                if len(sign) != 0:
                    if "-" in sign and len(sign) % 2 == 0:
                        equation.append("+")
                    else:
                        equation.append(sign[0])
                    sign = ""
                number += _input_eq[_e]
            else:
                if len(number) != 0:
                    equation.append(number)
                    number = ""
                sign += _input_eq[_e]
        _e += 1
    if len(number) != 0:
        equation.append(number)
    return equation


def to_postfix(equation):
    postfix = deque()
    answer = deque()
    for element in equation:
        if element not in operators or element in _variables:    # Operands
            answer.append(element)
        else:   # Operators
            if len(postfix) == 0 or (postfix and postfix[-1] == "("):
                postfix.append(element)
            elif element == "(":
                postfix.append(element)
            elif element == ")":
                while True:
                    if postfix[-1] != "(":
                        answer.append(postfix.pop())
                    else:
                        postfix.pop()
                        break
            elif postfix and is_precedence(element, postfix[-1]):
                postfix.append(element)
            elif postfix and not is_precedence(element, postfix[-1]):
                while True:
                    if postfix and (is_precedence(element, postfix[-1]) or postfix[-1] != "(") and postfix[-1] in operators:
                        answer.append(postfix.pop())
                    else:
                        postfix.append(element)
                        break
    postfix.reverse()
    for element in postfix:
        answer.append(element)
    return answer


def solve_postfix(postfix_equation):
    answer = deque()
    for element in postfix_equation:
        if element not in operators and element not in _variables:
            answer.append(element)
        elif element in _variables:
            answer.append(_variables[element])
        else:
            if element == "+":
                answer.append(solve_addition(int(answer.pop()), int(answer.pop())))
            elif element == "-":
                answer.append(solve_subtraction(int(answer.pop()), int(answer.pop())))
            elif element == "*":
                answer.append(solve_multiplication(int(answer.pop()), int(answer.pop())))
            elif element == "/":
                answer.append(solve_division(int(answer.pop()), int(answer.pop())))
            elif element == "^":
                answer.append(solve_power(int(answer.pop()), int(answer.pop())))
    return answer[-1]


def is_precedence(_element1, stacked_element):
    if operators[_element1] > operators[stacked_element]:
        return True
    return False


def menu():
    while flag:
        solve_input(input())
    else:
        print("Bye!")


operators = {"(": 0, ")": 0, "^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
_variables = {}
flag = True
menu()
