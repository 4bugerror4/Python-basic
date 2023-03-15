class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")

try:
    number = int(input("음수를 입력해주세요 >>> "))
    if number >= 0:
        raise PositiveNumberError
except Exception as e:
    print("에러 발생!", e)
