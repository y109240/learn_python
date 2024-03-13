# 문제풀기 중
# 소수만들기 프로그램 고치기
num = int(input("자연수를 입력해주세요:"))
if num == 1:
  print("1은 소수가 아닙니다.")
else:
  for i in range(2, num):
    if num % i == 0:
      print(f"{num}은 {i}로 나눌수 있습니다.")
    else:
      print(f"{num}은 소수입니다.")
      break