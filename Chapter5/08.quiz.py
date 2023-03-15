list = []

count = int(input("1일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("2일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("3일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("4일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("5일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("6일차 턱걸이 횟수 >>> "))
list.append(count)
count = int(input("7일차 턱걸이 횟수 >>> "))
list.append(count)

total = list[0] + list[1] + list[2] + list[3] + list[4] + list[5] + list[6]

avg = total / len(list)

print(int(avg))


