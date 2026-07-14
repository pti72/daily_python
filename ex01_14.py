# 기타제어문

# 1) break문 : 반복문 강제 종료
# 1~10까지의 범위 중 5까지만 출력
for i in range(1, 11):
    print(i)
    # i에 저장된 값이 5라면 반복문 종료
    if i == 5:
        print("프로그램 종료")
        break # 반복문 강제 종료


# 2) contunue문 : 다음 반복 계속 진행
# 1 ~ 10까지 정수 중 5만 빼고 출력
for i in range(1, 11):
    if i == 5:
        continue # 다음 반복으로 계속 진행
    else :
        print(i)


# 3) pass문 : 조건문, 반복문에 실행내용을 정하지 않았을 때 임시로 작성

if 10 >= 5:
    pass # 조건문에 넣어줄 실행문이 딱히 없을 경우

for i in range(3):
    pass # 아직 작성할 내용을 못 정했으니 넘어가기