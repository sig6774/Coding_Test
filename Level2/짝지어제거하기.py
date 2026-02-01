"""
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.

입출력 예
s	result
baabaa	1
cdcd	0
입출력 예 설명
입출력 예 #1
위의 예시와 같습니다.
입출력 예 #2
문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.
"""

"""
1. 문자열 개수가 홀수이면 바로 0 리턴
2. 문자열 개수 // 2 의 몫만큼 반복 수행
3. 앞,뒤 문자가 같은지 확인
4. 같으면 그 문자 인덱스 번호들과 문자를 받아서 제거하는 함수 실행 후 제거된 문자 리턴
5. 반복 수행이 끝날때까지 문자열이 남아 있으면 0 리턴
"""

def solution(s):
    def del_strs(idx_1, idx_2, st):
        if idx_1 > 0:
            start_str = st[:idx_1]
        else:
            start_str = ""
        
        total_str = start_str + st[idx_2+1:]
        return total_str
    
    total_exec_cnt = len(s)

    if total_exec_cnt % 2 != 0:
        return 0
    else:

        for _ in range(total_exec_cnt):
            for idx in range(len(s)-1):
                if s[idx] == s[idx+1]:
                    s = del_strs(idx, idx+1, s)
                    break 

        if len(s) == 0:
            return 1
        else:
            return 0

a = "baabaa"

print(solution(a))

# 시간초과 되는 케이스 존재

"""
1. stack 형태로 데이터 append
2. 마지막 넣은 것과 현재 값이 같으면 pop 아니면 append
3. 남아 있는 stack 데이터가 존재하면 0 아니면 1
"""

def solution(s):
    stk_lst = [] 
    for ele in s:
        if len(stk_lst) == 0:
            stk_lst.append(ele)
        else:
            if stk_lst[-1] == ele:
                stk_lst.pop()
    
    if len(stk_lst) == 0:
        return 1
    else:
        return 0

a = "cdcd"
print(solution(a))
