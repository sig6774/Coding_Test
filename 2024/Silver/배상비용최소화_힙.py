"""
문제 설명
OO 조선소에서는 태풍으로 인한 작업지연으로 수주한 선박들을 기한 내에 완성하지 못할 것이 예상됩니다. 
기한 내에 완성하지 못하면 손해 배상을 해야 하므로 남은 일의 작업량을 숫자로 매기고 배상비용을 최소화하는 방법을 찾으려고 합니다.
배상 비용은 각 선박의 완성까지 남은 일의 작업량을 제곱하여 모두 더한 값이 됩니다.

조선소에서는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있습니다. 
조선소에서 작업할 수 있는 N 시간과 각 일에 대한 작업량이 담긴 배열(works)이 있을 때 배상 비용을 최소화한 결과를 반환하는 함수를 만들어 주세요. 
예를 들어, N=4일 때, 선박별로 남은 일의 작업량이 works = [4, 3, 3]이라면 배상 비용을 최소화하기 위해 일을 한 결과는 [2, 2, 2]가 되고 배상 비용은 22 + 22 + 22 = 12가 되어 12를 반환해 줍니다.

제한사항
일할 수 있는 시간 N : 1,000,000 이하의 자연수
배열 works의 크기 : 1,000 이하의 자연수
각 일에 대한 작업량 : 1,000 이하의 자연수
"""

"""
1. 최소 힙을 가지고 올 수 있는 것을 착안해서 최대 힙 구함 
2. 남은 work 기간동안 최대 힙을 2까지 만드는 방식을 반복
3. 1~2의 과정을 반복
"""


def solution(no, works):
    import heapq
    if no > sum(works):
        return 0

    heap = []
    result = 0

    for num in works:
        heapq.heappush(heap, (-num, num))

    while no != 0:

        max_value = heapq.heappop(heap)[1]
        if max_value != 2:
            max_value -= 1
            no -= 1
            heapq.heappush(heap, (-max_value, max_value))

    for k,v in heap:
        result += (k * k)

    return result

# 88.4 / 100
# 아마 2로 확정한 것이 에러 케이스에 걸린 것 같음


def solution2(no, works):
    import heapq

    if no > sum(works):
        return 0

    works = [-i for i in works]
    # max heap
    heapq.heapify(works)

    for _ in range(no):
        heapq.heapreplace(works, works[0] + 1)
        # heappushpop 먼저 푸시하고 팝
        # heapreplace 먼저 팝하고 푸시

    return sum([i ** 2 for i in works])
