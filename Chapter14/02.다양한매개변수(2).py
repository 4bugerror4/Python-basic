# 1. 위치 가변 매개변수 (튜플 형식으로 받아옴)
def print_fruits(*args):
    for i in args:
        print(i)

print_fruits("apple", "banana", "otrange", "grape")

# 2. 키워드 가변 매개변수 (딕셔너리 형태로 받아옴)
def comment_info(**kargs):
    for key, value in kargs.items():
        print(f"{key} : {value}")

comment_info(name="파린이", content = "잘하고싶습니다.")

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변
def post_info(*tags, title, content):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}")


post_info("#파이싼", "#함수", title = "파이썬 함수 정리!", content = "다양한 매개변수")
