import random 
# 기본 형태
# 1. 정의하기
def printHello():
    print("Hello")

# 2. 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a, b):
    print(a + b)

sum(1, 3)

def getRandomNumer():
    number = random.randint(1, 10)
    return number

result = getRandomNumer()
print(result)

# 매개변수와 반환값이 있는 함수
def add(a , b):
    result = a + b
    return result

print(add(4, 6))