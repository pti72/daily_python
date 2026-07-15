tu = (10, 20, 30, 10, 30, "a", "b", 50)
print(tu, type(tu))
# 튜플은 시퀀스 자료형(인덱싱, 슬라이싱)

print(tu[0], type(tu[0]))
print(tu[:4], type(tu[:4]))

# 튜플은 인덱스 번호를 사용하여 수정 불가


# 튜플의 메소드
tu = (1, 3, 5, 6, 2, 3, 1, 4, 5)
print(tu, type(tu))

print(tu.count(1)) # tu에 1이 몇개 있니?
print(tu.index(1)) # tu에서 1이라는 값이 튜플의 몇번째 위치에 있는지 알려줘
                   # 중복된 값을 찾고자 하면 맨앞에 있는 인덱스 번호를 알려줌