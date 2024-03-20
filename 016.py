# 음성인식(3.11)

import speech_recognition as sr
r = sr.Recognizer()
microphone = sr.Microphone()

while True:
  with microphone as source:
    r.adjust_for_ambient_noise(source)
    print("음성 인식 대기중")
    audio = r.listen(source)
  try:
    text = r.recognize_google(audio, language="ko")
  except sr.UnknownValueError:
    print("인식할 수 없습니다.")
  else:
    print("인식 결과 : ", text)
    if text == "종료":
      break
print("종료하였습니다.")


# 음성합성
import pyttsx3
engine = pyttsx3.init()
engine.say("안녕하세요? 인공지능입니다.")
engine.runAndWait()