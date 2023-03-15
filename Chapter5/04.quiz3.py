# 20000원 이상 : 치킨, 10000원 이상 : 떡볶이, 2000원 이상 : 편의점 김밥

current_money = int(input("현재 가진 금액 입력 >>> "))

if current_money >= 20000:
    print("오늘 저녁은 치킨")
elif current_money >= 10000:
    print("오늘 저녁은 떡볶이")
else:
    print("오늘 저녁은 편의점 김밥")