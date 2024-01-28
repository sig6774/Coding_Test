'''
문제 설명
올바른 괄호란 두 개의 괄호 '(' 와 ')' 만으로 구성되어 있고, 괄호가 올바르게 짝지어진 문자열입니다. 괄호가 올바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 합니다.
예를들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
'''

'''
순서
1. )가 첫번째로 들어오는지 체크 
2. (라면 빈 리스트에 append 
3. )라면 리스트의 값 pop 
4. 리스트의 개수가 0이라면 True, 아니라면 False 
5. 리스트의 값이 없는데 pop을 할 수 있는 가능성이 있으므로 리스트의 개수 계속 체크 
'''

def solution(s):
    
    if s[0] == ')':
        return False 

    check_list = []

    for i in range(len(s)):
        if s[i] == '(':
            check_list.append(s[i])
        
        elif s[i] == ')': 
            if len(check_list) != 0:
                check_list.pop()
            else:
                return False
        
    if len(check_list) == 0:
        return True
    
    else:
        return False

# 정답 