import sys
string = list(input())

n = len(string)

def encode():
    alter = ''

    cnt = 0
    for i in range(n - 1):
        if string[i] != string[i + 1]:
            alter += f'{string[i]}{cnt + 1}'
            cnt = 0
        else:
            cnt += 1

    if cnt >= 0:
        alter += f'{string[-1]}{cnt + 1}'

    return len(alter)

ans = sys.maxsize
for _ in range(n - 1):
    ans = min(ans, encode())

    temp = string[-1]

    for i in range(n - 1, 0, -1):
        string[i] = string[i - 1]

    string[0] = temp

print(ans)