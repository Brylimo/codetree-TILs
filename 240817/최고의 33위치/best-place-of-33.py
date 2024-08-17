n = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n - 3 + 1):
    for j in range(n - 3 + 1):
        sum_value = 0
        for a in range(3):
            for b in range(3):
                sum_value += graph[i + a][j + b]

        result = max(result, sum_value)

print(result)