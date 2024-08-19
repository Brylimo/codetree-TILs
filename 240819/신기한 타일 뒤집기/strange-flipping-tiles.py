OFFSET = 10000
MAX_R = 20001
n = int(input())

cur = 0
segments = []
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'R':
        color = 'b'
        segment_left = cur
        segment_right = cur + distance
        cur += distance
    elif direction == 'L':
        color = 'w'
        segment_left = cur - distance
        segment_right = cur
        cur -= distance

    segments.append((color, segment_left, segment_right))

line = [0] * MAX_R
for color, segment_left, segment_right in segments:
    for i in range(OFFSET + segment_left, OFFSET + segment_right):
        if color == 'w':
            line[i] = 1
        elif color == 'b':
            line[i] = 2

w_cnt = 0
b_cnt = 0
for i in range(MAX_R):
    if line[i] == 1:
        w_cnt += 1
    elif line[i] == 2:
        b_cnt += 1

print(w_cnt, b_cnt)