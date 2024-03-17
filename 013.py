# 두수의 공약수 구하기
num1 = int(input("첫번째 숫자를 입력해주세요: "))
num2 = int(input("두번째 숫자를 입력해주세요: "))
common_divisors = []

for i in range(1, min(num1, num2)+1):
  if num1 % i ==0 and num2 % i ==0:
    common_divisors.append(i)
print(f"두수의 공약수는 {common_divisors}입니다.")

# 최대공약수 구하기
print(f"두수의 최대공약수는 {common_divisors[-1]}입니다.")

greatest_common_divisor = 1
for i in range(2, min(num1, num2)+1):
  if num1 % i ==0 and num2 % i ==0:
    greatest_common_divisor = i
print(f"두수의 최대공약수는 {greatest_common_divisor}입니다.")

# gcd()
import math
math.gcd(num1, num2)