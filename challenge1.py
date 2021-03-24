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
print(remain(5,3)) #나눗셈 나머지
print(negation(5)) #부호변경
print(power(2,3)) #지수