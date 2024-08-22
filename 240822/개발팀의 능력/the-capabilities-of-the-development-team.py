import sys

n = 5
members = list(map(int, input().split()))

ans = sys.maxsize
total = sum(members)
for i in range(n):
    for j in range(i + 1, n):
        for a in range(n):
            for b in range(a + 1, n):
                if i == a or i == b or j == a or j == b:
                    continue

                one = members[i] + members[j]
                two = members[a] + members[b]
                three = total - one - two

                if not (one == two or one == three or two == three):
                    min_value = min(one, two, three)
                    max_value = max(one, two, three)

                    ans = min(ans, max_value - min_value)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)