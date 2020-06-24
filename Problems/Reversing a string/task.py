from collections import deque

n = int(input())

my_stack = deque()

for _e in range(n):
    my_stack.append(input())

for _e in range(n):
    print(my_stack.pop())
