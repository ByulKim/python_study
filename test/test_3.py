#아이디의 길이는 3자 이상 15자 이하여야 합니다.
#아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
#단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

#1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
#2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
#5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
#6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

#new_id는 길이 1 이상 1,000 이하인 문자열입니다.
#new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
#new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.

import re

def del_dot(new_id): #앞,뒤 마침표 제거 함수
    # while new_id:
    #     if new_id[0] == "." : new_id = new_id[1:]
    #     elif new_id[len(new_id) -1] == "." : new_id = new_id[0:len(new_id) -1]
    #     else : break

    new_id = re.sub("^[.]|[.]$","",new_id)
            
    return new_id

def solution(new_id):

    #1단계
    new_id = new_id.lower()

    #2단계
    new_id = re.sub("[^a-z0-9-_.]","",new_id)

    #3단계
    # while ".." in new_id:
    #     new_id = new_id.replace("..",".")
    new_id = re.sub("\.+",".",new_id)

    #4단계
    new_id = del_dot(new_id)

    #5단계
    if not new_id:
        new_id = "a"

    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = del_dot(new_id)

    #7단계
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    return new_id

print(solution("abcdefghijklmn.p"))

#no	new_id	result
#예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
#예2	"z-+.^."	"z--"
#예3	"=.="	"aaa"
#예4	"123_.def"	"123_.def"
#예5	"abcdefghijklmn.p"	"abcdefghijklmn"