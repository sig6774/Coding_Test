"""
사탕 담기

문제 설명
m 그램(gram)을 담을 수 있는 가방에 사탕을 가득 채우는 경우의 수를 구하려 합니다. 단, 같은 사탕은 또 넣을 수 없습니다.

가방이 감당할 수 있는 무게 m, 사탕별 무게가 담긴 배열 weights가 매개변수로 주어질 때, 가방을 정확히 m 그램으로 채우는 경우의 수를 return 하는 solution 함수를 작성해주세요.

제한 조건
m은 1,000 이상 100,000 이하인 자연수입니다.
모든 사탕의 무게는 10 이상 100,000 이하인 자연수입니다.
weights의 길이는 3 이상 15 이하입니다.
입출력 예
m	weights	return
3000	[500, 1500, 2500, 1000, 2000]	3
입출력 예 설명
사탕을 하나씩 선택해 3000 그램으로 만드는 방법은 [500, 1000, 1500], [1000, 2000], [500, 2500] 으로 3가지입니다.
"""

"""
1. 체크 리스트 생성 및 기입 
2. dfs 알고리즘 활용해서 모든 경우의 수 파악
"""

def solution(m, weights):
    cnt = 0  
    ch = [0] * len(weights)  

    def dfs(v):
        nonlocal cnt  # dfs에서 바깥 스코프의 cnt를 사용하겠다고 명시

        if v == len(weights):
            s = 0
            for i in range(len(weights)):
                if ch[i] == 1:
                    s += weights[i]
            if s == m:
                cnt += 1
        else:
            ch[v] = 1
            dfs(v + 1)
            ch[v] = 0
            dfs(v + 1)

    dfs(0)
    return cnt


print(solution(3000, [500, 1500, 2500, 1000, 2000]))