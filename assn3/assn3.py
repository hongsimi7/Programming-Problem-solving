import random

class Posmon:       #포스몬 클래스
    def __init__(self, health, max_health, attack, defence, moves, name):
        self.health = health            # 포스몬의 체력 (int)
        self.max_health = max_health    # 포스몬의 최대(초기) 체력 (int)
        self.attack = attack            # 포스몬의 공격력 (int)
        self.defence = defence          # 포스몬의 방어력 (int)
        self.moves = moves              # 포스몬이 보유한 기술(Move) 리스트 (list of Move)
        self.name = name                # 포스몬의 이름(str)

    def get_name(self):              # 포스몬의 이름을 반환하는 메서드
        return self.name
    
    def get_max_health(self):        #포스몬의 최대 체력을 반환하는 메서드
        return self.max_health

    def get_type(self):              #포스몬 타입 / 오버라이딩으로 구현
        pass

    def reset_status(self, reset_health = False):
        if self.name == "Ponix":
            self.attack = 20
            self.defence = 23
        elif self.name == "Normie":
            self.attack = 20
            self.defence = 20
        elif self.name == "Rocky":
            self.attack = 15
            self.defence = 25
        else:
            self.attack = 30
            self.defence = 10

        if reset_health == True:
            self.health = self.max_health

class Ponix(Posmon):        #Ponix 정의

    def __init__(self):
        super().__init__(86, 86, 20, 23,["Tackle", "Growl", "SwordDance"], "Ponix")

    def get_type(self):
        return "Paper"
    
class Normie(Posmon):       #Normie 정의
    def __init__(self):
        super().__init__(80, 80, 20, 20,["Tackle", "Swift", "TailWhip"], "Normie")

    def get_type(self):
        return "Nothing"
    
class Rocky(Posmon):       #Rocky 정의
    def __init__(self):
        super().__init__(80, 80, 15, 25,["Tackle", "Growl"], "Rocky")

    def get_type(self):
        return "Rock"
    
class Swania(Posmon):       #Swania 정의
    def __init__(self):
        super().__init__(80, 80, 30, 10,["ScissorsCross", "SwordDance"], "Swania")

    def get_type(self):
        return "Scissors"
    
class Move:                     #포스몬 기술 클래스
    def __init__(self, name): 
        self.name = name # 기술 이름(str)
     
    def get_name(self): # 기술의 이름을 반환하는 메서드
        return self.name

    def get_speed(self):       # 기술의 속도를 반환하는 메서드 / 오버라이딩으로 구현
        pass

    def use(self, our_posmon, opponent_posmon, is_player_move=True):       # 기술을 사용하는 메서드 / 오버라이딩으로 구현    
        pass

class PhysicalMove(Move):       #공격 기술 클래스
    def __init__(self, power, name): 
        super().__init__(name)
        self.power = power      # 해당 기술의 위력

    def get_power(self):        # 이 기술의 위력을 반환하는 메서드
        return self.power

    def use(self, our_posmon, opponent_posmon, is_player_move=True):
        if our_posmon.get_type() == "Paper" and opponent_posmon.get_type() == "Rock":                       #위력이 2배되는 경우
            damage = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * 2
        elif our_posmon.get_type() == "Rock" and opponent_posmon.get_type() == "Scissors":
            damage = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * 2
        elif our_posmon.get_type() == "Scissors" and opponent_posmon.get_type() == "Paper":
            damage = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * 2
        else:                                                                                               #일반적인 경우
            damage = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * 1

        opponent_posmon.health = opponent_posmon.health - damage

        if is_player_move == True:          #플레이어가 기술 발동
            print("- %s 포스몬의 [체력] %d 감소 (%d -> %d)" %("컴퓨터", damage, opponent_posmon.health + damage, opponent_posmon.health))
        else:                               #컴퓨터가 기술 발동
            print("- %s 포스몬의 [체력] %d 감소 (%d -> %d)" %("당신", damage, opponent_posmon.health + damage, opponent_posmon.health))

        if opponent_posmon.health < 0:
            opponent_posmon.health = 0

class Tackle(PhysicalMove):
    def __init__(self):     #메서드
        super().__init__(power=25, name="Tackle")

    def get_speed(self):
        return 0
        
class ScissorsCross(PhysicalMove):
    def __init__(self):     #메서드
        super().__init__(power=30, name="ScissorsCross")

    def get_speed(self):
        return 0
    
class Swift(PhysicalMove):
    def __init__(self):     #메서드
        super().__init__(power=0, name="Swift")

    def get_speed(self):
        return 3
    
class StatusMove(Move):     #변화 기술 클래스
    pass

class Growl(StatusMove):
    def __init__(self, name = "Growl"): # Growl 기술의 인스턴스 초기화
        super().__init__(name)
        self.amount = -5 

    def get_speed(self):             # Growl 기술의 속도를 반환하는 메서드
        return 1

    def use(self, our_posmon, opponent_posmon, is_player_move = True):
        
        if opponent_posmon.attack < 5:              #기술 발동 시 공격력이 음수가 될 때
            effect = opponent_posmon.attack
            opponent_posmon.attack = 0
        
            if is_player_move == True:              #플레이어가 기술 발동
                print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %("컴퓨터", effect, effect, opponent_posmon.attack))

            else:                                   #컴퓨터가 기술 발동
                print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %("당신", effect, effect, opponent_posmon.attack))

        else:                                       #일반적인 경우
            opponent_posmon.attack = opponent_posmon.attack + self.amount
        
            if is_player_move == True:              #플레이어가 기술 발동
                print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %("컴퓨터", -(self.amount), opponent_posmon.attack - self.amount, opponent_posmon.attack))

            else:                                   #컴퓨터가 기술 발동
                print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %("당신", -(self.amount), opponent_posmon.attack - self.amount, opponent_posmon.attack))

class SwordDance(StatusMove):
    def __init__(self, name = "SwordDance"): # SwordDance 기술의 인스턴스 초기화
        super().__init__(name)
        self.amount = 10 

    def get_speed(self):             # SwordDance 기술의 속도를 반환하는 메서드
        return 0

    def use(self, our_posmon, opponent_posmon, is_player_move = True):
        our_posmon.attack = our_posmon.attack + self.amount
        
        if is_player_move == True:              #플레이어가 기술 발동
            print("- %s 포스몬의 [공격력] %d 증가 (%d -> %d)" %("당신", self.amount, our_posmon.attack - self.amount, our_posmon.attack))

        else:                                   #컴퓨터가 기술 발동
            print("- %s 포스몬의 [공격력] %d 증가 (%d -> %d)" %("컴퓨터", self.amount, our_posmon.attack - self.amount, our_posmon.attack))

class TailWhip(StatusMove):
    def __init__(self, name = "TailWhip"): # TailWhip 기술의 인스턴스 초기화
        super().__init__(name)
        self.amount = -5 

    def get_speed(self):             # TailWhip 기술의 속도를 반환하는 메서드
        return 1

    def use(self, our_posmon, opponent_posmon, is_player_move = True):
        if opponent_posmon.defence < 5:             #기술 사용 시 방어력이 음수가 될 때
            effect = opponent_posmon.defence
            opponent_posmon.defence = 0
            if is_player_move == True:              #플레이어가 기술 발동
                print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %("컴퓨터", effect, effect, opponent_posmon.defence))

            else:                                   #컴퓨터가 기술 발동
                print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %("당신", effect, effect, opponent_posmon.defence))

        else:                                       #일반적인 경우
            opponent_posmon.defence = opponent_posmon.defence + self.amount
            
            if is_player_move == True:              #플레이어가 기술 발동
                print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %("컴퓨터", -self.amount, opponent_posmon.defence - self.amount, opponent_posmon.defence))

            else:                                   #컴퓨터가 기술 발동
                print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %("당신", -self.amount, opponent_posmon.defence - self.amount, opponent_posmon.defence))

def choose_posmon(posmon_list):                             #플레이어의 포스몬 고르기
    if len(posmon_list) == 0:
        print("\n============================================")
        print(f"당신이 사용할 포스몬을 선택하세요. 현재 {len(posmon_list)} 마리/ 최대 3 마리")
        print("0. Ponix")
        print("1. Normie")
        print("2. Swania")
        print("3. Rocky")
        print("============================================")
        
        while True:                                    #포스몬 선택
            player_selection = input("입력: ")
            if player_selection in ['0', '1', '2', '3']:       #정상 입력
                break
            else:                                   #오류
                print("잘못된 입력입니다. 다시 입력하세요.")

        if player_selection == '0':
            p1_Poinx = Ponix()
            posmon_list.append(p1_Poinx)
        
        elif player_selection == '1':
            p1_Normie = Normie()
            posmon_list.append(p1_Normie)

        elif player_selection == '2':
            p1_Swania = Swania()
            posmon_list.append(p1_Swania)

        else:
            p1_Rocky = Rocky()
            posmon_list.append(p1_Rocky)

    elif len(posmon_list) == 1:
        print("\n============================================")
        print(f"당신이 사용할 포스몬을 선택하세요. 현재 {len(posmon_list)} 마리/ 최대 3 마리")
        print("0. Ponix")
        print("1. Normie")
        print("2. Swania")
        print("3. Rocky")
        print("-1. 그만두기")
        print("============================================")
        
        while True:                                        #포스몬 선택
            player_selection = input("입력: ")
            if player_selection in ['0', '1', '2', '3', '-1']:       #정상 입력
                break
            else:                                   #오류
                print("잘못된 입력입니다. 다시 입력하세요.")

        if player_selection == '0':
            p2_Poinx = Ponix()
            posmon_list.append(p2_Poinx)
        
        elif player_selection == '1':
            p2_Normie = Normie()
            posmon_list.append(p2_Normie)

        elif player_selection == '2':
            p2_Swania = Swania()
            posmon_list.append(p2_Swania)

        elif player_selection == '3':
            p2_Rocky = Rocky()
            posmon_list.append(p2_Rocky)
        
        else:
            return 1
        
    else:
        print("\n============================================")
        print(f"당신이 사용할 포스몬을 선택하세요. 현재 {len(posmon_list)} 마리/ 최대 3 마리")
        print("0. Ponix")
        print("1. Normie")
        print("2. Swania")
        print("3. Rocky")
        print("-1. 그만두기")
        print("============================================")
        
        while True:                                        #포스몬 선택
            player_selection = input("입력: ")
            if player_selection in ['0', '1', '2', '3', '-1']:       #정상 입력
                break
            else:                                   #오류
                print("잘못된 입력입니다. 다시 입력하세요.")

        if player_selection == '0':
            p3_Poinx = Ponix()
            posmon_list.append(p3_Poinx)
        
        elif player_selection == '1':
            p3_Normie = Normie()
            posmon_list.append(p3_Normie)

        elif player_selection == '2':
            p3_Swania = Swania()
            posmon_list.append(p3_Swania)

        elif player_selection == '3':
            p3_Rocky = Rocky()
            posmon_list.append(p3_Rocky)
        
        else:
            return 1
        
def com_posmon(com_posmon_list):                            #컴퓨터 포스몬 고르기
    posmon_list = ["Ponix", "Normie", "Swania", "Rocky"]          
    posmon = random.choice(posmon_list)                     #없앨 포스몬 하나 선택
    
    for i in range(len(com_posmon_list)):
        if posmon == com_posmon_list[i].get_name():
            com_posmon_list.pop(i)
            break
        

posmon_list = []
while True:                                                 #메인 함수
    print(" ____    ___    _____ ___ ___   ___   ____  ")
    print("|    \  /   \  / ___/|   T   T /   \ |    \ ")
    print("|   o )Y     Y(   \_ | _   _ |Y     Y|  _  Y")
    print("|   _/ |  O  | \__  T|  \_/  ||  O  ||  |  |")
    print("|  |   |     | /  \ ||   |   ||     ||  |  |")
    print("|  |   l     ! \    ||   |   |l     !|  |  |")
    print("l__j    \___/   \___jl___j___j \___/ l__j__j")
    print("============================================")
    print("0. 포스몬 선택")
    print("1. 배틀하기")
    print("2. 종료하기")
    print("============================================")
    
    while True:                                 #초기화면 선택
        player_selection = input("입력: ")
        if player_selection in ['0', '1', '2']:       #정상 입력
            break
        else:                                   #오류
            print("잘못된 입력입니다. 다시 입력하세요.")

    if player_selection == '0':       #포스몬 선택
        posmon_list = []
        
        count = 0
        while True:
            choice_posmon = choose_posmon(posmon_list)
            count += 1
            if choice_posmon == 1 or count == 3:      #그만두기를 받았을 때
                print("")
                break
        
        print("============================================")
        print("당신의 포스몬 목록: ", end = '')
        for posmon in posmon_list:    
            print(posmon.get_name(), end = ' ')
        print("\n============================================\n")

    
    elif player_selection == '1':    #배틀하기
        game_over = 0
        while True:
    
            if game_over in [1, 2]:                                         #게임이 끝났을 때
                break

            if posmon_list == []:                                           #포스몬을 선택하지 않은 경우
                print("\n싸울 포스몬이 없습니다! 먼저 포스몬을 선택해 주세요.\n")
                break

            com_Ponix = Ponix()
            com_Normie = Normie()
            com_Swania = Swania()
            com_Rocky = Rocky()
            com_posmon_list = [com_Ponix, com_Normie, com_Rocky, com_Swania]
            random.shuffle(com_posmon_list)                                 #컴퓨터 포스몬 순서 섞기
            com_posmon(com_posmon_list)                                     #컴퓨터 포스몬 고르기

            print("\n============================================")
            print("당신의 포스몬 목록:", end = '')
            for posmon in posmon_list:
                print(f" {posmon.get_name()}", end = '')
            print("")
            print("컴퓨터 포스몬 목록:", end = '')
            for posmon in com_posmon_list:
                print(f" {posmon.get_name()}", end = '')
            print("\n============================================\n")
            print("배틀이 시작됩니다.")
            p_posmon = 0
            c_posmon = 0


            while True:
                    p_posmon_count = len(posmon_list)
                    c_posmon_count = len(com_posmon_list)
                    
                    print("############################################")
                    print("컴퓨터 포스몬: [", end = '')
                    for i in range(len(com_posmon_list)):
                        if com_posmon_list[i].health == 0:                  #포스몬이 죽어있을 때
                            print("X", end ='')
                            c_posmon_count -= 1
                        else:                                               #포스몬이 살아있을 때
                            print("O", end = '')
                    print(f"] {c_posmon_count} / {len(com_posmon_list)}")
                    print(f"{com_posmon_list[c_posmon].name} <|{com_posmon_list[c_posmon].get_type()} {com_posmon_list[c_posmon].health} / {com_posmon_list[c_posmon].max_health}|")
                    print("                     VS                     ")
                    print(f"{posmon_list[p_posmon].name} <|{posmon_list[p_posmon].get_type()} {posmon_list[p_posmon].health} / {posmon_list[p_posmon].max_health}|")
                    print(f"당신의 포스몬: [", end = '')
                    for i in range(len(posmon_list)):
                        if posmon_list[i].health == 0:                      #포스몬이 죽어있을 때
                            print("X", end ='')
                            p_posmon_count -= 1
                        else:                                               #포스몬이 살아있을 때
                            print("O", end = '')
                    print(f"] {p_posmon_count} / {len(posmon_list)}")
                    print("++++++++++++++++++++++++++++++++++++++++++++")
                    print("기술: ", end = '')
                    count = 0
                    for move in posmon_list[p_posmon].moves:    
                        print(f"({count}) {move} ", end = '')
                        count += 1
                    print("")
                    print("############################################")

                    if game_over == 1:                                      #플레이어가 승리했을 때
                        print("\n[배틀 결과] 당신이 이겼습니다.\n")
                        posmon_list = []                                    #포스몬 초기화
                        com_posmon_list = []
                        break

                    if game_over == 2:                                      #컴퓨터가 승리했을 때
                        print("\n[배틀 결과] 컴퓨터가 이겼습니다.\n")
                        posmon_list = []                                    #포스몬 초기화
                        com_posmon_list = []
                        break

                    while True:                                 #플레이어 순서 명령어 선택
                        player_selection = input("입력: ")
                        player_selection_list = player_selection.split()


                        if player_selection_list[0] == 'e':                 #포스몬 확인
                            print("############################################")
                            count = 0
                            for posmon in posmon_list:                                
                                print(f"({count}) {posmon.name} <|{posmon.get_type()} {posmon.health} / {posmon.max_health}|")
                                count += 1
                            print("")
                            continue     

                        elif player_selection_list[0] == 'o':       #기술 사용
                            if int(player_selection_list[1]) in [x for x in range(0, len(posmon_list[p_posmon].moves))]:        #정상
                                print("############################################")
                                player_move = posmon_list[p_posmon].moves[int(player_selection_list[1])]
                                break
                                
                            else:                                                                                               #숫자가 벗어난 경우
                                print("선택할 수 없는 기술입니다!")
                                continue

                        elif player_selection_list[0] == 's':       #포스몬 교대
                            if int(player_selection_list[1]) in [x for x in range(0, len(posmon_list))]:
                                if posmon_list[int(player_selection_list[1])].health <= 0 or int(player_selection_list[1]) == p_posmon:     #쓰러진 포스몬 혹은 현재 포스몬일 경우
                                    print("포스몬을 교대시킬 수 없습니다!")
                                    continue
                                else:                                                                                                       #정상
                                    print("############################################")
                                    posmon_list[p_posmon].reset_status()
                                    p_posmon = int(player_selection_list[1])
                                    print(f"당신의 포스몬 {posmon_list[p_posmon].name}로 교대")
                                    player_move = 0
                                    break

                            else:                                                                                                           #숫자가 벗어난 경우
                                print("포스몬을 교대시킬 수 없습니다!")
                                continue
                            

                        else:                                                                                                               #잘못된 명령어
                            print(f"잘못된 명령어: {player_selection}")
                            continue
                            
                    if player_move == "Tackle":                                                                                             #플레이어 기술 클래스로 변환
                        player_move = Tackle()

                    elif player_move == "ScissorsCross":
                        player_move = ScissorsCross()

                    elif player_move == "Swift":
                        player_move = Swift()

                    elif player_move == "Growl":
                        player_move = Growl()

                    elif player_move == "SwordDance":
                        player_move = SwordDance()

                    elif player_move == "TailWhip":
                        player_move = TailWhip()
                        
                    else:
                        pass
                              

                    com_move = random.choice(com_posmon_list[c_posmon].moves)                                                               #컴퓨터의 기술 선택                    
                    if com_move == "Tackle":                                                                                                #컴퓨터 기술 클래스로 변환
                        com_move = Tackle()

                    elif com_move == "ScissorsCross":
                        com_move = ScissorsCross()

                    elif com_move == "Swift":
                        com_move = Swift()

                    elif com_move == "Growl":
                        com_move = Growl()

                    elif com_move == "SwordDance":
                        com_move = SwordDance()
                        
                    elif com_move == "TailWhip":
                        com_move = TailWhip()
                    
                    else:
                        pass

                    if type(player_move) == int:                                  #플레이어가 교대를 선택했을 때
                        print(f"컴퓨터 {com_posmon_list[c_posmon].name}: {com_move.name} 기술 사용")
                        com_move.use(com_posmon_list[c_posmon], posmon_list[p_posmon], False)
                        if posmon_list[p_posmon].health <= 0:                 #플레이어의 포스몬이 쓰러졌을 때
                                print(f"당신의 {posmon_list[p_posmon].name}: 쓰러짐")
                                live = False

                                for i in range(0, len(posmon_list)):              
                                    if posmon_list[i].health > 0:                   #플레이어의 포스몬이 남아있을 때
                                        p_posmon = i
                                        live = True
                                        break

                                if live == False:                                   #플레이어의 포스몬이 없을 때
                                    game_over = 2

                    elif player_move.get_speed() >= com_move.get_speed():         #플레이어의 기술 스피드가 더 빠를 때 혹은 동등할 때
                        print(f"당신의 {posmon_list[p_posmon].name}: {player_move.name} 기술 사용")
                        player_move.use(posmon_list[p_posmon], com_posmon_list[c_posmon])

                        if com_posmon_list[c_posmon].health <= 0:                 #컴퓨터 포스몬이 쓰러졌을 때
                            print(f"컴퓨터 {com_posmon_list[c_posmon].name}: 쓰러짐")
                            c_posmon += 1

                            if c_posmon < len(com_posmon_list):                   #컴퓨터의 포스몬이 남아있을 때
                                print(f"컴퓨터 {com_posmon_list[c_posmon].name}로 교대")

                            else:                                                 #컴퓨터의 포스몬이 없을 때
                                game_over = 1
                                c_posmon -= 1

                        else:                                                     #컴퓨터 포스몬이 살아있을 때
                            print(f"컴퓨터 {com_posmon_list[c_posmon].name}: {com_move.name} 기술 사용")
                            com_move.use(com_posmon_list[c_posmon], posmon_list[p_posmon], False)
                            
                            if posmon_list[p_posmon].health <= 0:                 #플레이어의 포스몬이 쓰러졌을 때
                                print(f"당신의 {posmon_list[p_posmon].name}: 쓰러짐")
                                live = False

                                for i in range(0, len(posmon_list)):              
                                    if posmon_list[i].health > 0:                   #플레이어의 포스몬이 남아있을 때
                                        p_posmon = i
                                        live = True
                                        break

                                if live == False:                                   #플레이어의 포스몬이 없을 때
                                    game_over = 2

                    else:                                                           #컴퓨터의 기술 스피드가 더 빠를 때
                        print(f"컴퓨터 {com_posmon_list[c_posmon].name}: {com_move.name} 기술 사용")
                        com_move.use(com_posmon_list[c_posmon], posmon_list[p_posmon], False)
                        if posmon_list[p_posmon].health <= 0:                 #플레이어의 포스몬이 쓰러졌을 때
                                print(f"당신의 {posmon_list[p_posmon].name}: 쓰러짐")
                                live = False

                                for i in range(0, len(posmon_list)):              
                                    if posmon_list[i].health > 0:                   #플레이어의 포스몬이 남아있을 때
                                        p_posmon = i
                                        live = True
                                        break

                                if live == False:                                   #플레이어의 포스몬이 없을 때
                                    game_over = 2

                        else:                                                       #플레이어의 포스몬이 살아있을 때
                            print(f"당신의 {posmon_list[p_posmon].name}: {player_move.name} 기술 사용")
                            player_move.use(posmon_list[p_posmon], com_posmon_list[c_posmon])
                            
                            if com_posmon_list[c_posmon].health <= 0:                 #컴퓨터 포스몬이 쓰러졌을 때
                                print(f"컴퓨터 {com_posmon_list[c_posmon].name}: 쓰러짐")
                                c_posmon += 1

                                if c_posmon < len(com_posmon_list):                   #컴퓨터의 포스몬이 남아있을 때
                                    print(f"컴퓨터 {com_posmon_list[c_posmon].name}로 교대")

                                else:                                                 #컴퓨터의 포스몬이 없을 때
                                    game_over = 1
                                    c_posmon -= 1
                                    
                    print("")



    else:                           #게임 종료
        break
