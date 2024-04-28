"""
- 이름이 동일한 사람이 없다고 가정하고 사람을 찾을 때도 이름으로만 찾는다.
- 사전 안의 사전 {"홍정모":{"Phone":"1234-1234", "Email":"jh@abc.efg"}}
- 파일에 전화번호부를 저장해서 다시 시작할때 이전 데이터가 다시 불러들여지도록 구현
- 파일 저장 형식은 자유 (csv, json, pickle 등 자유)
- 스크립트 모드에서 구현 권장
- 디버거를 적극적으로 사용
"""

import os
import json


def main_menu() -> int:
    """사용자의 입력을 받아서 검증하고 적절하다면 정수로 반환합니다."""
    commend = input("(1)찾기, (2)추가/변경, (3)삭제, (4)모두 보기, (5)종료 : ")
    if commend not in ["1", "2", "3", "4", "5"]:
        print("잘못된 입력입니다.")
        return main_menu()
    return int(commend)


def show_all():
    """모든 데이터 출력"""
    if contact_data:
        for name, info in contact_data.items():
            print(f"{name} {info['Phone']} {info['Email']}")
    else:
        print("현재 등록된 연락처가 없습니다.")
        return True


def find_person():
    """이름을 입력받고 그 이름으로 찾아서 해당 데이터 출력"""
    name = input("이름을 입력해 주세요: ")
    if name in contact_data.keys():
        print(f"{name} {contact_data[name]['Phone']} {contact_data[name]['Email']}")
    else:
        print(f"{name}을/를 찾지 못했습니다.")
        return True


def update_person():
    """사람 추가 또는 수정
    사용자로부터 이름, 전화번호, 이메일을 입력받아서
    이미 있는 이름이면 업데이트를 하고
    없는 이름이면 새로 추가
    """

    name = input("이름을 입력해 주세요: ")
    if name not in contact_data.keys():
        phone = input("전화번호를 입력해 주세요: ")
        email = input("이메일을 입력해 주세요: ")
        contact_data[name] = {'Phone':phone, 'Email':email}
    else:
        print(f"{name}의 정보를 수정합니다.")
        phone = input("전화번호를 입력해 주세요: ")
        email = input("이메일을 입력해 주세요: ")
        contact_data[name] = {'Phone':phone, 'Email':email}


def delete_person():
    """이름을 입력받아서 데이터 삭제"""
    name = input("삭제할 사람의 이름을 입력해 주세요: ")
    if name in contact_data.keys():
        del contact_data[name]
        print(f"{name}정보를 삭제하였습니다.")
    else:
        print(f"{name}을/를 찾지 못했습니다.")
        return True


# 프로그램 실행의 시작
# 시작할 때 저장파일이 존재하면 읽어들여서 데이터 초기화
# 메인메뉴에서 사용자 입력을 받은 후에 알맞게 기능 수행
# 종료할 때 데이터 저장

# 전화번호부 저장용 dict (전역변수)
contact_data = {}

if os.path.isfile("my_contacts.json"):
    try:
        with open("my_contacts.json", encoding="utf8") as file:
            contact_data = json.load(file)
    except Exception as e:
        print("파일을 읽는 도중 오류가 발생했습니다:", e)

# main_menu()로 받아온 사용자의 입력에 따라 함수 호출
while True:
    selected = main_menu()
    if selected == 1:
        find_person()
    elif selected == 2:
        update_person()
    elif selected == 3:
        delete_person()
    elif selected == 4:
        show_all()
    elif selected == 5:
        # 종료하기 전 파일로 데이터 저장
        try:
            with open("my_contacts.json", "w", encoding="utf8") as file:
                json.dump(contact_data, file, indent=4, ensure_ascii=False)
            print("종료합니다.")
            break
        except Exception as e:
            print("파일을 저장하는 도중 오류가 발생했습니다:", e)
