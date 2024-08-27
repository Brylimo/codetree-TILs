import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()

gap = sys.maxsize
for i in range(n):
    one = array[i]
    two = array[i + n]

    gap = min(gap, abs(one - two))

print(gap)