# 원화를 입력, 환율 입력 -> 달러 값

won = input("원화금액을 입력하세요 >>> ")
doller = input("환율을 입력하세요 >>> ")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(doller))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("나누기 0 은 불가능 합니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("예외O, 예외X, 상관없음 항상 실행되는 코드")