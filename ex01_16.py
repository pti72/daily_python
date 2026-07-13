# 디폴트 매개변수
# 정수 4개를 전달 받아 그 합을 반환하는 함수 정의
def add_nums (num1, num2, num3, num4 = 40): # 디폴트 매개변수는 반드시 맨 뒤의 매개변수부터 설정을 해야한다!
    return num1 + num2 + num3 + num4

# 함수호출
print(add_nums(10, 20, 30))



# 가변 매개 변수 : 몇개의 인수가 들어올지 모를 때 사용
# 전달되는 인수들을 출력하는 함수 show() 함수 정의

def show(*args):
    print(args, type(args))

# 함수 호출
show(1, "python", 3)
show("a", 3.14)