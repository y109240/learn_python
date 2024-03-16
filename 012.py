# 간단한 계산기 만들기

first_number = int(input("첫 번째 숫자를 입력해주세요:"))
operator = input("연산자를 입력해주세요:")
second_number = int(input("두 번째 숫자를 입력해주세요:"))

if operator == "+":
  result = first_number + second_number
elif operator == "-":
  result = first_number - second_number
elif operator == "*":
  result = first_number * second_number
elif operator == "/":
  result = first_number / second_number
print(f"{first_number} {operator} {second_number} = {result}")