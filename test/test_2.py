#lottos(0은 알아볼 수 없는 숫자) win_nums(1-45 정수) answer(최고, 최저)
#[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
#[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
#[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]

#1	6개 번호가 모두 일치
#2	5개 번호가 일치
#3	4개 번호가 일치
#4	3개 번호가 일치
#5	2개 번호가 일치
#6(낙첨)	그 외

def solution(lottos, win_nums):
    answer = []

    rank = [6,6,5,4,3,2,1]

    #현재 당첨 번호와 같은 개수 찾기
    right_cnt = 0
    for i in lottos:
        if i in win_nums:
            right_cnt += 1

    #0의 개수 찾기
    zero_cnt = lottos.count(0)

    answer.append(rank[(right_cnt+zero_cnt)]) #최고
    answer.append(rank[right_cnt]) #최저

    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))