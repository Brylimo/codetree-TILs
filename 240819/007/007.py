class Object:
    def __init__(self, code, place, time):
        self.c = code
        self.p = place
        self.t = time

code, place, time = input().split()
o = Object(code, place, time)

print(f'secret code : {o.c}')
print(f'meeting point : {o.p}')
print(f'time : {o.t}')