# 굉장히 인기있는 굿즈상품 판매 예약받기
# 주문취소는 없다고 가정, 한번에 최대 주문개수는 3개로 제한

product = 20
waiting = 1

class SoldOutError(Exception):
  pass

while (True):
  try:
    print("남은상품 : {0}".format(product))
    order = int(input("몇개의 상품을 주문하시겠습니까? : "))
    if order > product :
      print("재료가 부족합니다.")
    elif order <1 or order >3 :
      raise ValueError
    else:
      print("[대기번호 : {0}] {1}개의 상품이 주문완료 되었습니다.".format(waiting, order))
      product -= order
      waiting += 1
    if product == 0:
      raise SoldOutError
  except ValueError:
    print("잘못된 값을 입력하였습니다.")
    print("최소 1개이상 최대 3개이하의 상품을 주문해 주세요.")
  except SoldOutError:
    print("모든상품이 판매완료되었습니다.")
    break