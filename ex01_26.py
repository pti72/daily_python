# 숫자 내장함수

# abs()
print(abs(-10)) # -10의 절댓값 출력
print(abs(10)) # 10의 절댓값 출력

# divmod : 몫, 나머지
print(divmod(10, 6), type(divmod(10, 6))) # (1, 4)
print(10 // 6) # 몫
print(10 % 6) # 나머지

# max(), min(), sum()
li = [2, 5, 7, 9, 12]
print(max(li)) # li에서 가장 큰 값
print(min(li)) # li에서 가장 작은 값
print(sum(li)) # li의 모든 요소들을 합한 값

# pow()
print(20 ** 3) # 20x20x20
print(pow(20, 3)) # 거듭제곱

# round()
print(round(2.4)) # 2
print(round(4.78)) # 5
print(round(3.447, 2)) # 3.45, 소수점 두자리로 반올림