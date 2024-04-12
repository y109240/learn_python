# 간단한 계산기 만들기

first_number = int(input("첫 번째 숫자를 입력해주세요:"))
operator = input("연산자를 입력해주세요:")
second_number = int(input("두 번째 숫자를 입력해주세요:"))

if operator == "+":
  result = first_number + second_number
elif operator == "-":
  result = first_number - second_number
elif operator == "*":
  result = first_number * second_number
elif operator == "/":
  result = first_number / second_number
print(f"{first_number} {operator} {second_number} = {result}")



# tkinter로 만들어보기

from tkinter import *

def clear():
  entry1.delete(0, len(entry1.get()))
  entry2.delete(0, len(entry2.get()))

def calculate(operation):
  num1 = float(entry1.get())
  num2 = float(entry2.get())

  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  
  result_label.config(text = f"{num1} {operation} {num2} = {result}")

main = Tk()
main.title("사칙연산 계산기")
main.geometry("400x300")
frame_top = Frame(main)
frame_top.pack(side="top")
label = Label(frame_top, text="간단한 사칙연산 계산기", font="Arial 20")
label.pack()
entry1 = Entry(frame_top, justify="right")
entry1.pack()
entry2 = Entry(frame_top, justify="right")
entry2.pack()
btn_clear = Button(frame_top, text="지우기", width=10, command=clear)
btn_clear.pack()
result_label = Label(frame_top , text="결과", font="Arial 10")
result_label.pack(side="left")
frame_bot = Frame(main)
frame_bot.pack(side="top")

calitm = [["+", "-"],
          ["*", "/"]]
for i, items in enumerate(calitm):
  for k, item in enumerate(items):
    btn = Button(frame_bot, text=item, width=10, height=5,
                command=lambda cmd=item: calculate(cmd))
    btn.grid(row=(i+1), column=k)

main.mainloop()
