# 구구단 만들기
n = int(input("몇단을 출력할까요? : "))

# 함수 
def print_gugudan(dan):
  print("{}단".format(dan))
  for i in range(1, 10) :
    result = dan * i
    print("{} * {} = {}".format(dan, i, result))
print_gugudan(n)

# 반복문
for i in range(1, 10):
  result = n * i
  print(f"{n} * {i} = {result}")
