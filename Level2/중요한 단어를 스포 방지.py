"""
문제 설명
카카오톡은 메시지의 일부를 가려두었다가, 클릭했을 때만 공개되는 스포 방지 기능을 제공합니다. 이 기능을 활용하면 중요한 정보를 가리고 보낼 수 있습니다.

무지는 이 기능을 이용해 하나의 메시지 곳곳에 스포 방지 기능을 적용해 당신에게 보냈습니다. 당신은 메시지 시작부터 왼쪽 → 오른쪽 순서로 스포 방지 구간을 하나씩 클릭해 공개되는 단어들 중, 중요한 단어가 몇 개인지 확인하려 합니다.

단어 및 중요한 단어 규칙

단어는 공백으로 구분되며, 알파벳 소문자와 숫자로만 구성된 연속된 문자열입니다.
단어를 구성하는 문자들의 인덱스 중 하나 이상이 스포 방지 구간에 포함될 경우, 해당 단어는 스포일러 방지 단어로 간주합니다. 즉, 단어 내 일부 문자에만 스포일러 방지 기능이 적용되더라도, 해당 단어 전체를 스포일러 방지 단어로 간주합니다.
한 단어가 여러 개의 스포 방지 구간에 걸쳐 있을 수 있으며, 하나의 스포 방지 구간에 여러 단어가 포함될 수 있습니다.
스포 방지 구간을 클릭해 단어의 모든 문자가 공개되었을 때, 그 단어가 아래 조건을 모두 만족하면 중요한 단어입니다.
스포 방지 단어여야 합니다.
메시지의 스포 방지 구간이 아닌 구간(= 어떤 스포 방지 구간에도 속하지 않는 모든 구간: 각 구간의 앞·사이·뒤 포함)에 등장한 적이 없어야 합니다.
이전에 공개된 스포 방지 단어와 중복되지 않아야 합니다.
여러 단어가 동시에 공개된 경우, 왼쪽부터 순서대로 하나씩 중요한 단어인지 판단합니다.
무지가 당신에게 보내온 메시지를 나타내는 문자열 message와 스포 방지가 적용된 구간을 나타내는 2차원 정수 배열 spoiler_ranges가 매개변수로 주어질 때, 스포 방지 단어 중 중요한 단어의 수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ message의 길이 ≤ 20,000
message는 알파벳 소문자, 숫자 그리고 공백으로 이루어져 있습니다.
message는 하나 이상의 단어로 구성된 문자열입니다.
공백은 연속해서 등장하지 않습니다.
1 ≤ spoiler_ranges의 길이 ≤ 1,000
spoiler_ranges[i]는 [start, end] 형태로 스포 방지를 적용한 구간을 나타냅니다. 이때 start와 end는 문자 인덱스이며, 두 인덱스 모두 구간에 포함됩니다.
0 ≤ start ≤ end < message의 길이
모든 구간은 서로 겹치지 않으며, start 기준으로 오름차순 정렬되어 주어집니다.

테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹은 하나 이상의 하위 그룹으로 이루어져 있으며, 하위 그룹의 모든 테스트 케이스를 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	추가 제한 사항
#1	7%	message의 모든 단어는 중복없이 한 번씩만 등장합니다.
#2	13%	모든 스포 방지 구간은 각각 정확히 한 단어의 시작과 끝을 가리킵니다. spoiler_ranges의 길이 = 1
#3	45%	모든 스포 방지 구간은 각각 정확히 한 단어의 시작과 끝을 가리킵니다.
#4	35%	추가 제한 사항 없음
입출력 예
message	spoiler_ranges	result
"here is muzi here is a secret message"	[[0, 3], [23, 28]]	1
"my phone number is 01012345678 and may i have your phone number"	[[5, 5], [25, 28], [34, 40], [53, 59]]	4
입출력 예 설명
"""

"""
1. 전달 받은 내용에 따라 스포 방지 단어 추출 후 리스트에 저장 
    1.1 스포방지 단어 구간이라면 그 단어는 모두 리스트에 저장
    1.2 걸쳐있는 경우 단어를 추출하거나 문자를 추출하는 로직 작성
2. 리스트에 저장된 단어가 기존 문자열에 포함이 되는지 여부 파악 
3. 중복이 있는지 파악 
"""

# def solution(message, spoiler_ranges):
    
    
#     return answer

message = "here is muzi here is a secret message"
spoiler_ranges = [[0, 3], [23, 28]]

message = "my phone number is 01012345678 and may i have your phone number"
spoiler_ranges = [[5, 5], [25, 28], [34, 40], [53, 59]]

str_lst = []
idx_lst = []
total_idx_lst = [] 
k = ""

for idx in range(len(message)):
    
    if message[idx] != " ":
        k += message[idx]
        idx_lst.append(idx)
    
    else:
        str_lst.append(k)
        k = ""
        total_idx_lst.append(idx_lst)
        idx_lst= [] 
        


print(str_lst, total_idx_lst)

# 스포일러 단어 추출 
spoiler_words = [] 
for total_idx in range(len(total_idx_lst)):
    for k in spoiler_ranges:
        
        if k[0] in total_idx_lst[total_idx]:
            # print(total_idx)
            # print(str_lst[total_idx])
            spoiler_words.append(str_lst[total_idx])

# 기존 문장에 있는지 파악 
print(spoiler_words)
for spo_word in spoiler_words:
    cnt = 0 
    for word in str_lst:
        if spo_word == word:
            cnt += 1 
    
    if cnt >= 2:
        # print(spo_word)
        spoiler_words.remove(spo_word)

# 중복 체크 
important_word_cnt = len(set(spoiler_words))
print(important_word_cnt)


# 못 품... (나중에 다시 풀어보기)

# 참고 풀이 
def solution(message, spoiler_ranges):
    words = []
    n = len(message)
    # 1. 단어와 위치 찾기
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue

        start = i

        while i < n and message[i] != ' ':
            i += 1

        end = i - 1
        word = message[start:i]

        words.append([word, start, end])

    # 2. 스포일러 위치 표시
    covered = [False] * n

    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            covered[i] = True

    # 3. 평문 단어 찾기
    normal_words = set()

    for word, start, end in words:
        spoiler_word = False

        for i in range(start, end + 1):
            if covered[i]:
                spoiler_word = True
                break

        if not spoiler_word:
            normal_words.add(word)

    # 4. 공개 진행
    opened = [False] * n
    used = set()
    answer = 0

    for s, e in spoiler_ranges:

        for i in range(s, e + 1):
            opened[i] = True

        for word, start, end in words:

            spoiler_word = False
            for i in range(start, end + 1):
                if covered[i]:
                    spoiler_word = True
                    break

            if not spoiler_word:
                continue

            full_open = True
            for i in range(start, end + 1):
                if covered[i] and not opened[i]:
                    full_open = False
                    break

            if not full_open:
                continue

            if word not in normal_words and word not in used:
                answer += 1
                used.add(word)

    return answer