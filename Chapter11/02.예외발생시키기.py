# raise 구문을 사용해서 에러를 강제로 발생시키기
try:
    number = int(input("음수를 입력해주세요 >>> "))
    if number >= 0:
        raise Exception("양수는 입력 불가")
except Exception as e:
    print("에러 발생!", e)