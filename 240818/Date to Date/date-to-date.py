m1, d1, m2, d2 = map(int, input().rstrip().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
time1 = 0
time2 = 0
for i in range(1, m1):
    time1 += num_of_days[i]
time1 += d1

for i in range(1, m2):
    time2 += num_of_days[i]
time2 += d2

print(time2 - time1 + 1)