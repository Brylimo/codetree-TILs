import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())

answer = []

def print_answer():
    for num in answer:
        print(num, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(1, k + 1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)