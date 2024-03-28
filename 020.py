import speech_recognition as sr
from datetime import datetime
from pytz import timezone
from io import BytesIO
from navertts import NaverTTS
from pydub import AudioSegment
from pydub.playback import play
import requests
from collections.abc import Callable

def speech_to_text() -> str:
  """음성 인식
  마이크로 사용자의 음성을 듣고 결과를 문자열로 반환
  Args:
    마이크와 음성인식기를 함수 안에서 초기화하기 때문에 인수 없음
  Returns:
    str: 음성 인식 결과 문자열. 실패시 빈 문자열 반환.
  """
  r = sr.Recognizer()
  microphone = sr.Microphone()
  with microphone as source:
    r.adjust_for_ambient_noise(source)
    print("음성 인식 대기중")
    audio = r.listen(source)
  text = r.recognize_google(audio, language="ko")
  print("인식 결과:", text)
  return text if text else ""



def text_to_speech(text: str) -> None:
  """음성 합성
  입력받은 문자열을 print()로 출력하고 TTS로 스피커로 출력
  Args:
    text (str): 음성 합성할 문자열
  """
  print(text)
  tts = NaverTTS(text, lang="ko")
  fp = BytesIO()
  tts.write_to_fp(fp)
  fp = BytesIO(fp.getvalue())
  my_sound = AudioSegment.from_file(fp, format="mp3")
  play(my_sound)



def report_daytime(user_command: str) -> None:
  """시간과 날짜 안내
  user_command에 "시간"이 포함되어 있으면 현재 시간 안내
  user_command에 "날짜"가 포함되어 있으면 현재 날짜 안내
  user_command에 도시 이름이 포함되어 있을 경우에는 그 도시 기준, 그렇지 않으면 기본 도시(예: "서울") 기준
  Args:
    user_command (str): 도시 이름을 찾아볼 사용자 명령문
  """

  cities_dict = {
    "서울": "Asia/Seoul",
    "뉴욕": "America/New_York",
    "로스앤젤레스": "America/Los_Angeles",
    "파리": "Europe/Paris",
    "런던": "Europe/London",
  }

  found = [found for found in cities_dict if found in user_command]
  if found:
    cities = found[0]
  else:
    cities = "서울"

  tz = timezone(cities_dict[cities])
  today = datetime.today().astimezone(tz)
  if "시간" in user_command:
    return text_to_speech(f"현재 {cities}의 시간은 {today.hour}시 {today.minute}분 입니다.")
  elif "날짜" in user_command:
    return text_to_speech(f"오늘 {cities}은/는 {today.year}년 {today.month}월 {today.day}일 입니다.")



def report_weather(user_command: str) -> None:
  """날씨 안내
  현재 날씨를 text_to_speech()를 사용해서 안내
  user_command에 도시 이름이 포함되어 있을 경우에는 그 도시의 날씨를 안내하고
  그렇지 않을 경우 기본 도시(예: "서울")의 날씨를 안내
  Args:
    user_command (str): 도시 이름을 찾아볼 사용자 명령문
  """

  API_KEY = "88d6eee1ee4b6147b48668adf07947eb"
  BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
  LANGUAGE = "kr"

  cities_dict = {
    "서울": "seoul",
    "뉴욕": "new york",
    "로스앤젤레스": "los angeles",
    "파리": "paris",
    "런던": "london",
  }

  user_command = speech_to_text()
  found = [found for found in cities_dict if found in user_command]
  if found:
    cities = found[0]
  else:
    cities = "서울"

  if "날씨" in user_command:
    requests_url = f"{BASE_URL}?appid={API_KEY}&q={cities_dict[cities]}&lang=Kr"
    response = requests.get(requests_url)
    if response.status_code == 200:
      data = response.json()
      weather = data["weather"][0]["description"]
      temperaturs = round(data["main"]["temp"]-273.15, 2)
      text_to_speech(f"현재 {cities}의 날씨는 {weather}, 온도는 {temperaturs}도 입니다.")
    else:
      text_to_speech("날씨 정보를 받아오지 못했습니다.")

