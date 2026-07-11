# 내장메소드

# count()
str = "I love you"
print(str, type(str))
print(str.count("I")) # str에서 I가 몇번 나오는지 알려줘

# find()
str2 = "best of best"
print(str2.find("of")) # str2에서 "of"가 처음 나온 위치 인덱스 번호 반환
print(str2.find("worst")) # 찾는 문자열이 없을 경우 -1 반환

# index()
str2 = "best of best"
print(str2.index("best")) # find()와 기능이 같다
# 없는 문자열을 찾으려고 하면 오류 발생

# join()
li = ["h", "e", "l", "l", "o"]
print(li, type(li))
print("".join(li)) # 리스트의 요소들이 하나의 문자열로 합쳐짐
print("-".join(li)) # 리스트의 요소 사이마다 " - " 문자열이 추가되어 합쳐짐

di = {"a" : 1, "b" : 2}
print(di, type(di))
print("".join(di)) # 딕셔너리는 키만 연결됨

