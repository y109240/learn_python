# 구구단표 만들기
print(format("구구단표",">20s"))

# 표 머리 출력
print("  |", end = "")
for j in range(1, 10):
  print("  ", j, end = "")
# 새로운 행 삽입
print()
print("-----------------------------------------")

# 구구단 표 출력
for i in range(1, 10):
  print(i, "|", end="")
  for j in range(1, 10):
    print(format(i*j,">4d"), end="")
  print()


# 전체 표 출력
for i in range(1, 10):
  for j in range(2, 10):
    print(f"{j} x {i} = {j*i:2}", end="\t")
  print()
