# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요>>>")

if input_pass == origin_pass:
    print("로그인 성공했습니다.")
elif input_pass == "":
    print("공백입니다.")
else:
    print("로그인 실패했습니다.")