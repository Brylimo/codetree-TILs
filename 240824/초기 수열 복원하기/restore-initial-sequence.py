import sys

n = int(input())
array = list(map(int, input().split()))

numbers = [0] * n

# a 경우의 수
for i in range(1, n+1):
    # b 경우의 수
    for j in range(1, n+1):
        if i == j:
            continue
        
        numbers[0] = i 
        numbers[1] = j

        goback = False
        temp = [i, j]
        for k in range(n - 2):
            numbers[k + 2] = numbers[k] + array[k + 1] - array[k]
            
            if numbers[k + 2] in temp or numbers[k+2] < 1:
                goback = True
                break
            else:
                temp.append(numbers[k + 2])

        if goback:
            continue

        goback = False
        for k in range(n - 2):
            if numbers[k] + numbers[k + 1] != array[k]:
                goback = True
                break

        if goback:
            continue

        # succeed
        for t in range(n):
            print(numbers[t], end=" ")
        sys.exit(0)