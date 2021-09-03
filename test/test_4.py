#문자열 압축하기
#가장 짧게 압축한 문자열의 길이 구하기

def solution(s):

    answer = []

    for cnt in range(1,len(s)//2+1):
        num = 1 #연속개수
        total_length = len(s); #전체길이

        for i in range(0,len(s),cnt):
            tmp = "" if i == 0 else s[i-cnt:i] #이전문자
            cut = s[i:i+cnt] #현재문자

            if cut == tmp : 
                num += 1
                if i + cnt < len(s) : continue
            
            if num != 1 : total_length -= ((cnt*num) - (cnt+1)) #연속문자 길이 조정
            num = 1 #연속 개수 초기화
            
        answer.append(total_length)

    return min(answer)

print(solution("aabbaccc"))

# s	result
# "aabbaccc"	7 => 2a2ba3c (1자리 구분)
# "ababcdcdababcdcd"	9 => 2ababcdcd (8자리 구분)
# "abcabcdede"	8 => 2abcdede
# "abcabcabcabcdededededede"	14 => 2abcabc2dedede
# "xababcdcdababcdcd"	17 => xababcdcdababcdcd