# 플로이드의 삼각형

# for문
rows = 5
num = 1

for i in range(1, rows+1):
  for j in range(1, i+1):
    print(num, end=" ")
    num += 1
  print()

# while문 으로 변형
rows = 5
num = 1

for i in range(1, rows+1):
  counte = 1
  while counte <= i:
    print(num, end=" ")
    num += 1
    counte += 1
  print()

rows = 1
num = 1
while rows <= 5:
  counte = 1
  while counte <= rows:
    print(num, end=" ")
    num += 1
    counte += 1
  rows += 1
  print()