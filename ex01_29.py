# 내장메소드

# split()

data = "hello world"
print(data,type(data))

print(data.split(), type(data.split())) # 문자열을 공백 문자 기준으로 분리 후 리스트에 저장한 결과 반환
print(data.split("o")) # 문자열을 "o"라는 문자열로 분리

# replace()

data = "I love you"
print(data)
print(data.replace("love", "like")) # data에서 "love"를 "like"로 바꿔줘

# 불필요한 문자열 제거 메소드
str = "%%%%%%%1%%2%%3%%%%%%%"

print(str.strip("%")) # 양쪽끝에 있는 % 제거
print(str.lstrip("%")) # 왼쪽 끝에 있는 % 제거
print(str.rstrip("%")) # 오른쪽 끝에 있는 % 제거
# 문자열 중간에 포함되어 있는 것은 제거할 수 없음