import sys

input = sys.stdin.readline

n = int(input().rstrip())

cnt = 0
answer = []


def choose(curr_num):
    global cnt

    if curr_num == n + 1:
        digit_cnt = 1
        flag = False

        for i in range(len(answer)):
            if len(answer) > 1 and i < len(answer) - 1 and answer[i] == answer[i + 1]:
                digit_cnt += 1
                continue
            else:
                if digit_cnt < answer[i] or digit_cnt % answer[i] != 0:
                    flag = True
                    break

                digit_cnt = 1

        if not flag:
            cnt += 1

        return

    for i in range(1, 5):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return


choose(1)

print(cnt)