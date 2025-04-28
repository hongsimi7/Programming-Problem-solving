import random
import copy
import os

def print_score_board(score_list):                  #점수판 출력

    score_list2 = copy.deepcopy(score_list)          #변수 리스트 변형시키지 않기 위함.
    score_list3 = copy.deepcopy(score_list)

    for score_line in score_list2:                  #점수 문자열에서 정수로 변환 및  'x'를 0으로 변환
        for i in range(1,3):
            if score_line[i] == 'x':
                score_line[i] = 0
            else:
                score_line[i] = int(score_line[i])

    sub_total_1 = score_list2[0][1] + score_list2[1][1] + score_list2[2][1] + score_list2[3][1] + score_list2[4][1] + score_list2[5][1]             #점수 sub_total
    sub_total_2 = score_list2[0][2] + score_list2[1][2] + score_list2[2][2] + score_list2[3][2] + score_list2[4][2] + score_list2[5][2]

    total_1 = sub_total_1 + score_list2[6][1] + score_list2[7][1] + score_list2[8][1] + score_list2[9][1] + score_list2[10][1] + score_list2[11][1]     #점수 total
    total_2 = sub_total_2 + score_list2[6][2] + score_list2[7][2] + score_list2[8][2] + score_list2[9][2] + score_list2[10][2] + score_list2[11][2]

    if score_list[0][1] != 'x' and score_list[1][1] != 'x' and score_list[2][1] != 'x' and score_list[3][1] != 'x' and score_list[4][1] != 'x' and score_list[5][1] != 'x':     #player의 점수판에 1부터 6까지 다 채워져 있을 때
        if sub_total_1 >= 63:           #보너스 점수 획득
            bonus_score_1 = 35
            total_1 += bonus_score_1    
        else:                           #보너스 점수 획득 실패
            bonus_score_1 = 0

    else:                               #1부터 6까지 다 채워지지 않았지 않은 경우                             
        if sub_total_1 >= 63:           #보너스 점수 획득
            bonus_score_1 = 35
            total_1 += bonus_score_1    
        else:
            bonus_score_1 = ''

    if score_list[0][2] != 'x' and score_list[1][2] != 'x' and score_list[2][2] != 'x' and score_list[3][2] != 'x' and score_list[4][2] != 'x' and score_list[5][2] != 'x':     #computer의 점수판에 1부터 6까지 다 채워져 있을 때
        if sub_total_2 >= 63:           #보너스 점수 획득
            bonus_score_2 = 35
            total_2 += bonus_score_2
        else:                           #보너스 점수 획득 실패
            bonus_score_2 = 0

    else:                               #1부터 6까지 다 채워지지 않았지 않은 경우
        if sub_total_2 >= 63:           #보너스 점수 획득
            bonus_score_2 = 35
            total_2 += bonus_score_2
        else:
            bonus_score_2 = ''

    


    for score_line in score_list3:                  #출력을 위해 정수에서 문자열로 변환 및 'x'을 공백으로 변환
        for i in range(1,3):
            if score_line[i] == 'x':
                score_line[i] = ''
            else:
                score_line[i] =str(score_line[i])

    print("┌──────────┬──────────┐")
    print("│       Player       │      Computer      │")
    print("├──────────┴──────────┤")
    print("│ 1:         %2s      │ 1:         %2s      │" %(score_list3[0][1], score_list3[0][2]))
    print("│ 2:         %2s      │ 2:         %2s      │" %(score_list3[1][1], score_list3[1][2]))
    print("│ 3:         %2s      │ 3:         %2s      │" %(score_list3[2][1], score_list3[2][2]))
    print("│ 4:         %2s      │ 4:         %2s      │" %(score_list3[3][1], score_list3[3][2]))
    print("│ 5:         %2s      │ 5:         %2s      │" %(score_list3[4][1], score_list3[4][2]))
    print("│ 6:         %2s      │ 6:         %2s      │" %(score_list3[5][1], score_list3[5][2]))
    print("├─────────────────────┤")
    print("│ Sub total: %2d/63   │ Sub total: %2d/63   │" %(sub_total_1, sub_total_2))
    
    if bonus_score_1 == 0 and bonus_score_2 == 0:                                                           #점수판의 칸을 맞추기 위한 작업
        print("│ +35 bonus: %s       │ +35 bonus: %s       │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == 0 and bonus_score_2 == 35:
        print("│ +35 bonus: %s       │ +35 bonus: +%2s     │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == 35 and bonus_score_2 == 0:
        print("│ +35 bonus: +%2s     │ +35 bonus: %s       │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == 35 and bonus_score_2 == 35:
        print("│ +35 bonus: +%2s     │ +35 bonus: +%2s     │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == '' and bonus_score_2 == 35:
        print("│ +35 bonus: %2s      │ +35 bonus: +%2s     │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == 35 and bonus_score_2 == '':
        print("│ +35 bonus: +%2s     │ +35 bonus: %2s      │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_1 == 0:
        print("│ +35 bonus: %s       │ +35 bonus: %2s      │" %(str(bonus_score_1),str(bonus_score_2)))
    elif bonus_score_2 == 0:
        print("│ +35 bonus: %2s      │ +35 bonus: %s       │" %(str(bonus_score_1),str(bonus_score_2)))
    else:
        print("│ +35 bonus: %2s      │ +35 bonus: %2s      │" %(str(bonus_score_1),str(bonus_score_2)))

    print("├─────────────────────┤")
    print("│ C:         %2s      │ C:         %2s      │" %(score_list3[6][1], score_list3[6][2]))
    print("├─────────────────────┤")
    print("│ 4K:        %2s      │ 4K:        %2s      │" %(score_list3[7][1], score_list3[7][2]))
    print("│ FH:        %2s      │ FH:        %2s      │" %(score_list3[8][1], score_list3[8][2]))
    print("│ SS:        %2s      │ SS:        %2s      │" %(score_list3[9][1], score_list3[9][2]))
    print("│ LS:        %2s      │ LS:        %2s      │" %(score_list3[10][1], score_list3[10][2]))
    print("│ Yacht:     %2s      │ Yacht:     %2s      │" %(score_list3[11][1], score_list3[11][2]))
    print("├─────────────────────┤")
    print("│ Total:    %3d      │ Total:    %3d      │" %(total_1, total_2))
    print("└─────────────────────┘")


def load_file2list(filename):                   #파일 불러오기
    score_list = []
    score_file = open(filename, "r")            #파일 열기
    
    while True:
        score = score_file.readline().split()   #한 줄씩 받아드림

        if score == []:                         #파일이 끝났을 때
            break
        
        score_list.append(score)                #점수를 리스트로 저장
    
    score_file.close()                          #파일 닫기

    return score_list
            

def check_error(score_list):                #올바른 파일인지 확인
    
    count = 0
    sorted_score_list = []
    for i in range(len(score_list)):        #총 줄의 개수 세기
        count += 1

    if len(score_list) != 12:               #총 줄의 개수가 12가 아닌 경우(오류 1)
        return 1
    
    for i in range(1, 7):                               #점수 정렬
        for j in range(0, 12):
            sel = "%d:" %i
            if score_list[j][0] == sel:
                sorted_score_list.append(score_list[j])
    for i in range(0, 12):
        if score_list[i][0] == 'C:':
            sorted_score_list.append(score_list[i])
    for i in range(0, 12):
        if score_list[i][0] == '4K:':
            sorted_score_list.append(score_list[i])
    for i in range(0, 12):
        if score_list[i][0] == 'FH:':
            sorted_score_list.append(score_list[i])
    for i in range(0, 12):
        if score_list[i][0] == 'SS:':
            sorted_score_list.append(score_list[i])
    for i in range(0, 12):       
        if score_list[i][0] == 'LS:':
            sorted_score_list.append(score_list[i])
    for i in range(0, 12):
        if score_list[i][0] == 'Y:':
            sorted_score_list.append(score_list[i])

    score_list = sorted_score_list
    
    if score_list[0][1] not in ['0', '1', '2', '3', '4', '5', 'x'] or score_list[0][2] not in ['0', '1', '2', '3', '4', '5', 'x']:            #Aces 점수 확인(오류 2)          
        return 2

    if score_list[1][1] not in ['0', '2', '4', '6', '8', '10', 'x'] or score_list[1][2] not in ['0','2', '4', '6', '8', '10', 'x']:           #Deuces 점수 확인(오류 2)
        return 2

    if score_list[2][1] not in ['0', '3', '6', '9', '12', '15', 'x'] or score_list[2][2] not in ['0', '3', '6', '9', '12', '15', 'x']:        #Threes 점수 확인(오류 2)
        return 2
    
    if score_list[3][1] not in ['0', '4', '8', '12', '16', '20', 'x'] or score_list[3][2] not in ['0', '4', '8', '12', '16', '20', 'x']:      #Fours 점수 확인(오류 2)
        return 2
    
    if score_list[4][1] not in ['0', '5', '10', '15', '20', '25', 'x'] or score_list[4][2] not in ['0', '5', '10', '15', '20', '25', 'x']:    #Fives 점수 확인(오류 2)
        return 2
    
    if score_list[5][1] not in ['0', '6', '12', '18', '24', '30', 'x'] or score_list[5][2] not in ['0', '6', '12', '18', '24', '30', 'x']:    #Sixes 점수 확인(오류 2)
        return 2
        
    if score_list[6][1] not in [str(i) for i in range(1, 31)]+ ['0','x']  or score_list[6][2] not in [str(i) for i in range(1, 31)] + ['0','x']:      #Choice 점수 확인(오류 2)
        return 2

    if score_list[7][1] not in [str(i+j) for i in range(4, 25, 4) for j in range(1, 7)] + ['0','x'] or score_list[7][2] not in [str(i+j) for i in range(4, 25, 4) for j in range(1, 7)] + ['0','x'] :     #4 of a Kind 점수 확인(오류 2)     
        return 2

    if score_list[8][1] not in [str(i*2 + j*3) for i in range(1, 7) for j in range(1, 7)] + ['0','x'] or score_list[8][2] not in [str(i*2 + j*3) for i in range(1, 7) for j in range(1, 7)] + ['0','x'] : #Full House 점수 확인(오류 2)
        return 2
    
    if score_list[9][1] not in ['0', '15', 'x'] or score_list[9][2] not in ['0', '15', 'x']:    #Small Straight 점수 확인(오류 2)
        return 2

    if score_list[10][1] not in ['0', '30', 'x'] or score_list[10][2] not in ['0', '30', 'x']:    #Large Straight 점수 확인(오류 2)
        return 2

    if score_list[11][1] not in ['0', '50', 'x'] or score_list[11][2] not in ['0', '50', 'x']:    #Yacht 점수 확인(오류 2)
        return 2
    
    return score_list              #유효한 파일인 경우

    
def roll_dice(dice_set=[], reroll_indices=[]):      #주사위 던지기
    
    new_dice_set = copy.deepcopy(dice_set)  #변수 리스트 변형 안시키기 위함.

    if dice_set == []:     #주사위 처음 굴릴 때
        for i in range(1,6):
            num = random.randint(1,6)
            new_dice_set.append(num)
    
    else:                   #주사위 다시 굴릴 때
        for dice_num in reroll_indices:
            new_dice_set[dice_num-1] = random.randint(1,6)

    return new_dice_set

        
def calc_score(dice_set, sel, score_list, turn):          # 점수 계산
    while True:
        if sel == '1' and score_list[0][turn] == 'x':  #1 선택
            count = 0
        
            for num in dice_set:
                if num == 1:
                    count += 1 
                    
            score_list[0][turn] = count * 1
                
        elif sel == '2' and score_list[1][turn] == 'x':  #2 선택
            count = 0
                    
            for num in dice_set:
                if num == 2:
                    count += 1 
                    
                score_list[1][turn] = count * 2

        elif sel == '3' and score_list[2][turn] == 'x':  #3 선택
            count = 0
                    
            for num in dice_set:
                if num == 3:
                    count += 1 
                    
            score_list[2][turn] = count * 3

        elif sel == '4' and score_list[3][turn] == 'x':  #4 선택
            count = 0
                    
            for num in dice_set:
                if num == 4:
                    count += 1 
                    
            score_list[3][turn] = count * 4
                
        elif sel == '5' and score_list[4][turn] == 'x':  #5 선택
            count = 0
                    
            for num in dice_set:
                if num == 5:
                    count += 1 
                    
            score_list[4][turn] = count * 5
                
        elif sel == '6' and score_list[5][turn] == 'x':  #6 선택
            count = 0
                    
            for num in dice_set:
                if num == 6:
                    count += 1 
                    
            score_list[5][turn] = count * 6

        elif sel == 'C' or sel == 'c' and score_list[6][turn] == 'x':   #C 선택
            total = 0

            for num in dice_set:
                total += num

            score_list[6][turn] = total

        elif sel == '4K' or sel == '4k' and score_list[7][turn] == 'x':   #4K 선택
            total = 0

            if dice_set in [sorted([x,x,x,x,y]) for x in range(1,7) for y in range(1,7)]:  #4K 경우의 수
                for num in dice_set:
                    total += num

            score_list[7][turn] = total

        elif sel == 'FH' or sel == 'fh' or sel == 'Fh' or sel == 'fH' and score_list[8][turn] == 'x':   #FH 선택
            total = 0

            if dice_set in [sorted([x,x,x,y,y]) for x in range(1,7) for y in range(1,7)]:  #FH 경우의 수
                for num in dice_set:
                    total += num
        
            score_list[8][turn] = total
        
        elif sel == 'SS' or sel == 'ss' or sel == 'Ss' or sel == 'sS' and score_list[9][turn] == 'x':   #SS 선택
            total = 0

            if dice_set in [sorted([x,x+1,x+2,x+3,y]) for x in range(1,4) for y in range(1,7)]:  #SS 경우의 수
                    total = 15
        
            score_list[9][turn] = total

        elif sel == 'LS' or sel == 'ls' or sel == 'Ls' or sel == 'lS' and score_list[10][turn] == 'x':   #LS 선택
            total = 0

            if dice_set in [sorted([x,x+1,x+2,x+3,x+4]) for x in range(1,3)]:  #LS 경우의 수
                    total = 30
        
            score_list[10][turn] = total

        elif sel == 'Y' or sel == 'y' and score_list[11][turn] == 'x':   #Y 선택
            total = 0

            if dice_set in [sorted([x,x,x,x,x]) for x in range(1,7)]:  #Y 경우의 수
                    total = 50
        
            score_list[11][turn] = total

        else:                                   #점수가 들어있는 칸을 선택한 경우 혹은 sel을 잘못 입력한 경우
            print("Wrong Input!")
            sel = input("Choose a category: ")
            continue

        break

    return score_list


def computer_pattern(dice_set, score_list):             #컴퓨터의 선택
    cpy_dice_set = copy.deepcopy(dice_set)
    cpy_dice_set = sorted(cpy_dice_set)                 #주사위 리스트 정렬
    score_dict = dict()                                 #key 값은 sel, value 값은 점수로 받을 딕셔너리 생성
    reroll_indices = []

    if score_list[0][2] == 'x':                         #점수가 입력이 되지 않았을 때의 1
        score_dict["1"] = cpy_dice_set.count(1) * 1
    if score_list[1][2] == 'x':                         #점수가 입력이 되지 않았을 때의 2
        score_dict["2"] = cpy_dice_set.count(2) * 2
    if score_list[2][2] == 'x':                         #점수가 입력이 되지 않았을 때의 3
        score_dict["3"] = cpy_dice_set.count(3) * 3
    if score_list[3][2] == 'x':                         #점수가 입력이 되지 않았을 때의 4
        score_dict["4"] = cpy_dice_set.count(4) * 4
    if score_list[4][2] == 'x':                         #점수가 입력이 되지 않았을 때의 5
        score_dict["5"] = cpy_dice_set.count(5) * 5
    if score_list[5][2] == 'x':                         #점수가 입력이 되지 않았을 때의 6
        score_dict["6"] = cpy_dice_set.count(6) * 6
    if score_list[6][2] == 'x':                         #점수가 입력이 되지 않았을 때의 C
        if sum(cpy_dice_set) >= 20:                     #점수가 20이상일 때
            c = sum(cpy_dice_set)
        else:                                           #점수가 20미만일 때
            c = 0       
        score_dict['C'] = c
    if score_list[7][2] == 'x':                                                                 #점수가 입력이 되지 않았을 때의 4K
        if cpy_dice_set in [sorted([x,x,x,x,y]) for x in range(1,7) for y in range(1,7)]:
            fourk = sum(cpy_dice_set)
        else:
            fourk = 0
        score_dict['4K'] = fourk
    if score_list[8][2] == 'x':                                                                 #점수가 입력이 되지 않았을 때의 FH
        if cpy_dice_set in [sorted([x,x,x,y,y]) for x in range(1,7) for y in range(1,7)]:    
            fh = sum(cpy_dice_set)
        else:
            fh = 0
        score_dict['FH'] = fh
    if score_list[9][2] == 'x':                                                                 #점수가 입력이 되지 않았을 때의 SS
        if cpy_dice_set in [sorted([x,x+1,x+2,x+3,y]) for x in range(1,4) for y in range(1,7)]:
            ss = 15
        else:
            ss = 0
        score_dict['SS'] = ss    
    if score_list[10][2] == 'x':                                                                #점수가 입력이 되지 않았을 때의 LS
        if cpy_dice_set in [[x,x+1,x+2,x+3,x+4] for x in range(1,3)]:
            ls = 30
        else:
            ls = 0
        score_dict['LS'] = ls
    if score_list[11][2] == 'x':                                                                #점수가 입력이 되지 않았을 때의 Y
        if cpy_dice_set in [[x,x,x,x,x] for x in range(1, 7)]:
            y = 50
        else:
            y = 0
        score_dict['Y'] = y

    score_dict_value = sorted(score_dict.values())      #value 값을 오름차순으로 정렬
    high_score = score_dict_value[-1]                   #value 값 중 가장 큰 것 선택

    for element in score_dict.keys():                   #가장 큰 점수와 value 값이 같은 key 선택
        if score_dict[element] == high_score:
            sel = element
            break

    if sel in ['1','2','3','4','5','6']:            #만약 1부터 6이라면, 선택된 수 이외의 모든 수 다시 던지기 위해 리스트 작성
        count = 1
        for i in dice_set:
            if i != int(sel):
                reroll_indices.append(count)
            count += 1

    elif sel == 'C':                                #만약 C라면, 3이하의 모든 수를 다시 던지기 위해 리스트 작성
        count  = 1
        for i in dice_set:
            if i <= 3:
                reroll_indices.append(count)
            count += 1

    else:                                          #만약 4K, FH, SS, LS, Y이고 그 값이 완성이 되었다면, 다시 던지지 않음.
        if score_dict[sel] != 0:
            reroll_indices = []
        else:                                      #만약 4K, FH, SS, LS, Y이고 그 값이 완성이 되지 않았다면, 다시 던짐.
            reroll_indices = [1, 2, 3, 4, 5]       
        
    return sel, reroll_indices


while True:                                         #메인 함수
    print("[Yacht Dice]")
    print("----------------------------------")
    print("1. New Game  2. Load Game  3. Exit")
    print("----------------------------------")
    
    while True:
        selction = int(input("Select a menu: "))        
        if selction in [1, 2, 3]:       #정상 입력
            break
        else:                           #오류
            print("Wrong Input!\n") 

    if selction == 1:                   #새로운 게임 시작
        print("")
        print("Starting a game...")
        score_list = [['1:', 'x', 'x'], ['2:', 'x', 'x'], ['3:', 'x', 'x'], ['4:', 'x', 'x'], ['5:', 'x', 'x'], ['6:', 'x', 'x'], ['C:', 'x', 'x'], ['4K:', 'x', 'x'], ['FH:', 'x', 'x'], ['SS:', 'x', 'x'], ['LS:', 'x', 'x'], ['Y:', 'x', 'x']]   #점수판 생성
        player_turn = 1
        computer_turn = 1
        reroll_indices = "Q"
        player_choice = "Q"

        while True:
            dice_set = roll_dice()    #플레이어 차례 및 첫 주사위 굴리기

            print_score_board(score_list)   #점수판 출력
            print("")
            print("[Player's Turn (%d/12)]" %(player_turn))     #플레이어 턴 출력
            print(f"Roll: {dice_set}")                          #주사위 출력

            while True:
                try:
                    reroll_indices = input("Which dice to reroll (1~5)? ")      #다시 굴릴 주사위 입력
                    
                    if reroll_indices in ["Q", "q"]:                                           #게임 중단
                        print("")
                        save_file = input("Game paused. Enter the filename to save:\n")        #저장할 파일 이름 입력
                        break

                            
                    reroll_indices = reroll_indices.split()
                    delete_list = []

                    for i in range(len(reroll_indices)):                        #리스트 원소 정수형으로 바꾸기
                        reroll_indices[i] = int(reroll_indices[i])
                                
                        if reroll_indices[i] not in [1, 2, 3, 4, 5]:            #잘못 받은 숫자 확인
                            delete_list.append(reroll_indices[i])


                    reroll_indices = set(reroll_indices) - set(delete_list)     #잘못 받은 숫자 지우기 및 중복 제거
                    reroll_indices = list(reroll_indices)
                    if reroll_indices in ["", []]:                                    #주사위 다시 안굴릴 때
                        break
                    dice_set = roll_dice(dice_set, reroll_indices)
                    print(f"Roll: {dice_set}")              #주사위 출력

                    while True:
                        try:
                            reroll_indices = input("Which dice to reroll (1~5)? ")      #다시 굴릴 주사위 입력
                            

                            if reroll_indices in ["Q", "q"]:                                           #게임 중단
                                print("")
                                save_file = input("Game paused. Enter the filename to save:\n") #저장할 파일 이름 입력
                                break

                                
                            reroll_indices = reroll_indices.split()
                            delete_list = []

                            for i in range(len(reroll_indices)):                        #리스트 원소 정수형으로 바꾸기
                                reroll_indices[i] = int(reroll_indices[i])
                                    
                                if reroll_indices[i] not in [1, 2, 3, 4, 5]:            #잘못 받은 숫자 확인
                                    delete_list.append(reroll_indices[i])


                            reroll_indices = set(reroll_indices) - set(delete_list)     #잘못 받은 숫자 지우기 및 중복 제거
                            reroll_indices = list(reroll_indices)
                            
                            if reroll_indices in ["", []]:                                    #주사위 다시 안굴릴 때
                                break
                                
                            dice_set = roll_dice(dice_set, reroll_indices)
                            print(f"Roll: {dice_set}")                                  #주사위 출력       
                            break

                        except:
                            print("Wrong input!")       #스페이스 또는 숫자 외 다른 문자를 입력 받았을 때, 오류 

                    break

                except:
                    print("Wrong input!")               #스페이스 또는 숫자 외 다른 문자를 입력 받았을 때, 오류 
            
            if reroll_indices in ["Q", "q"]:                   #게임 중단
                break

            print("")
            dice_set = sorted(dice_set)         #주사위 정렬
            print(f"Sorted Roll: {dice_set}")
            
            while True:
                player_choice = input("Choose a category: ")
                if player_choice in ["Q", "q"]:                                                #게임 중단
                    print("")
                    save_file = input("Game paused. Enter the filename to save:\n")     #저장할 파일 이름 입력
                    break

                elif player_choice in ['1', '2', '3', '4', '5', '6', 'C', 'c', '4k', '4K', 'fh', 'fH', 'Fh', 'FH', 'ss','Ss', 'sS', 'SS', 'ls', 'Ls', 'lS', 'LS', 'y', 'Y']:    #player가 sel을 올바르게 선택했을 때
                    break

                else:                           #player가 sel을 올바르지 않게 선택했을 때
                    print("Wrong Input!")
                    continue

            if player_choice in ["Q", "q"] or reroll_indices in ["Q", "q"]:                       #게임 중단
                break

            score_list = calc_score(dice_set, player_choice, score_list, 1)         #점수판에 점수 입력
            
            print("")
            
            print_score_board(score_list)       #점수판 출력

            player_turn += 1                    #턴 추가

            dice_set = roll_dice()              #컴퓨터 차례 및 첫 번째 주사위 굴리기
            print("\n[Computer's Turn (%d/12)]" %(computer_turn))     #컴퓨터 턴 출력
            print(f"Roll: {dice_set}")              #1번째 주사위 출력

            sel, reroll_indices = computer_pattern(dice_set, score_list)        #컴퓨터의 선택

            print(f"Which dice to reroll (1~5)?", end = ' ')                    #컴퓨터의 다시 굴릴 주사위 출력
            for i in reroll_indices:
                print(f"{i}", end = ' ')
            print("")

            while True:
                if reroll_indices == []:                #다시 굴릴 주사위가 없는 경우
                    break

                dice_set = roll_dice(dice_set, reroll_indices)
                print(f"Roll: {dice_set}")              #2번째 주사위 출력
                sel, reroll_indices = computer_pattern(dice_set, score_list)    #컴퓨터의 선택
                print(f"Which dice to reroll (1~5)?", end = ' ')                #컴퓨터의 다시 굴릴 주사위 출력
                for i in reroll_indices:
                    print(f"{i}", end = ' ')
                print("")

                if reroll_indices == []:                #다시 굴릴 주사위가 없는 경우
                    break

                dice_set = roll_dice(dice_set, reroll_indices)      
                print(f"Roll: {dice_set}")                                          #3번째 주사위 출력
                sel, reroll_indices = computer_pattern(dice_set, score_list)        #컴퓨터의 선택

                break

            dice_set = sorted(dice_set)             #주사위 정렬
            print("")
            print(f"Sorted Roll: {dice_set}")       #정렬된 주사위 출력
            print(f"Choose a category: {sel}")      #컴퓨터의 선택 출력
            print("")
            
            score_list = calc_score(dice_set, sel, score_list, 2)       #점수판의 컴퓨터의 점수 입력

            computer_turn += 1                              #턴 추가

            if player_turn == 13 and computer_turn == 13:   #게임이 끝났을 때
                break
        
        if player_choice in ['Q', 'q'] or reroll_indices in ["Q", "q"]:   #게임 중단
            outfile = open(save_file, "w")                  #파일 쓰기 모드로 열기
            
            for score in score_list:
                outfile.write("%s %s %s\n" %(score[0],score[1],score[2]))

            outfile.close()                                 #파일 닫기
            print("File saved.\n")
            continue
            

        print("<Final Score Board>")                        #최종 점수판 출력
        print_score_board(score_list)
        
        player_score = 0                                    #플레이어 및 컴퓨터 점수 합산
        computer_score = 0
        sub_total1 = 0
        sub_total2 = 0
        for i in range(0, 12):
            player_score += int(score_list[i][1])
            computer_score += int(score_list[i][2])
        for i in range(0, 6):
            sub_total1 += int(score_list[i][1])
            sub_total2 += int(score_list[i][2])
        
        if sub_total1 >= 63:
            player_score += 35
        if sub_total2 >= 63:
            computer_score += 35
            

        if player_score > computer_score:                   #플레이어 승리
            print("You win!")
        elif player_score == computer_score:                #무승부
            print("Draw")
        else:                                               #컴퓨터 승리
            print("You lose!")

        print("")
        restart = input("Press Enter to continue...")       #엔터키 입력시 초기화면으로 돌아가기
        if restart == "":
            print("")
            continue

       
    elif selction == 2:                 #게임 이어하기
        while True:
            print("")
            load_file = input("Enter filename to load: ")
            if os.path.exists(load_file):                   #파일이 존재할 때
                score_list = load_file2list(load_file)
                score_list = check_error(score_list)
                
                if score_list == 1:              #1번 오류
                    print("File does not exist.")
                    continue
                elif score_list == 2:            #2번 오류
                    print("Invalid file content.")
                    continue
                else:                                       
                    break
            else:                                           #파일이 존재하지 않을 때
                print("File does not exist.")
                continue

        
        print("Starting a game...")
        player_turn = 13
        computer_turn = 13
        reroll_indices = "Q"
        player_choice = "Q"

        for i in range(0, 12):              #진행된 턴 수 확인
            if score_list[i][1] == 'x':
                player_turn -= 1
            if score_list[i][2] == 'x':
                computer_turn -= 1

        while True:
            dice_set = roll_dice()    #플레이어 차례 및 첫 주사위 굴리기

            print_score_board(score_list)   #점수판 출력
            print("")
            print("[Player's Turn (%d/12)]" %(player_turn))     #플레이어 턴 출력
            print(f"Roll: {dice_set}")                          #주사위 출력

            while True:
                try:
                    reroll_indices = input("Which dice to reroll (1~5)? ")      #다시 굴릴 주사위 입력
                    
                    if reroll_indices in ["Q", "q"]:                                           #게임 중단
                        print("")
                        save_file = input("Game paused. Enter the filename to save:\n")        #저장할 파일 이름 입력
                        break

                            
                    reroll_indices = reroll_indices.split()
                    delete_list = []

                    for i in range(len(reroll_indices)):                        #리스트 원소 정수형으로 바꾸기
                        reroll_indices[i] = int(reroll_indices[i])
                                
                        if reroll_indices[i] not in [1, 2, 3, 4, 5]:            #잘못 받은 숫자 확인
                            delete_list.append(reroll_indices[i])


                    reroll_indices = set(reroll_indices) - set(delete_list)     #잘못 받은 숫자 지우기 및 중복 제거
                    reroll_indices = list(reroll_indices)

                    if reroll_indices in ["", []]:                                    #주사위 다시 안굴릴 때
                        break

                    dice_set = roll_dice(dice_set, reroll_indices)
                    print(f"Roll: {dice_set}")              #주사위 출력

                    while True:
                        try:
                            reroll_indices = input("Which dice to reroll (1~5)? ")      #다시 굴릴 주사위 입력

                            if reroll_indices in ["Q", "q"]:                                           #게임 중단
                                print("")
                                save_file = input("Game paused. Enter the filename to save:\n") #저장할 파일 이름 입력
                                break

                                
                            reroll_indices = reroll_indices.split()
                            delete_list = []

                            for i in range(len(reroll_indices)):                        #리스트 원소 정수형으로 바꾸기
                                reroll_indices[i] = int(reroll_indices[i])
                                    
                                if reroll_indices[i] not in [1, 2, 3, 4, 5]:            #잘못 받은 숫자 확인
                                    delete_list.append(reroll_indices[i])


                            reroll_indices = set(reroll_indices) - set(delete_list)     #잘못 받은 숫자 지우기 및 중복 제거
                            reroll_indices = list(reroll_indices)
                            

                            if reroll_indices in ["", []]:                                    #주사위 다시 안굴릴 때
                                break
                                
                            dice_set = roll_dice(dice_set, reroll_indices)
                            print(f"Roll: {dice_set}")                                  #주사위 출력       
                            break

                        except:
                            print("Wrong input!")       #스페이스 또는 숫자 외 다른 문자를 입력 받았을 때, 오류 

                    break

                except:
                    print("Wrong input!")               #스페이스 또는 숫자 외 다른 문자를 입력 받았을 때, 오류 
            
            if reroll_indices in ["Q", "q"]:                   #게임 중단
                break

            print("")
            dice_set = sorted(dice_set)         #주사위 정렬
            print(f"Sorted Roll: {dice_set}")
            
            while True:
                player_choice = input("Choose a category: ")
                if player_choice in ["Q", "q"]:                                                #게임 중단
                    print("")
                    save_file = input("Game paused. Enter the filename to save:\n")     #저장할 파일 이름 입력
                    break

                elif player_choice in ['1', '2', '3', '4', '5', '6', 'C', 'c', '4k', '4K', 'fh', 'fH', 'Fh', 'FH', 'ss','Ss', 'sS', 'SS', 'ls', 'Ls', 'lS', 'LS', 'y', 'Y']:    #player가 sel을 올바르게 선택했을 때
                    break

                else:                           #player가 sel을 올바르지 않게 선택했을 때
                    print("Wrong Input!")
                    continue

            if player_choice in ["Q", "q"] or reroll_indices in ["Q", "q"]:                       #게임 중단
                break

            score_list = calc_score(dice_set, player_choice, score_list, 1)         #점수판에 점수 입력
            
            print("")
            print_score_board(score_list)       #점수판 출력

            player_turn += 1                    #턴 추가

            dice_set = roll_dice()              #컴퓨터 차례 및 첫 번째 주사위 굴리기
            print("\n[Computer's Turn (%d/12)]" %(computer_turn))     #컴퓨터 턴 출력
            print(f"Roll: {dice_set}")              #1번째 주사위 출력

            sel, reroll_indices = computer_pattern(dice_set, score_list)        #컴퓨터의 선택

            print(f"Which dice to reroll (1~5)?", end = ' ')                    #컴퓨터의 다시 굴릴 주사위 출력
            for i in reroll_indices:
                print(f"{i}", end = ' ')
            print("")

            while True:
                if reroll_indices == []:                #다시 굴릴 주사위가 없는 경우
                    break

                dice_set = roll_dice(dice_set, reroll_indices)
                print(f"Roll: {dice_set}")              #2번째 주사위 출력
                sel, reroll_indices = computer_pattern(dice_set, score_list)    #컴퓨터의 선택
                print(f"Which dice to reroll (1~5)?", end = ' ')                #컴퓨터의 다시 굴릴 주사위 출력
                for i in reroll_indices:
                    print(f"{i}", end = ' ')
                print("")

                if reroll_indices == []:                #다시 굴릴 주사위가 없는 경우
                    break

                dice_set = roll_dice(dice_set, reroll_indices)      
                print(f"Roll: {dice_set}")                                          #3번째 주사위 출력
                sel, reroll_indices = computer_pattern(dice_set, score_list)        #컴퓨터의 선택

                break

            dice_set = sorted(dice_set)             #주사위 정렬
            print("")
            print(f"Sorted Roll: {dice_set}")       #정렬된 주사위 출력
            print(f"Choose a category: {sel}")      #컴퓨터의 선택 출력
            print("")
            
            score_list = calc_score(dice_set, sel, score_list, 2)       #점수판의 컴퓨터의 점수 입력

            computer_turn += 1                              #턴 추가

            if player_turn == 13 and computer_turn == 13:   #게임이 끝났을 때
                break
        
        if player_choice in ['Q', 'q'] or reroll_indices in ['Q', 'q']:   #게임 중단
            outfile = open(save_file, "w")                  #파일 쓰기 모드로 열기
            
            for score in score_list:
                outfile.write("%s %s %s\n" %(score[0],score[1],score[2]))

            outfile.close()                                 #파일 닫기
            print("File saved.\n")
            continue
            

        print("<Final Score Board>")                        #최종 점수판 출력
        print_score_board(score_list)
        
        player_score = 0                                    #플레이어 및 컴퓨터 점수 합산
        computer_score = 0
        sub_total1 = 0
        sub_total2 = 0
        for i in range(0, 12):
            player_score += int(score_list[i][1])
            computer_score += int(score_list[i][2])
        for i in range(0, 6):
            sub_total1 += int(score_list[i][1])
            sub_total2 += int(score_list[i][2])
        
        if sub_total1 >= 63:
            player_score += 35
        if sub_total2 >= 63:
            computer_score += 35
            

        if player_score > computer_score:                   #플레이어 승리
            print("You win!")
        elif player_score == computer_score:                #무승부
            print("Draw")
        else:                                               #컴퓨터 승리
            print("You lose!")

        print("")
        restart = input("Press Enter to continue...")       #엔터키 입력시 초기화면으로 돌아가기
        if restart == "":
            print("")
            continue

    
    else:                 #프로그램 종료
        print("Program ended, Bye!")
        break
