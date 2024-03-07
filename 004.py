import random

# 유저가 맞추는 하이앤로우
def guess(x):
  random_numder = random.randint(1, x)
  guess = 0
  while guess != random_numder:
    guess = int(input(f"1부터 {x}사이의 숫자중에서 맞춰보세요 : "))
    if guess < random_numder:
      print("숫자가 작습니다.")
    elif guess > random_numder:
      print("숫자가 큽니다.")
  
  print(f"정답! 숫자를 맞췄습니다! {random_numder}")

guess(100)

# 컴퓨터가 맞추는 하이앤로우
def computer_guess(x):
  low = 1
  high = x
  feedback = ""

  while feedback != "correct":
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f"is{guess} too high, too low, or correct? : ").lower()
    if feedback == "high":
      high = guess -1
    elif feedback == "low":
      low = guess +1
  print(f"The computer guessd your number, {guess} correctly.")

computer_guess(100)

# 제한이있는 하이앤로우
hit_number = random.randint(1, 1000)
class CountError(Exception):
  pass
count = 0
passfail = False
while passfail == False:
  try:
    user = int(input("1~999 사이의 숫자 중에서 맞혀보세요 : "))
    count += 1
    if hit_number == user :
      print(f"[{count}번째] 정답입니다!")
      passfail = True
    if count > 20:
      raise CountError
    elif hit_number > user:
      print(f"[{count}번째] 숫자가 작습니다. 다시 맞혀보세요.")
    elif hit_number < user:
      print(f"[{count}번째] 숫자가 큽니다. 다시 맞혀보세요.")
    if isinstance(user, int) != True:
      raise ValueError
  except ValueError:
    print("잘못된 값을 입력하였습니다. 숫자를 입력해주세요.")
  except CountError:
    print("20번의 기회가 모두 끝났습니다.")
    break
