import random

class Panel:
    def __init__(self):             #패널 초기화
        self.isRevealed = False    
        self.hasFlag = False

    def toggleFlag(self):           #깃발을 토글한다.
        if self.hasFlag == True:
            self.hasFlag = False
        elif self.hasFlag == False:
            self.hasFlag = True

    def unveil(self):               #해당 panel을 밝혀진 상태로 변경
        self.isRevealed = True

class EmptyPanel(Panel):
    numOfNearMines = 0              # 해당 panel과 인접한 mine의 수를 저장하는 num type 변수

    def addNumOfNearMines(self):    #주변 지뢰 개수를 1 증가시킨다.
        self.numOfNearMines += 1

    def unveil(self):               #해당 panel을 밝혀진 상태로 변경
        super().unveil()
        return self.numOfNearMines  #인접한 mine의 수 return

class MinePanel(Panel): 
    def unveil(self):               #해당 panel을 밝혀진 상태로 변경
        super().unveil()
        return -1                   #-1 return

class Board:

    panels = 0                      #변수 생성

    def reset(self, numMine, height, width):
        self.panels = [[0 for j in range(width)] for i in range(height)]             #panels를 2차원 리스트로 초기화
        for i in range(numMine):
            while True:
                row = random.randint(0, height-1) 
                col = random.randint(0, width-1)
                if isinstance(self.panels[row][col], MinePanel) == False:       #중복 확인
                    break
            self.panels[row][col] = MinePanel()  #중복 없이 numMine개의 지뢰를 랜덤하게 배치

        for j in range(len(self.panels)):
            for i in range(len(self.panels[j])):
                if not self.checkMine(j, i):                                    #지뢰가 아닐 경우
                    self.panels[j][i] = EmptyPanel()                            #EmptyPanel로 추가
                    for k in range(0, self.getNumOfNearMines(j, i)):            #주변 지뢰 수 확인
                        self.panels[j][i].addNumOfNearMines()

    def getNumOfRevealedPanels(self):   #오픈된 패널의 개수를 반환한다.
        count = 0
        for j in range(len(self.panels)):
            for i in range(len(self.panels[j])):
                if self.panels[j][i].isRevealed == True:
                    count += 1
        return count

    def unveil(self, y, x):
        if self.checkMine(y, x):        #지뢰일 경우
            return -1
        
        else:
            self.panels[y][x].isRevealed = True

        if self.checkFlag(y, x):        #깃발이 있을 때
            self.toggleFlag(y, x)

        if self.panels[y][x].unveil() == 0:     #주변 지뢰 수가 0일 때
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if 0 <= y+j < len(self.panels) and 0 <= x+i < len(self.panels[y]) and not self.checkReveal(y+j, x+i):
                        self.unveil(y+j, x+i)

        

    def toggleFlag(self, y, x):         #y, x 위치의 패널의 깃발을 토글한다.
        if self.panels[y][x].hasFlag == True:
            self.panels[y][x].hasFlag = False
        elif self.panels[y][x].hasFlag == False:
            self.panels[y][x].hasFlag = True

    def checkReveal(self, y, x):        #y, x 위치의 패널이 오픈되었는지 확인한다.
        if self.panels[y][x].isRevealed == True:
            return True
        elif self.panels[y][x].isRevealed == False:
            return False

    def checkFlag(self, y, x):          #y, x 위치의 패널에 깃발이 꽂혀있는지 확인한다.
        if self.panels[y][x].hasFlag == True:
            return True
        elif self.panels[y][x].hasFlag == False:
            return False

    def checkMine(self, y, x):          #y, x 위치의 패널이 지뢰인지 확인한다.
        return isinstance(self.panels[y][x], MinePanel)

    def getNumOfNearMines(self, y, x):  #y, x 위치의 패널의 주변 지뢰 개수를 반환한다.
        count = 0
        if y == 0:                          #y행 좌측 측면
            if x == 0:                      #x열 상단 측면
                for j in range(0, 2):       
                    for i in range(0, 2):
                        if self.checkMine(y+j, x+i):
                            count += 1

            elif x == len(self.panels[y]) - 1:  #x열 하단 측면
                for j in range(0, 2):
                    for i in range(-1, 1):
                        if self.checkMine(y+j, x+i):
                            count += 1

            else:                               #일반적인 경우
                for j in range(0, 2):
                    for i in range(-1, 2):
                        if self.checkMine(y+j, x+i):
                            count += 1

            
        elif y == len(self.panels) - 1:         #y행 하단 측면
            if x == 0:                          #x열 좌측 측면
                for j in range(-1, 1):
                    for i in range(0, 2):
                        if self.checkMine(y+j, x+i):
                            count += 1

            elif x == len(self.panels[y]) - 1:  #x열 우측 측면
                for j in range(-1, 1):
                    for i in range(-1, 1):
                        if self.checkMine(y+j, x+i):
                            count += 1

            else:                               #일반적인 경우
                for j in range(-1, 1):
                    for i in range(-1, 2):
                        if self.checkMine(y+j, x+i):
                            count += 1

        elif x == 0 and y not in [0, len(self.panels)- 1]:      #x열 우측 측면
            for j in range(-1, 2):
                    for i in range(0, 2):
                        if self.checkMine(y+j, x+i):
                            count += 1

        elif x == len(self.panels[y]) - 1 and y not in [0, len(self.panels)- 1]:        #x열 좌측 측면
            for j in range(-1, 2):
                    for i in range(-1, 1):
                        if self.checkMine(y+j, x+i):
                            count += 1

        else:                               #일반적인 경우
            for j in range(0, 3):
                for i in range(0, 3):
                    if self.checkMine(y+j-1, x+i-1):
                        count += 1
        return count