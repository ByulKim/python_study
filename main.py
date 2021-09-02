players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

print("-"*20)

IN = input("IN 선수 이름: ")
OUT = input("OUT 선수 이름: ")

print("-"*20)

players.remove(OUT)
players.append(IN)

print("교체 결과 : ")
for member in players:
    print(member)