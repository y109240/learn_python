# 가위바위보 게임 만들기

from random import *
user = input("안내면 진거? 가위바위보! : ")
computer = ["가위", "바위", "보"]
computer = sample(computer ,1)[0]
print("컴퓨터 : {}".format(computer))

if user == computer :
  print("DRAW")
elif user == "가위" and computer == "보" :
  print("WIN")
elif user == "바위" and computer == "가위" :
  print("WIN")
elif user == "보" and computer == "바위" :
  print("WIN")
else:
  print("LOSE")