# 음성 인터페이스 만들어보기 (py 3.11)

import speech_recognition as sr
from datetime import datetime
from io import BytesIO
from navertts import NaverTTS
from pydub import AudioSegment
from pydub.playback import play

r = sr.Recognizer()
microphone = sr.Microphone()
print(sr.Microphone.list_microphone_names())

while True:
  with microphone as source:
    r.adjust_for_ambient_noise(source)
    tts = NaverTTS("음성 명령을 기다리는 중입니다.", lang="ko")
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
    if user in "종료":
      print("음성 인식 결과 : ", user)
      tts = NaverTTS("음성 인터페이스를 종료합니다.", lang="ko")
      fp = BytesIO()
      tts.write_to_fp(fp)
      fp = BytesIO(fp.getvalue())
      my_sound = AudioSegment.from_file(fp, format="mp3")
      play(my_sound)
      break

    elif "시간" in user:
      print("음성 인식 결과 : ", user)
      current_time = datetime.now()
      tts = NaverTTS(f"지금은 {current_time.hour}시 {current_time.minute}분 입니다.", lang="ko")
      fp = BytesIO()
      tts.write_to_fp(fp)
      fp = BytesIO(fp.getvalue())
      my_sound = AudioSegment.from_file(fp, format="mp3")
      play(my_sound)
    
    elif "날짜" in user:
      print("음성 인식 결과 : ", user)
      today = datetime.today()
      tts = NaverTTS(f"오늘은 {today.month}월 {today.day}일 입니다.", lang="ko")
      fp = BytesIO()
      tts.write_to_fp(fp)
      fp = BytesIO(fp.getvalue())
      my_sound = AudioSegment.from_file(fp, format="mp3")
      play(my_sound)

    else:
      tts = NaverTTS("알 수 없는 명령입니다.")
      fp = BytesIO()
      tts.write_to_fp(fp)
      fp = BytesIO(fp.getvalue())
      my_sound = AudioSegment.from_file(fp, format="mp3")
      play(my_sound)


# 덧붙일 내용 : 날씨 알려줘, 미세먼지 알려줘