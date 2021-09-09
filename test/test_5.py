#오픈채팅방
# Enter -님이 들어왔습니다.
# Change (닉네임변경)
# Leave -님이 나갔습니다. 

def solution(record):
    answer = []

    recode_dict = {}
    for item in record:
        data = item.split(" ")
        if data[0] != "Leave" : recode_dict[data[1]] = data[2]

    for item in record:
        data = item.split(" ")
        if data[0] != "Change" : answer.append(recode_dict[data[1]]+"님이 "+ ("들어왔습니다." if data[0] == "Enter" else "나갔습니다.")) 

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# record
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
# result
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]