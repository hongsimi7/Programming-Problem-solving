import random

import os

from IPython.display import clear_output

def clear_screen():
    clear_output() 
    return

def print_stairs(user, com, stair_num):
    stairs = []
    if stair_num % 2 == 0: #짝수일 때, 계단 구현
        for i in range(stair_num // 2 + 1):
            stairs.append([])
            for j in range(stair_num + 1):
                stairs[i].append("  ")

        for i in range(1, stair_num // 2 + 1):
            for j in range(i):
                stairs[i][j] = "▨"
                stairs[i][stair_num - j] = "▨"
        
        if user <= (stair_num // 2): #짝수일 때, 유저 구현
            stairs[user][user] = "○"
        else:
            stairs[stair_num - user][user] = "○"

        if com <= (stair_num // 2): #짝수일 때, 컴퓨터 구현
            stairs[com][stair_num - com] = "●"
        else:
            stairs[stair_num - com][stair_num - com] = "●"

        if user == (stair_num - com): #짝수일 때, 겹칠 때 구현
            if user <= (stair_num // 2):
                stairs[user][user] = "◑"
            else:
                stairs[stair_num - user][user] = "◑"

    else: #홀수일 때, 계단 구현
        for i in range(stair_num // 2 + 2): 
            stairs.append([])
            for j in range(stair_num + 1):
                stairs[i].append("  ")
    
        for i in range(1, stair_num // 2 + 2):
            for j in range(i):
                stairs[i][j] = "▨"
                stairs[i][stair_num - j] = "▨"
        
        if user <= (stair_num // 2): #홀수일 때, 유저 구현
            stairs[user][user] = "○"
        elif user == (stair_num // 2 + 1):
            stairs[user-1][user] = "○"
        else:
            stairs[stair_num - user][user] = "○"

        if com <= (stair_num // 2): #홀수일 때, 컴퓨터 구현
            stairs[com][stair_num - com] = "●"
        elif com == (stair_num // 2 + 1):
            stairs[com - 1][stair_num - com] = "●"
        else:
            stairs[stair_num - com][stair_num - com] = "●"

        if user == (stair_num - com): #홀수일 때, 겹칠 때 구현
            if user <= (stair_num // 2):
                stairs[user][user] = "◑"
            elif user == (stair_num // 2 + 1):
                stairs[user-1][user] = "◑"
            else:
                stairs[stair_num - user][user] = "◑"

    print("총 계단 수: %d" %stair_num)
    print("PLAYER: ○ <%d>" %user)
    print("COMPUTER: ● <%d>" %com)

    for i in range(len(stairs)): #출력
        for j in range(len(stairs[i])):
            print(stairs[i][j],end="")
        print(" ")

def print_scissors():
    print("┌──────────────────┐")
    print("│                           ▩▩     │")
    print("│           ▩▩        ▩▩▩▩▩   │")
    print("│       ▩▩▩▩▩   ▩▩▩▩▩▩▩  │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩           │")
    print("│ ▩▩▩▩▩▩▩▩▩                 │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩             │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│   ▩▩▩▩▩▩▩  ▩▩▩▩▩▩▩   │")
    print("│     ▩▩▩▩▩▩      ▩▩▩▩▩   │")
    print("│         ▩▩▩            ▩▩     │")
    print("└──────────────────┘")
    
def print_rock():
    print("┌──────────────────┐")
    print("│                                    │")
    print("│       ▩▩▩▩▩                   │")
    print("│     ▩▩▩▩▩▩▩▩▩             │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩           │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩           │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩           │")
    print("│   ▩▩▩▩▩▩▩▩▩▩             │")
    print("│     ▩▩▩▩▩▩▩                 │")
    print("│                                    │")
    print("└──────────────────┘")
    
def print_paper():
    print("┌──────────────────┐")
    print("│                                    │")
    print("│       ▩▩▩▩▩                   │")
    print("│     ▩▩▩                         │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩               │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│ ▩▩▩▩▩▩▩▩▩▩               │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩               │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│     ▩▩▩▩▩                     │")
    print("│                                    │")
    print("└──────────────────┘")

def computer_choice():
    com_choice = random.choice(["가위","바위", "보"])
    return com_choice



print("======================") #초기화면 구현
print("[묵찌빠 계단 오르기]")
print("======================")
print("○                  ●")
print("▨                  ▨")
print("▨▨              ▨▨")
print("▨▨▨          ▨▨▨")
print("▨▨▨▨      ▨▨▨▨")
print("▨▨▨▨▨  ▨▨▨▨▨")
print("▨▨▨▨▨▨▨▨▨▨▨")


while True:               #계단 개수 입력
    stair = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))
    if stair > 30 or stair < 10:
        continue
    else:
        break
clear_screen()

player = 0                #필요 함수 정리
computer = 0
move = 1
syoubu = 0

while True:
    if player >= stair:                     #플레이어 최종 승리
        player = stair
        print_stairs(player,computer,stair)
        print("\n")
        print("▨"*(stair+1))
        print("  플레이어 최종 승리!!!")
        print("▨"*(stair+1))
        print("\n")
        print("게임을 종료합니다...")
        break
    
    if computer >= stair:                   #컴퓨터 최종 승리
        computer = stair
        print_stairs(player,computer,stair)
        print("\n")
        print("▨"*(stair+1))
        print("  컴퓨터 최종 승리!!!")
        print("▨"*(stair+1))
        print("\n")
        print("게임을 종료합니다...")
        break
        
    print_stairs(player,computer,stair)             #현재 계단 현황 출력
    next_page = input("계속하려면 엔터를 눌러주세요...")
    if next_page == "":
        clear_screen()

    while True:
        print("[공격권 결정 가위바위보]")
        while True:
            player_choice = input("가위, 바위, 보 중 하나 선택: ") #플레이어 가위바위보 선택
            if player_choice == "가위" or player_choice == "바위" or player_choice == "보":
                break
            else:
                continue
        com_choice = computer_choice() #컴퓨터 가위바위보 선택


        print("[컴퓨터 선택]")  #컴퓨터 가위바위보 출력
        if com_choice == "가위":
            print_scissors()
        elif com_choice == "바위":
            print_rock()
        else:
            print_paper()
        print("[플레이어 선택]")    #플레이어 가위바위보 출력
        if player_choice == "가위":
            print_scissors()
        elif player_choice == "바위":
            print_rock()
        else:
            print_paper()

        if com_choice == player_choice:         #무승부일 때
            print("[결과] 무승부입니다.")
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            continue
        elif com_choice == "가위" and player_choice == "바위":  #플레이어 공격일 때1
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
        elif com_choice == "바위" and player_choice == "보":      #플레이어 공격일 때2
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
        elif com_choice == "보" and player_choice == "가위":      #플레이어 공격일 때3
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
        else:                                                     #컴퓨터 공격일 때
            print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
            syoubu = 0
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
        break
    

    while True:
        print("[묵찌빠]")
        print("승리 시 이동 칸 수: %d" %move)
        if syoubu == 1:
            print("플레이어 공격, 컴퓨터 수비입니다.")
        else:
            print("컴퓨터 공격, 플레이어 수비입니다.")
        while True:
            player_choice = input("가위, 바위, 보 중 하나 선택: ") #플레이어 묵찌빠 선택
            if player_choice == "가위" or player_choice == "바위" or player_choice == "보":
                break
            else:
                continue
        com_choice = computer_choice() #컴퓨터 묵찌빠 선택


        print("[컴퓨터 선택]")  #컴퓨터 묵찌빠 출력
        if com_choice == "가위":
            print_scissors()
        elif com_choice == "바위":
            print_rock()
        else:
            print_paper()
        print("[플레이어 선택]")    #플레이어 묵찌빠 출력
        if player_choice == "가위":
            print_scissors()
        elif player_choice == "바위":
            print_rock()
        else:
            print_paper()

        if com_choice == player_choice: #결과 출력(승부 결정)
            print("[결과] 묵찌빠 종료")
            if syoubu == 1:                                   #플레이어 승
                print("플레이어 승, %d칸 이동합니다." %move)
                player += move

            else:                                              #컴퓨터 승
                print("컴퓨터 승, %d칸 이동합니다." %move)
                computer += move
            move = 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            break

        elif com_choice == "가위" and player_choice == "바위": #결과 출력(승부 결정 안남.), 플레이어 공격
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            move += 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            continue
        elif com_choice == "바위" and player_choice == "보":    #플레이어 공격
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            move += 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            continue
        elif com_choice == "보" and player_choice == "가위":    #플레이어 공격
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            syoubu = 1
            move += 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            continue
        else:                                                   #컴퓨터 공격
            print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
            syoubu = 0
            move += 1
            next_page = input("계속하려면 엔터를 눌러주세요...")
            if next_page == "":
                clear_screen()
            continue
        
