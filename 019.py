# 음성 인터페이스 만들어보기 (py 3.11)

import speech_recognition as sr
from datetime import datetime
from io import BytesIO
from navertts import NaverTTS
from pydub import AudioSegment
from pydub.playback import play
import requests

r = sr.Recognizer()
microphone = sr.Microphone()
print(sr.Microphone.list_microphone_names())

while True:
  with microphone as source:
    r.adjust_for_ambient_noise(source)
    ai_answer = "음성 명령을 기다리는 중입니다."
    tts = NaverTTS(ai_answer, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)
    audio = r.listen(source)
  
  try:
    user = r.recognize_google(audio, language="ko")
  except Exception as e:
    print("명령을 인식할 수 없습니다.", e)
  else:
    print("음성 인식 결과 : ", user)
    
    if user in "종료":
      ai_answer = "음성인터페이스를 종료합니다."
    
    elif user in "시간":
      current_time = datetime.now()
      ai_answer = f"지금은 {current_time.hour}시 {current_time.minute}분 입니다."
    
    elif user in "날짜":
      today = datetime.today()
      ai_answer = f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다."
    
    elif user in "날씨":
      API_KEY = "88d6eee1ee4b6147b48668adf07947eb"
      BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
      requests_url = f"{BASE_URL}?appid={API_KEY}&q=Seoul&lang=Kr"
      response = requests.get(requests_url)
      if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"]-273.15, 2)
        ai_answer = f"현재 서울의 날씨는 {weather}입니다. 온도는 {temperature}도 입니다."
      else:
        ai_answer = "날씨 정보를 얻어 못했습니다."
    else:
      ai_answer = "알 수 없는 명령입니다."
    print(ai_answer)

    tts = NaverTTS(ai_answer, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)

    if user in "종료":
      break


# 덧붙일 내용 : 미세먼지 알려줘
# in을 썻는데도 "시간"은 인식하고 "지금 시간"은 인식하지 못함. 왜?
# 018에서도 시간과 날짜는 인식하지만 종료는 다른말과 덧붙였을때 인식하지 못함.