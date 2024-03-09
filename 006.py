# 틱택토 게임 만들기
# 2차원 리스트 이용, 사용자는 행과 열을 콤마로 연결해서 선택, 사용자가 (0,0)을 입력할 경우 게임 종료

import random
class Tic_Tac_Toe:

  # 게임판 생성
  def __init__(self):
    self.board = []

  # 게임판 초기화
  def create_board(self):
    for i in range(3):
      row = []
      for j in range(3):
        row.append("*")
      self.board.append(row)

  # 첫 플레이어 선택
  def select_first_player(self):
    if random.randint(0, 1) == 0:
      return "X"
    else:
      return "O"

  # 기호 표시
  def mark_spot(self, row, col, player):
    self.board[row][col] = player

  # 승리 상태 확인
  def is_win(self, player):
    n = len(self.board)
    # 행 확인
    for i in range(n):
      win = True
      for j in range(n):
        if self.board[i][j] != player:
          win = False
          break
      if win == True:
        return win
    # 열 확인
    for i in range(n):
      win = True
      for j in range(n):
        if self.board[j][i] != player:
          win = False
          break
      if win == True:
        return win
    # 오른쪽 대각선 확인
    win = True
    for i in range(n):
      if self.board[i][i] != player:
        win = False
        break
    if win == True:
      return win
    # 왼쪽 대각선
    win = True
    for i in range(n):
      if self.board[i][n-i-1] != player:
        win = False
        break
    if win == True:
      return win
    return False

  #잔여 빈칸 여부 확인
  def is_board_full(self):
    for row in self.board:
      for item in row:
        if item == "*":
          return False
    return True

  # 플레이어 변경
  def next_player(self, player):
    if player == "O":
      return "X"
    else:
      return "O"
    # return "X" if player == "O" else "O"

  # 현재 게임판 상태 출력
  def show_board(self):
    for row in self.board:
      for item in row:
        print(item, end=" ")
      print()

  # 게임 시작
  def start(self):
    self.create_board()
    self.show_board()
    # 첫 플레이어 선택
    player = self.select_first_player()
    # 게임 루프 시작
    while True:
      if player == "X":
        print("컴퓨터 차례입니다.")
      else:
        print("사용자 차례입니다.")
      # 현재 게임판 상태 출력
      # self.show_board()
      # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
      if player == "X":
        while True:
          row, col = random.randint(1,3), random.randint(1,3) #사용자와 동일한 입력 상황을 맞춤
          if self.board[row-1][col-1] == "*":
            break
        print("컴퓨터가 " +str(row)+ "행, "+str(col)+ "열을/를 선택했습니다.")
      else:
        row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요 : ").split(",")))
        print("사용자가 " +str(row)+ "행, " +str(col)+ "열을/를 선택했습니다.")
        if self.board[row-1][col-1] != "*":
          player = "X"
          print("이미 선택되어있는 위치입니다. 다른곳을 선택해 주세요.")
      # row, col 입력값이 0,0인 경우 게임 종료
      if row == 0 and col == 0:
        break
      # 입력된 위치 표시
      self.mark_spot(row-1, col-1, player)
      self.show_board()
      # 현재 플레이어가 이겼는지 확인
      if self.is_win(player) == True:
        if player == "X":
          print("컴퓨터가 이겼습니다. 다시 도전하세요.")
        else:
          print("사용자가 이겼습니다. 축하합니다.")
        break
      # 게임판 가득참 확인, 빈칸 여부
      if self.is_board_full() == True:
        print("무승부입니다. 다시 도전하세요.")
        break
      # 플레이어 변경
      player = self.next_player(player)
    # 최종 게임판 출력
    print()
    self.show_board()

# 게임 생성
TTT = Tic_Tac_Toe()

#게임 시작
TTT.start()