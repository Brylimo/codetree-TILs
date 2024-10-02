n, q = map(int, input().split())

parents = None
tree = [-1] * (2 ** 20 - 1)
authority = [0] * (n + 1)
alarms = [True] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

def init(inp):
    global parents

    parents = [0] + inp[:n]
    authority_inp = inp[n:len(inp)]

    for i in range(n):
        graph[parents[i + 1]].append(i + 1)
        graph[i + 1].append(parents[i + 1])

        authority[i + 1] = authority_inp[i]

def alarm_switch(inp):
    c = inp[0]

    if alarms[c]:
        alarms[c] = False
    else:
        alarms[c] = True

def alter_authority(inp):
    c, power = inp[0], inp[1]

    authority[c] = power

def change_parent(inp):
    c1, c2 = inp[0], inp[1]

    graph[parents[c1]].remove(c1)
    graph[parents[c2]].remove(c2)

    graph[parents[c1]].append(c2)
    graph[parents[c2]].append(c1)

    parents[c1], parents[c2] = parents[c1], parents[c2]

count = 0
def dfs(x, depth):
    global count

    for i in graph[x]:
        if visited[i]:
            continue

        if parents[x] == i:
            continue

        visited[i] = True
        if not alarms[i]:
            continue

        if authority[i] >= depth:
            count += 1
            dfs(i, depth + 1)
        else:
            dfs(i, depth + 1)

def browse(inp):
    global count, visited

    c = inp[0]
    count = 0
    visited = [False] * (n + 1)

    visited[c] = True
    dfs(c, 1)

for _ in range(q):
    option, *inp = list(map(int, input().split()))

    if option == 100:
        init(inp)
    elif option == 200:
        alarm_switch(inp)
    elif option == 300:
        alter_authority(inp)
    elif option == 400:
        change_parent(inp)
    elif option == 500:
        browse(inp)
        print(count)