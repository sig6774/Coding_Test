"""
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
"""

"""
1. brown과 yellow를 더했을 때 값과 곱했을 때 그 값이 같은 조합 찾기
2. 찾은 조합 중 가로가 세로보다 같거나 큰 조합만 추출 
3. row -2 * column -2의 값이 yellow값과 같은 애들 찾기
"""

# brown = 8
# yellow = 1

# row_col_value = dict()
# total = brown + yellow

# for i in range(2, (total // 2 +1)):
#     if total % i == 0:
#         if i >= total // i:
#             row_col_value[i] = total // i

# # print(row_col_value)
        
# for k, v in row_col_value.items():
#     if (k - 2) * (v - 2) == yellow:
#         print([k,v])

def solution(brown, yellow):
    
    answer = []
    row_col_value = dict()

    total = brown + yellow

    # 반으로 나눠서 하면 연산량 줌
    for i in range(2, (total // 2 +1)):
        if total % i == 0:
            if i >= total // i:
                row_col_value[i] = total // i
    
    for k, v in row_col_value.items():
        if (k - 2) * (v - 2) == yellow:
            answer.append(k)
            answer.append(v)
    
    return answer

brown = 24
yellow = 24
print(solution(brown=brown, yellow=yellow))