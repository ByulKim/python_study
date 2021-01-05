#21/01/05,Tue

#NoneType
a_noneType = None #null

#Sequence Type - list : mutable - 변경가능
days = ['Mon','Tue','Wed','Thur','Fri'];
print("Mon" in days);
print(len(days));
days.append("Sat")
print(days)
days.insert(2,'a')
print(days)
days.pop(1)
print(days)

# tuple : immutable - 변경불가능
days = ('Mon','Tue','Wed','Thur','Fri');
print(type(days))

#dictionary
byul = {
  "name":"Byul",
  "age" : 28,
  "fav_food" : ["Chicken","Pizza"]
}

print(byul)

#substring
text = "abcd"
sl = slice(0,1)

print(text[sl])

#funtion - 들여쓰기로 구분
def say_hello() : 
  print("hello")
  print("bye")
print("2")
say_hello()
say_hello()

def plus(a, b) :
  print(a + b)
plus(1,2)
def minus(a, b=0) :
  print(a - b)
minus(1,2)

plus(b=30, a=2) #keyword argument

def say_hi(name, age) :
  return f"Hi {name} you are {age} years old"
  # = return "Hi "+name+" you are "+age+" years old"
print(say_hi("byul", 28))

#--------------- Code Challenge 1 -----------------
# 7 function
# + , - , * , / ,  % , -x, **

def plus (a,b) :
  return int(a) + int(b)

def minus (a,b) :
  return int(a) - int(b)

def times (a,b) :
  return int(a) * int(b)

def div (a,b) :
  return int(a) / int(b)

def remain (a,b) :
  return int(a) % int(b)

def negation (a) :
  return -int(a)

def power (a, b) :
  return int(a) ** int(b)

print(plus(5,10)) #더하기
print(minus(5,10)) #빼기
print(times(5,10)) #곱하기
print(div(5,10)) #나누기
print(remain(5,10)) #나눗셈 나머지
print(negation(5)) #부호변경
print(power(2,3)) #지수