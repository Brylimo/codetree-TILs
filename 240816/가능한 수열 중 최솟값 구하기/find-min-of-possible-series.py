import sys

# 변수 선언 및 입력
n = int(input())
numbers = [4, 5, 6]

series = []

# 가능한 수열인지 여부를 판별합니다.
def is_possible_series():
    # 가능한 연속 부분 수열의 길이 범위를 탐색합니다.
    length = 1
    while True:
        # 연속 부분 수열의 시작과 끝 인덱스를 설정하여 줍니다.
        start1, end1 = len(series) - length, len(series) - 1
        start2, end2 = start1 - length, start1 - 1

        if start2 < 0:
            break

        # 인접한 연속 부분 수열이 같은지 여부를 확인합니다.
        if series[start1:end1 + 1] == series[start2:end2 + 1]:
            return False

        length += 1
    
    return True


def find_min_series(cnt):
    # n개의 숫자가 선택됐을 때 불가능한 수열인 경우 탐색을 종료합니다.
    # 가능한 수열인 경우 이를 출력하고 프로그램을 종료합니다.
    if cnt == n:
        for elem in series:
            print(elem, end = "")
        sys.exit(0)
    
    # 사용 가능한 각 숫자가 뽑혔을 때의 경우를 탐색합니다.
    for number in numbers:
        series.append(number)
        # 해당 시점까지 만들 수열이 조건을 만족하는 경우에만
        # 탐색을 진행합니다.
        if is_possible_series():
            find_min_series(cnt + 1)
        series.pop()
        

find_min_series(0)