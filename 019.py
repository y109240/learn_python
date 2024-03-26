# 음성 인터페이스 만들어보기 (py 3.11)

import speech_recognition as sr
from datetime import datetime, timedelta
from io import BytesIO
from navertts import NaverTTS
from pydub import AudioSegment
from pydub.playback import play
import requests
from pytz import timezone

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

    cities_dict = {
      "서울":"Asia/Seoul",
      "뉴욕":"America/New_York",
      "로스앤젤레스":"America/Los_Angeles",
      "파리":"Europe/Paris",
      "런던":"Europe/London",
      }

    found = [found for found in cities_dict if found in user]
    if found:
      cities = found[0]
    else:
      cities = "서울"
    tz = timezone(cities_dict[cities])
    today = datetime.today().astimezone(tz)

  except Exception as e:
    print("명령을 인식할 수 없습니다.", e)
  else:
    print("음성 인식 결과 : ", user)
    
    if "종료" in user:
      ai_answer = "음성인터페이스를 종료합니다."
    
    elif "시간" in user:
      ai_answer = f"지금 {cities}은/는 {today.hour}시 {today.minute}분 입니다."
    
    elif "날짜" in user:
      ai_answer = f"현재 {cities}은/는 {today.year}년 {today.month}월 {today.day}일 입니다."
    
    elif "날씨" in user:
      API_KEY = "88d6eee1ee4b6147b48668adf07947eb"
      BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
      city = cities_dict[cities[0]][cities_dict[cities[0]].find("/")+1:]
      requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}&lang=Kr"
      response = requests.get(requests_url)

      if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"]-273.15, 2)
        ai_answer = f"현재 {cities}의 날씨는 {weather}입니다. 온도는 {temperature}도 입니다."
      else:
        ai_answer = "날씨 정보를 얻지 못했습니다."
    else:
      ai_answer = "알 수 없는 명령입니다."
    print(ai_answer)

    tts = NaverTTS(ai_answer, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)

    if "종료" in user:
      break


# 덧붙일 내용 : 미세먼지 알려줘
# in을 썻는데도 "시간"은 인식하고 "지금 시간"은 인식하지 못함. 왜? : in기준 반대로 씀
# 018에서도 시간과 날짜는 인식하지만 종료는 다른말과 덧붙였을때 인식하지 못함. 고침
# 날씨 정보에서 도시이름 찾아내는법?
