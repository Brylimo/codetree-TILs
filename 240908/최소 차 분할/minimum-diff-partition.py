from itertools import combinations

n = int(input())
numbers = list(map(int, input().split(' ')))
total = sum(numbers)

worst = total - 2 * min(numbers)

def loop():
    answer = worst
    for num_a in range(1, n // 2 + 1):
        for group_a in combinations(numbers, num_a):
            loss = abs(total - 2 * sum(group_a))
            if loss < answer:
                answer = loss
                if answer == 0:
                    return answer
    return answer

print(loop())