words = ["사랑해", "고마워", "미안해", "사과할게"]

success = 0
fail = 0

print("한국어 공부")
for word in words:
    print(word)
    answer = input()

    if answer != word:
        fail += 1
    else:
        success += 1

print("전체 문제 개수 : " + str(len(words)))
print("맞힌 문제 개수 : " + str(success))
print("틀린 문제 개수 : " + str(fail))
