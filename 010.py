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

def find_divisors(num):
  return [x for x in range(1, num+1) if num % x == 0]
  # divisors = []
  # for x in range(1, num+1):
  #   if num % x == 0:
  #     divisors.append(x)
  # return divisors

def is_prime(num):
  if num == 1:
    return False
  else:
    for i in range(2, num):
      if num % i == 0:
        return False
    else:
      return True

def find_prime_divisors(num):
  return [x for x in find_divisors(num) if is_prime(x)]
  # prime_divisors = []
  # for x in find_divisors(num):
  #   if is_prime(x):
  #     prime_divisors.append(x)
  # return prime_divisors

try:
  num = int(input("자연수를 입력해 주세요 : "))
except ValueError:
  print("자연수가 아닙니다.")
else:
  print(find_prime_divisors(num))
