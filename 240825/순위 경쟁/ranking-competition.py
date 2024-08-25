n = int(input())

cnt = 0
a, b, c = 0, 0, 0
status = ['a', 'b', 'c']
for _ in range(n):
    cs, s = input().split()
    s = int(s)

    if cs == 'A':
        a += s
    elif cs == 'B':
        b += s 
    elif cs == 'C':
        c += s

    temp = []
    if a == b == c:
        temp.append('a')
        temp.append('b')
        temp.append('c')
    elif a == b and b > c:
        temp.append('a')
        temp.append('b')
    elif b == c and b > a:
        temp.append('b')
        temp.append('c')
    elif a == c and a > b:
        temp.append('a')
        temp.append('c')
    elif a > b and a > c:
        temp.append('a')
    elif b > a and b > c:
        temp.append('a')
    elif c > b and c > a:
        temp.append('c')

    if sorted(temp) != sorted(status):
        cnt += 1
        status = temp

print(cnt)