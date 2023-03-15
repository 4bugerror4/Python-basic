# 문자열 포매팅이 없다면?
# 기준님 수강기간이 7일 남았습니다.

name = "기준"
duration = 7

message = name + '님 수강기간이 '  + str(duration) + "일 남았습니다."
print(message)

# 문자열 포매팅 사용시!!!!
message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(message_format)

# format 메서드
a = ' Hello {2} {1} {0}'.format("apple", "paineapple", "pen")
print(a)

# f-string 사용
name1 = "apple"
name2 = "pineapple"
name3 = "pen"
c = f'{name1}, {name2}, {name3}'
print(c)