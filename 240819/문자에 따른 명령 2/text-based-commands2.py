array = list(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0

direction = 0
for s in array:
    if s == 'L':
        direction = (direction + 4 - 1) % 4
    elif s == 'R':
        direction = (direction + 4 + 1) % 4
    elif s == 'F':
        x = x + dx[direction]
        y = y + dy[direction]

print(y, x)