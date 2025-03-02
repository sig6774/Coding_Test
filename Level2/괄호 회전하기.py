"""
문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.

입출력 예
s	result
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
"""

"""
1. 0 ~ (문자열 길이 -1)의 숫자 사이에서 1칸씩 왼쪽에서 오른쪽으로 이동
2. 열린 기호를 큐에 넣고 닫히는 기호가 매칭이 되면 열린 기호 데이터 빼기
3. 만약 큐에 데이터가 남아있으면 패스 없으면 +1 
"""

from collections import deque
# s= "[](){}"
# s = "}]()[{"	
# s = "[)(]"	
# s = "}}}"	
# value_lst = deque(s)
# cnt = 0
# for num in range(len(s)):
#     # print(value_lst)
#     new_li = deque()
#     pop_li = []
#     for q_v in value_lst:
#         if q_v in ('[', '(', '{'):
#             new_li.append(q_v)

#         if len(new_li) > 0:
#             if new_li[-1] == '[' and q_v == ']':
#                 pop_li.append(new_li.pop())
#             elif new_li[-1] == '{' and q_v == '}':
#                 pop_li.append(new_li.pop())
#             elif new_li[-1] == '(' and q_v == ')':
#                 pop_li.append(new_li.pop())
#         else:
#             new_li.append(q_v)
#     # if len(new_li) == len(pop_li) and len(pop_li) != 0:
#     if len(new_li) == 0:
#         cnt += 1

#     first_v = value_lst.popleft()
#     value_lst.append(first_v)

# print(cnt)

def solution(s):
    from collections import deque

    answer = 0

    value_lst = deque(s)

    for num in range(len(s)):
        # print(value_lst)
        new_li = deque()
        pop_li = []

        for q_v in value_lst:
            if q_v in ('[', '(', '{'):
                new_li.append(q_v)

            if len(new_li) > 0:
                if new_li[-1] == '[' and q_v == ']':
                    pop_li.append(new_li.pop())
                elif new_li[-1] == '{' and q_v == '}':
                    pop_li.append(new_li.pop())
                elif new_li[-1] == '(' and q_v == ')':
                    pop_li.append(new_li.pop())
            else:
                new_li.append(q_v)

        if len(new_li) == 0:
            answer += 1

        first_v = value_lst.popleft()
        value_lst.append(first_v)

    return answer
# s= "[](){}"
# s = "}]()[{"	
# s = "[)(]"	
s = "}}}"	

print(solution(s=s))