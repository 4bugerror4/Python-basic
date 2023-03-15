kor = int(input("국어 >>> "))
math = int(input("수학 >>> "))
eng = int(input("영어 >>> "))

result = kor + math + eng
score = result / 3

if (0 < kor > 100) or (0 < math > 100) or (0 < eng > 100):
    print("잘못 입력하였습니다.")
else:
    if score >= 80:
        print("불합격")
    else:
        print("합격")