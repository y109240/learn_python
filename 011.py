# 전설의 별찍기 문제 #

# 1. 별(*)을 가로로 num_stars 만큼 출력
num_stars = 5

count = 1
while count <= num_stars:
  print("*", end="")
  count += 1

for i in range(num_stars):
  print("*", end="")


# 2. 세로로 1부터 num_lines까지 정수를 출력
num_lines = 5

count = 1
while count <= num_lines:
  print(count)
  count += 1

for i in range(num_lines):
  print(i+1)


# 3. 위의 두 문제를 합쳐서
num_lines = 5
num_stars = 3

for i in range(num_lines):
  print(i+1, end="")
  for i in range(num_stars):
    print("*", end="")
  print()


# 4. 직각삼각형 그리기, 줄 번호만큼 별출력
num_lines = 5
for i in range(1, num_lines+1):
  print(i, end="")
  for j in range(i):
    print("*", end="")
  print()


# 5. 줄번호 빼고
num_lines = 5

for i in range(1, num_lines+1):
  for j in range(i):
    print("*", end="")
  print()


# 6. 직각삼각형 뒤집기
num_lines = 5

for i in range(num_lines, 0, -1):
  for j in range(i):
    print("*", end="")
  print()


# 7. 별앞에 숫자넣기
num_lines = 5

for i in range(1, num_lines+1):
  for j in range(num_lines-i):
    print(j, end="")
  for k in range(i):
    print("*", end="")
  print()


# 8. 숫자를 공백으로 바꾸기
num_lines = 5

for i in range(1, num_lines+1):
  for j in range(num_lines-i):
    print(" ", end="")
  for k in range(i):
    print("*", end="")
  print()


# 9. 뒤집어보기
num_lines = 5

for i in range(num_lines, 0, -1):
  for j in range(num_lines-i):
    print(" ", end="")
  for k in range(i):
    print("*", end="")
  print()


# 10. 피라미드 그리기
num_lines = 5

for i in range(1, num_lines+1):
  for j in range(num_lines-i):
    print(" ", end="")
  for i in range(i*2-1):
    print("*", end="")
  print()


# 11. 피라미드 뒤집기
num_lines = 5

for i in range(num_lines, 0, -1):
  for j in range(num_lines-i):
    print(" ", end="")
  for i in range(i*2-1):
    print("*", end="")
  print()


# 12. f-string을 이용한 직각삼각형 그리기
for i in range(num_lines):
  print(f"{'*'*(i+1)}")

# 13. 우측정렬
for i in range(num_lines):
  print(f"{'*'*(i+1):>{num_lines}}")

# 14. 가운데정렬
for i in range(num_lines):
  print(f"{'*'*(i*2+1):^{num_lines*2-1}}")
