n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

answer = 0
cnt = 0
for i in range(len(array)):
    cnt += 1
    answer = max(answer, cnt)
    
    if i != 0 and array[i] != array[i - 1]:
        cnt = 0

print(answer)