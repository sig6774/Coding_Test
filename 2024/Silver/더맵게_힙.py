"""
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 1 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
"""

"""
순서
1. 스코빌 지수가 제일 낮은 음식과 그 다음으로 낮은 음식 추출 
2. 섞은 음식 스코빌 지수를 바탕으로 계산 후 입력값보다 같거나 높은지 파악하면서 count 진행 
3. 1~2번의 과정을 반복
"""

from collections import deque


def solution(scoville, K):
    count = 0
    new_scovile_value = 0

    while True:

        scoville.sort()
        scoville_list = deque(scoville)

        min_value = scoville_list.popleft()
        second_min_value = scoville_list.popleft()
        new_scovile_value = min_value + (second_min_value * 2)
        if new_scovile_value >= K:
            break
        else:
            count += 1
            scoville = list(scoville_list)
            scoville.append(new_scovile_value)

    answer = count + 1
    return answer

# 오답 (효율성 검사에서 시간초과)


from heapq import heapify, heappush, heappop


def solution2(scoville, K):
    # heap 자료구조로 변환
    heapify(scoville)
    count = 0

    while scoville[0] < K:
        try:
            # item을 heap에 추가하는데 추가하는 것이 heappop을 사용하여 가장 작은 원소 리턴하여 연산한 값을 추가
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        except IndexError:
            return -1
        count += 1
    return count

# 첫번째 있는 요소(가장 작은)가 K보다 크다면 이미 K를 넘었다는 개념으로 동작
# Heap을 사용하면 효율성 증대에 도움
