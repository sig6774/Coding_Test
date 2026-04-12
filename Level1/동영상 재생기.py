"""
문제 설명
당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

제한사항
video_len의 길이 = pos의 길이 = op_start의 길이 = op_end의 길이 = 5
video_len, pos, op_start, op_end는 "mm:ss" 형식으로 mm분 ss초를 나타냅니다.
0 ≤ mm ≤ 59
0 ≤ ss ≤ 59
분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타냅니다.
비디오의 현재 위치 혹은 오프닝이 끝나는 시각이 동영상의 범위 밖인 경우는 주어지지 않습니다.
오프닝이 시작하는 시각은 항상 오프닝이 끝나는 시각보다 전입니다.
1 ≤ commands의 길이 ≤ 100
commands의 원소는 "prev" 혹은 "next"입니다.
"prev"는 10초 전으로 이동하는 명령입니다.
"next"는 10초 후로 이동하는 명령입니다.

입출력 예
video_len	pos	op_start	op_end	commands	result
"34:33"	"13:00"	"00:55"	"02:55"	["next", "prev"]	"13:00"
"10:55"	"00:05"	"00:15"	"06:55"	["prev", "next", "next"]	"06:55"
"07:22"	"04:05"	"00:15"	"04:07"	["next"]	"04:17"
"""

"""
1. 분, 초 단위의 입력을 초 단위의 숫자로 모두 변경 
2. 각 요건에 맞게 입력하도록 작업 
    2.1 prev 인데 00:00 이하라면 00:00으로 변환 
    2.2 next 인데 최대 동영상 길이라면 최대 길이로 변환 
    2.3 next 했을 때 오프닝 건너뛰기가 된다면 오프닝 건너뛰기 마지막으로 변환
    2.4 현재 위치가 오프닝 사이에 있다면 오프닝 건너뛰기로 변환 후 next 연산
"""

video_len = "10:55"
pos = "00:05"
op_start = "00:15"
op_end = "06:55"
commands = ["prev", "next", "next"]

video_len = "07:22"
pos = "04:05"
op_start = "00:15"
op_end = "04:07"
commands = ["next"]

def solution(video_len, pos, op_start, op_end, commands):
    def convert_time_to_second(con_len):
        minute = int(con_len[:2])
        second = int(con_len[3:])

        return minute*60 + second

    converted_video_len = convert_time_to_second(video_len)
    converted_pos = convert_time_to_second(pos)
    op_start = convert_time_to_second(op_start)
    op_end = convert_time_to_second(op_end)
    if converted_pos >= op_start and converted_pos <= op_end:
        converted_pos = op_end

    for com in commands:
        # print(converted_pos)

        if com == "next":
            tmp_pos = converted_pos + 10
            if tmp_pos >= converted_video_len:
                converted_pos = converted_video_len
            elif tmp_pos >= (converted_video_len - 10):
                converted_pos = tmp_pos
            else:
                converted_pos = tmp_pos
        
        else:
            tmp_pos = converted_pos - 10 
            if tmp_pos <= 0 or tmp_pos <= 10:
                converted_pos = 0
            else:
                converted_pos = tmp_pos

        if converted_pos >= op_start and converted_pos <= op_end:
            converted_pos = op_end

    min_int = converted_pos // 60
    if min_int < 10:
        min_str = f'0{min_int}'
    else:
        min_str = str(min_int)
    
    sec_int = converted_pos % 60
    if sec_int < 10:
        sec_str = f'0{sec_int}'
    else:
        sec_str = str(sec_int)
    
    return f'{min_str}:{sec_str}'

print(solution(video_len=video_len, pos=pos, op_start=op_start, op_end=op_end, commands=commands))

# 정답 

