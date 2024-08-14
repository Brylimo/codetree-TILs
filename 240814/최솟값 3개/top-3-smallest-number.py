import heapq

n = int(input())
array = list(map(int, input().split()))

heap = []
for num in array:
    heapq.heappush(heap, num)

    if len(heap) >= 3:
        sum_val = 1
        temp_arr = []
        for _ in range(3):
            temp = heapq.heappop(heap)
            sum_val *= temp
            temp_arr.append(temp)
        
        print(sum_val)

        for temp_val in temp_arr:
            heapq.heappush(heap, temp_val)
    else:
        print(-1)