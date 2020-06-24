from collections import deque

exam_log = deque()
passed_students = deque()


def queue_manipulation(issue):
    global exam_log
    if issue[0] == "READY":
        exam_log.appendleft(issue[1])
    if issue[0] == "EXTRA":
        exam_log.appendleft(exam_log.pop())
    if issue[0] == "PASSED" and len(exam_log) > 0:
        passed_students.appendleft(exam_log.pop())


n = int(input())

for _ in range(n):
    queue_manipulation(input().split())

for _r in range(len(passed_students)):
    print(passed_students.pop())
