def range_sum(numbers, a, b):
    sum_of_specified_elements = 0

    for number in numbers:
        if a <= int(number) <= b:
            sum_of_specified_elements += int(number)

    return sum_of_specified_elements


_numbers = input().split()
_a, _b = input().split()
print(range_sum(_numbers, int(_a), int(_b)))