def search_seq(seq, key):

    i = 0

    while True:
        
        if i == len(seq):
            return -1 
        
        if seq[i] == key:
            return i 
        
        i += 1

if __name__ == "__main__":
    
    num = int(input('원소의 개수를 입력해주세요.'))

    seq = [None] * num

    for i in range(num):
        seq[i] = int(input())
    
    search_key = int(input('찾고자 하는 원소의 값을 입력해주세요.'))

    find_index = search_seq(seq, search_key)

    if find_index == -1:
        print("찾고자 하는 값의 인덱스가 없습니다.")
    else:
        print(f"찾고자 하는 값의 인덱스는 {find_index} 입니다.")
