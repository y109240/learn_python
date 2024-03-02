
# 구구단 만들기

# def print_gugudan(dan):
#   print("{}단".format(dan))
#   for i in range(1, 10) :
#     result = dan * i
#     print("{} * {} = {}".format(dan, i, result))

# print_gugudan(2)

n = input("몇단을 출력할까요? : ")

def print_gugudan(dan):
  print("{}단".format(dan))
  for i in range(1, 10) :
    result = dan * i
    print("{} * {} = {}".format(dan, i, result))

print_gugudan(int((n)))
