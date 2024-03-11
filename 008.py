# 위에서 떨어지는 적 피하기 게임 만들기
# 조건
# 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
# 적은 화면 가장위에서 떨어짐, x좌표는 매번 랜덤으로 설정
# 캐릭터가 적을 피하면 다음적이 다시 떨어짐
# 캐릭터가 적과 충돌하면 게임종료
# FPS는 30으로 고정

import pygame
import random
# pylint: disable=no-member
pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("하늘에서 떨어지는 적 피하기")
clock = pygame.time.Clock()

# 배경
background = pygame.image.load("")
# 캐릭터
character = pygame.image.load("")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) /2
character_y_pos = screen_height - character_height
to_x = 0
character_speed = 1
# 적
enemy = pygame.image.load("")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.uniform(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.5

# 이벤트 루프
runnig = True
while runnig:
  dt = clock.tick(30)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0

  character_x_pos += to_x * dt
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width :
    character_x_pos = screen_width - character_width

  # 적이 위에서 떨어지도록
  enemy_y_pos += enemy_speed * dt
  if enemy_y_pos > screen_height:
    enemy_x_pos = random.uniform(0, screen_width - enemy_width)
    enemy_y_pos = 0

  # 충돌처리
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos
  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

  if character_rect.colliderect(enemy_rect):
    print("충돌")
    runnig = False

  # 화면에 그리기 
  screen.blit(background, (0,0))
  screen.blit(character, (character_x_pos, character_y_pos))
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
  pygame.display.update()
pygame.time.delay(500)
pygame.quit()
