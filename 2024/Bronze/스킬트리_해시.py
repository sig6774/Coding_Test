"""
문제 설명
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

제한 조건
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 "CBD"로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
"""

"""
순서
1. 스킬의 첫번째 원소가 있는 스킬트리만 추출 후 첫번쨰 원소가 있는 스킬트리부터 선택
2. 1번 과정 반복하면서 최종 남아있는 애들 list 개수 추출 
""" 

def solution(skill, skill_trees):
    
    for i in range(len(skill)):
        check_skill = [] 

        new_char = skill[i]

        for i in range(len(skill_trees)):

            if new_char in skill_trees[i]:

                text_num = skill_trees[i].find(new_char)

                if text_num != -1:

                    check_skill.append(skill_trees[i][text_num:])
        
    return len(check_skill)

# 못품(check_skill이 갱신되면서 반복하는 아이디어로 생각했는데 그렇게 된다면 첫번째 추출을 못함)

"""
key point 
- 값이 리스트에 있고 첫번째 값이 그 값과 같을 때 통과
"""

# 정답 
# for else 구문 사용해서 중간에 break 등으로 끊기지 않는다면 통과되는 구문 사용 
from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = deque(skill)

        for s in skill_tree:

            if s in skill and s != skill_list.popleft():
                break

        else:
            answer += 1

    return answer