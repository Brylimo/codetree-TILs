n = int(input())
blocks = []
for _ in range(n):
    blocks.append(int(input()))
blocks.reverse()

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

temp = [0] * n

end_of_block = n
end_of_temp = 0
for i in range(n):
    if n - e1 <= i <= n - s1:
        pass
    else:
        temp[end_of_temp] = blocks[i]
        end_of_temp += 1

temp2 = [0] * n
end_of_temp2 = 0
for i in range(end_of_temp):
    if end_of_temp - e2 <= i <= end_of_temp - s2:
        pass
    else:
        temp2[end_of_temp2] = blocks[i]
        end_of_temp2 += 1

print(end_of_temp2)
for i in range(end_of_temp2 - 1, -1, -1):
    print(temp2[i])