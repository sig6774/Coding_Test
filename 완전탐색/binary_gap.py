# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    """
    1. 2로 나눈 후 나머지가 홀수 짝수 여부 판단
    2. 홀수라면 1, 짝수라면 0 추가 
    3. 갭이 있어야하므로 다시 1이 오는지 안오는지 판단 추가 
    """
    s = ""
    while N >= 1:
        tmp_v = N%2 
        if tmp_v % 2 == 0:
            s += "0"
        else:
            s += "1"
        
        N = N//2
        # print(N)
    
    get_v = s[::-1]
    max_v, cnt = 0, 0
    flag = False 
    for v in get_v:
        if v == "1":
            if flag:
                if max_v <= cnt:
                    max_v = cnt
            else:
                flag = True
            cnt = 0

        else:
            cnt += 1      
    return max_v

print(solution(529))

# 정답!