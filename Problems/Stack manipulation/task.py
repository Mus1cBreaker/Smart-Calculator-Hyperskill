from collections import deque

operations = deque()


def stack_manipulation(command):
    global operations
    if command[0] == "PUSH":
        operations.append(command[1])
    if command[0] == "POP" and len(operations) > 0:
        operations.pop()


n = int(input())

for _ in range(n):
    stack_manipulation(input().split())

for _r in range(len(operations)):
    print(operations.pop())