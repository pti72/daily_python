# 상속

# 부모 클래스
class Person :
    # 부모 클래스의 생성자
    def __init__(self, name): 
        self.name = name # 데이터 속성
    # 매소드
    def eat (self, food):
        print(self.name, "이/가", food, "를 먹습니다" )

# person 클래스를 상속 받는 자식 클래스 생성
class Student(Person):
    # 자식 클래스의 생성자
    def __init__ (self, name, school):
        # 부모 클래스의 생성자 호출
        super().__init__(name) # 부모의 생성자 매개변수 name에 값을 전달
        self.school = school # 자식 클래스에 추가된 데이터 속성
    
    # 자식 클래스에서 추가할 메소드
    def study(self):
        print(self.name, "은/는", self.school, "에서 공부합니다")


# 부모 클래스의 객체
pr1 = Person("홍길동")
pr1.eat("떡볶이")
# pr1.study() # 자식 클래스에서 새롭게 추가된 속성은 부모 클래스의 객체에서 사용 불가

# 자식 클래스 객체 생성
st1 = Student("짱구", "python학교")
st1.study()
st1.eat("당근") # 자식 클래스의 객체로 부모 클래스에서 상속 받은 메소드 호출