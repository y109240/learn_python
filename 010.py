# 문제풀기 중
# 소수찾기 프로그램 고치기
num = int(input("자연수를 입력해주세요:"))
if num == 1:
  print("1은 소수가 아닙니다.")
elif num != 1:
  for i in range(2, num):
    if num % i == 0:
      print(f"{num}은 {i}로 나눌수 있습니다.")
      break
  else:
    print(f"{num}은 소수입니다.")

# 더 효율적으로 찾는 방법
# 모든 약수들을 찾아서 나열하는 방법
