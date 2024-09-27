n, k = map(int, input().split())
seq = list(map(int, input().split()))

root = seq[0]
nxt_parent = root

nodes = [root]
parents = [-1] * 1000001
child = [[] for _ in range(1000001)]

def get_next_idx(x):
    for j in range(x, n - 1):
        if seq[j] + 1 != seq[j + 1]:
            return j

    return n - 1

i = 1
while i < n:
    j = get_next_idx(i)

    for t in range(i, j + 1):
        parents[seq[t]] = nxt_parent
        child[nxt_parent].append(seq[t])
        nodes.append(seq[t])

    i = j + 1

    for node in nodes:
        if not child[node]:
            nxt_parent = node
            break

father = parents[k]
grand_father = -1
if father != -1:
    grand_father = parents[father]

flst = child[grand_father]

ans = 0
for fa in flst:
    if fa != father:
       ans += len(child[fa])

print(ans)