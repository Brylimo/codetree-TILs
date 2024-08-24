n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

cost = 0
for i in range(n - 1):
    if a_list[i] > b_list[i]:
        diff = a_list[i] - b_list[i]
        cost += diff

        a_list[i+1] += diff 

print(cost)