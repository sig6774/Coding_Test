"""
문제 설명
빙고는 NxN 크기의 게임 보드 칸에 1부터 NxN까지의 자연수를 중복 없이 하나씩 적은 후 숫자를 하나씩 지워나가는 게임입니다. 이때, 가로, 세로, 대각선 방향으로 한 줄에 적힌 숫자를 모두 지울 경우 빙고를 1개 만들었다고 합니다.
다음은 4X4 크기의 게임 보드를 이용해 게임을 진행한 예시입니다.

위와 같이 각 칸에 숫자가 적혀 있을 때, 위 게임 보드에서 순서대로 지운 숫자가 [14,3,2,4,13,1,16,11,5,15]인 경우 아래와 같이 빙고 3개가 만들어집니다.
빙고 게임 보드에 적힌 숫자가 담겨있는 배열 board, 게임 보드에서 순서대로 지운 숫자가 들어있는 배열 nums가 매개변수로 주어질 때, board에서 nums에 들어있는 숫자를 모두 지우면 몇 개의 빙고가 만들어지는지 return하도록 solution함수를 완성해주세요.

제한사항
board는 게임 보드 칸에 적힌 숫자를 뜻하는 NxN크기의 2차원 배열이며, N은 2 이상 500이하의 자연수입니다.
board의 각 칸에는 1 이상 NxN이하의 자연수가 중복 없이 하나씩 들어있습니다.
nums는 board에서 지울 숫자가 들어있는 배열이며, 길이는 1 이상 NxN이하입니다.
nums에 들어있는 숫자는 1 이상 NxN이하의 자연수이며, 중복된 수가 들어있지 않습니다.

입출력 예
board	nums	result
[[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]	[14,3,2,4,13,1,16,11,5,15]	3
[[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]]	[15,7,2,25,9,16,12,18,5,4,10,13,20]	2
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
다음 그림과 같이 2개의 빙고가 만들어집니다.
"""

"""
1. nums에 해당하는 값이 있으면 0으로 변환
2. 가로, 세로 빙고 모듈 작성 
3. 대각선 빙고 모듈 작성 
"""

def create_new_board(board, nums):
    new_board = []
    for row in board:
        for v in nums:
            if v in row:
                for row_v in range(len(row)):
                    if row[row_v] == v:
                        row[row_v] = 0 


        new_board.append(row)
    return new_board

# 가로, 세로 확인 모듈 
def check_h_v_bingo(board):
    cnt = 0 

    # 가로 확인
    for h in range(len(board)):
        tmp_cnt = 0
        for v in range(len(board)):
            if board[h][v] == 0:
                tmp_cnt += 1 

        if tmp_cnt == len(board):
            cnt += 1 
    
    # 세로 확인
    for v in range(len(board)):
        tmp_cnt = 0

        for h in range(len(board)):
            if board[v][h] == 0:
                tmp_cnt += 1 
        
        if tmp_cnt == len(board):
            cnt += 1 
    
    return cnt 

# 대각선 확인 모듈 
def check_diagonal_bingo(board):

    cnt = 0 

    # 정방향 대각선 
    for h in range(len(board)):
        tmp_cnt = 0
        for v in range(len(board)):
            if h==v:
                if board[h] == board[v]:
                    tmp_cnt += 1

    if tmp_cnt == len(board):
        cnt += 1 
    
    new_tmp_cnt = 0 
    for h in range(len(board)):
        for v in range(len(board)):
            if (h+v) == (len(board)-1):
                if board[h][v] == 0:
                    new_tmp_cnt += 1
                    
    if new_tmp_cnt == len(board):
        cnt += 1 
    
    return cnt 

def solution(board, nums):
    new_board = create_new_board(board, nums)

    cnt1 = check_h_v_bingo(new_board)
    cnt2 = check_diagonal_bingo(new_board)
    
    return cnt1+cnt2

# board = [[11,13,15,16],
#         [12,1,4,3],
#         [10,2,7,8],
#         [5,14,6,9]]

# nums = [14,3,2,4,13,1,16,11,5,15]

board = [[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]]
nums = [15,7,2,25,9,16,12,18,5,4,10,13,20]	

print(solution(board=board, nums=nums))

# 시간 초과... 

def solution(board, nums):
    N = len(board)
    nums = set(nums)
    answer = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] in nums:
                board[i][j] = 0

    answer += len([i for i in board if sum(i) == 0])
    answer += len([i for i in zip(*board) if sum(i) == 0])
    answer += int(sum(board[i][i] for i in range(N)) == 0)
    answer += int(sum(board[N - 1 - i][i] for i in range(N)) == 0)

    return answer
# 아 sum을 활용하면 되는구나...