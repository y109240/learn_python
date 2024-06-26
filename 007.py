# pygame 간단한 게임 만들기
import os
import pygame
# pylint: disable=no-member
pygame.init() # 초기화 반드시필요

# 화면 크기 설정
screen_width = 480
screen_hight = 640
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀 설정
pygame.display.set_caption("Game name")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("경로")

# 캐릭터 스프라이터 불러오기
character = pygame.image.load("경로")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_hight = character_size[1]
character_x_pos = (screen_width - character_width) /2
character_y_pos = screen_hight - character_hight

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.5

# 적
enemy = pygame.image.load("경로")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_hight = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) /2
enemy_y_pos = (screen_hight - enemy_hight) /2

# 폰트정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)
# 총시간
total_time = 10
# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴

# 이벤트 루프
runnig = True # 게임이 진행중인가?
while runnig:
  dt = clock.tick(60) # 게임화면의 초당 프레임수를 설정
  # print("fps : " + str(clock.get_fps)) # fps확인
  for event in pygame.event.get(): # 어떤 이벤트가 발생했는지
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는지
      running = False # 게임이 진핸중이 아님
    if event.type == pygame.KEYDOWN: # 키보드를 눌렀는지 확인
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
      elif event.key == pygame.K_UP:
        to_y -= character_speed
      elif event.key == pygame.K_DOWN:
        to_y += character_speed
    if event.type == pygame.KEYUP: # 키보드를 떼면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
  
  character_x_pos += to_x * dt
  character_y_pos += to_y * dt
  # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width :
    character_x_pos = screen_width - character_width
  # 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_hight - character_hight :
    character_y_pos = screen_hight - character_hight

  # 충돌처리를 위한 rect 정보 업데이트
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos
  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

  # 충돌체크
  if character_rect.colliderect(enemy_rect):
    print("충돌")
    runnig = False

  screen.blit(background, (0,0)) # 배경 그리기
  screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

  # 타이머 집어 넣기
  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000 # 경과시간(ms)을 1000으로 나누어서 초 단위로 표시
  timer = game_font.render(str(int(total_time - elapsed_time)), True, ("#FFFFFF"))
  screen.blit(timer, (10, 10))
  if total_time - elapsed_time <= 0:
    print("타임아웃")
    runnig = False

  pygame.display.update() # 게임화면을 다시 그리기

pygame.time.delay(1000) # 1초정도 대기

pygame.quit()