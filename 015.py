# 한자리수가 될때까지 각자리수 합치기
num = int(input("숫자를 입력해 주세요 : "))
while len(str(num)) > 1:
  print(num)
  # num = sum([int(x) for x in str(num)])
  num = sum([int(str(num)[i]) for i in range(len(str(num)))])
else:
  print(num)

# 숫자에 천단위로 컴마넣기
input_number = input("숫자를 입력해 주세요 : ")
re_number = input_number[::-1]
# splitted = [re_number[i:i+3] for i in range(0, len(str_num), 3)]
splitted = [re_number[i*3:(i+1)*3] for i in range(len(re_number)//3+1)]
",".join(splitted)[::-1]