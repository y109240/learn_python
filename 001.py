
# 구구단 만들기

def print_gugudan(dan):
  print("{}단".format(dan))
  for i in range(1, 10) :
    result = dan * i
    print("{} * {} = {}".format(dan, i, result))

print_gugudan(2)