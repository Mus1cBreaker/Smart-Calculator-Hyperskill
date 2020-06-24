from collections import deque

issues = deque()


def queue_manipulation(issue):
    global issues
    if issue[0] == "ISSUE":
        issues.appendleft(issue[1])
    if issue[0] == "SOLVED" and len(issues) > 0:
        issues.pop()


n = int(input())

for _ in range(n):
    queue_manipulation(input().split())

for _r in range(len(issues)):
    print(issues.pop())