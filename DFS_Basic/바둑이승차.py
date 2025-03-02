"""
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태 울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 둘째 줄부터 N마리 바둑이의 무게가 주어진다.
▣ 출력설명
첫 번째 줄에 가장 무거운 무게를 출력한다.
▣ 입력예제 1 259 5
81
58
42 33 61
▣ 출력예제 1 242
"""

def dfs(L, total_sum):
    global tmp_v, answer_v
    if total_sum > sum_v:
        return 
    
    if tmp_v < total_sum:
        tmp_v = total_sum 

    if L==n:
        answer_v = tmp_v
    
    else:
        dfs(L+1, total_sum+li[L])
        dfs(L+1, total_sum)

if __name__ == "__main__":
    sum_v, n =map(int, input().split())
    li = [] 
    for i in range(n):
        li.append(int(input()))
    # print(li)

    tmp_v = -1234
    answer_v = 0

    # n = 5 
    # li = [81, 58, 42, 33, 61]
    dfs(0,0)
    print(answer_v)
    # 풀었는데 내 생각에 가지치기를 조금 해야할 것 같음(time out 우려)


"""
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)
"""