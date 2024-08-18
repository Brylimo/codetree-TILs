a, b, c, d = map(int, input().rstrip().split())

time1 = 60 * a + b
time2 = 60 * c + d

print(time2 - time1)