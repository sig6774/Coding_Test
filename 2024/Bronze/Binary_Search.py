def binary_search(seq, key):

    seq_start = 0
    seq_end = len(seq) -1 
    

    while True:
        
        seq_mid = (seq_start + seq_end) // 2    

        if seq[seq_mid] == key:
            return seq_mid 
        
        # 중앙 인덱스 번호에 있는 값이 찾고자 하는 값보다 큰 경우 
        # 중앙 인덱스 -1 하여 검색 끝으로 재 선언 후 검색
        elif seq[seq_mid] > key:
            seq_end = seq_mid - 1

        # 중앙 인덱스 번호에 있는 값이 찾고자 하는 값보다 작은 경우 
        # 중앙 인덱스 +1 하여 검색 시작으로 재 선언 후 검색
        else:
            seq_start = seq_mid +1

        if seq_start > seq_end:
            break

        return -1 

if __name__ == "__main__":
    
    num = int(input('원소의 개수를 입력해주세요.'))

    seq = [None] * num

    print("배열을 오름차순으로 입력하세요.")

    seq[0] = int(input())

    for i in range(1,num):
        while True:
            seq[i] = int(input(f'x[{i}] : '))

            if seq[i] > seq[i-1]:
                break
    
    search_key = int(input('검색하고자 하는 값을 입력하세요.'))

    find_index = binary_search(seq, search_key)
    
    if find_index == -1:
        print("찾고자 하는 값이 없습니다.")
    else:
        print(f"찾고자 하는 값의 인덱스가 {find_index}에 있습니다.")
