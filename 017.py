# 음성 인터페이스 만들어보기 (py 3.11)

import speech_recognition as sr
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
    tts = NaverTTS("음성 인식 대기중 입니다.", lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)
    audio = r.listen(source)

    user = r.recognize_google(audio, language="ko")

    print("인식결과 : ", user)
    tts = NaverTTS(user, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)

    if user == "종료":
      tts = NaverTTS("음성 인터페이스를 종료합니다.", lang="ko")
      fp = BytesIO()
      tts.write_to_fp(fp)
      fp = BytesIO(fp.getvalue())
      my_sound = AudioSegment.from_file(fp, format="mp3")
      play(my_sound)
      break