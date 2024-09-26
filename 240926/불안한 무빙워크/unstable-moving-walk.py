n, k = map(int, input().split())
array = list(map(int, input().split()))
nums = list(range(2 * n))
loc = [False] * (2 * n)
MAX_M = 2 * n

plst = []
def rotate():
    global nums

    num_temp = nums.pop()
    nums = [num_temp] + nums

    idx = nums[n - 1]
    if loc[idx]:
        loc[idx] = False
        plst.remove(idx)

def move():
    rlst = []
    for i in range(len(plst)):
        idx = plst[i]

        if loc[idx]:
            next_idx = (idx + 1) % MAX_M

            if not loc[next_idx] and array[next_idx] > 0:
                loc[next_idx] = True
                array[next_idx] -= 1
                loc[idx] = False
                plst[i] = next_idx

                if next_idx == nums[n - 1]:
                    loc[next_idx] = False
                    rlst.append(next_idx)

    if rlst:
        plst.pop(0)

def put():
    idx = nums[0]

    if not loc[idx] and array[idx] > 0:
        loc[idx] = True
        array[idx] -= 1
        if idx not in plst:
            plst.append(idx)

def simulate():
    # 무빙워크 1칸 회전
    rotate()

    # 무빙워크 내 사람 이동
    move()

    if end():
        return

    # 사람 한명 올림
    put()

    if end():
        return

def end():
    cnt = 0
    for i in range(MAX_M):
        if array[i] == 0:
            cnt += 1

    if cnt >= k:
        return True

    return False

ans = 0
while not end():
    ans += 1
    simulate()

print(ans)