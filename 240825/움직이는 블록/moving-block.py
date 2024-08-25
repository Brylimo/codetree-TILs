import heapq

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

sum_value = sum(array)

each_val = sum_value // n

cnt = 0
for i in range(n):
    cnt += abs(array[i] - each_val)

print(cnt // 2)