OFFSET = 100000
MAX_R = 200001

n = int(input())

cur = 0
segments = []
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        segment_left = cur - distance + 1
        segment_right = cur
        cur -= distance - 1
        color = 'w'
    elif direction == 'R':
        segment_left = cur
        segment_right = cur + distance - 1
        cur += distance - 1
        color = 'b'

    segments.append((color, segment_left, segment_right))

line = [[0] * 3 for _ in range(MAX_R)]
for color, segment_left, segment_right in segments:
    if color == 'w':
        for i in range(segment_left, segment_right + 1):
            if not (line[i][0] >= 2 and line[i][1] >= 2):
                line[i][0] += 1
                line[i][2] = 1

            if line[i][0] >= 2 and line[i][1] >= 2:
                line[i][2] = 3
    elif color == 'b':
        for i in range(segment_left, segment_right + 1):
            if not (line[i][0] >= 2 and line[i][1] >= 2):
                line[i][1] += 1
                line[i][2] = 2

            if line[i][0] >= 2 and line[i][1] >= 2:
                line[i][2] = 3

w_cnt = 0
b_cnt = 0
g_cnt = 0
for i in range(MAX_R):
    if line[i][2] == 1:
        w_cnt += 1
    elif line[i][2] == 2:
        b_cnt += 1
    elif line[i][2] == 3:
        g_cnt += 1

print(w_cnt, b_cnt, g_cnt)