class Device:
    def __init__(self, ta, tb):
        self.ta = ta
        self.tb = tb

n, c, g, h = map(int, input().split())

devices = []
for _ in range(n):
    ta, tb = map(int, input().split())
    devices.append(Device(ta, tb))

ans = 0
for i in range(1001):
    temp = 0
    for j in range(n):
        if devices[j].ta > i:
            temp += c 
        elif devices[j].ta <= i <= devices[j].tb:
            temp += g
        else:
            temp += h

    ans = max(ans, temp)

print(ans)