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