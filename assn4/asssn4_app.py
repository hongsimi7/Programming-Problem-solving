import tkinter as tk
from assn4_model import Board


TITLE = "Minesweeper"
BTN_WIDTH = 30
BTN_HEIGHT = 30
BORDER_SIZE = 2
OUTTER_PADDING_SIZE = 10
BACKGROUND_COLOR = "#DCDCDC"


class App(tk.Frame):
    def __init__(self, master, numMine, height, width):
        super(App, self).__init__(master)
        self.master = master
        master.title(TITLE)                                 #제목 설정
        self.board = Board()
        self.create_widgets(numMine, height, width)         #위젯 생성

    def create_widgets(self, numMine, height, width):       #위젯 생성 메서드
        self.board.reset(numMine, height, width)            #난이도에 맞춰 보드 생성
        
        self.master.geometry(f"{width * (BTN_WIDTH) + (OUTTER_PADDING_SIZE + BORDER_SIZE) * 2}x{(height + 1) * (BTN_HEIGHT) + (OUTTER_PADDING_SIZE + BORDER_SIZE) * 7}")    #창 크기 조정

        self.base_icon = tk.PhotoImage(file="imgs/smile.png")               #이미지 로드
        self.success_icon = tk.PhotoImage(file="imgs/sunglasses.png")
        self.fail_icon = tk.PhotoImage(file="imgs/skull.png")
        self.flag_icon = tk.PhotoImage(file="imgs/flag.png")
        self.bomb_icon = tk.PhotoImage(file="imgs/bomb.png")

        self["bg"] = BACKGROUND_COLOR           #창 크기 및 디자인 설정
        self["relief"] = tk.SUNKEN
        self["bd"] = BORDER_SIZE
        self["padx"] = OUTTER_PADDING_SIZE
        self["pady"] = OUTTER_PADDING_SIZE

        head = tk.Frame(self, bg=BACKGROUND_COLOR,relief=tk.SUNKEN, bd=BORDER_SIZE)     #head 설정
        head.grid(row=0, column=0, columnspan=width, pady=(0, OUTTER_PADDING_SIZE), sticky='ew')

        start_wrapper = tk.Frame(head, width=BTN_WIDTH, height=BTN_HEIGHT)              #초기화 버튼 설정
        start_wrapper.pack_propagate(0)
        start_wrapper.pack(padx=OUTTER_PADDING_SIZE, pady=OUTTER_PADDING_SIZE)
        start = tk.Button(start_wrapper, image=self.base_icon, bd=BORDER_SIZE)
        start.bind("<ButtonRelease-1>", lambda e: self.new_game(numMine, height, width))
        start.pack(expand=True, fill='both')

        body = tk.Frame(self, bg=BACKGROUND_COLOR, relief=tk.SUNKEN, bd=BORDER_SIZE)    #body 설정
        body.grid(row=1, column=0, columnspan=width)

        menubar = tk.Menu(self.master)                                                  #난이도 메뉴바 설정
        difficulty_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="난이도", menu=difficulty_menu)
        difficulty_menu.add_command(label="Easy", command=lambda: self.new_game(10, 10, 10))
        difficulty_menu.add_command(label="Normal", command=lambda: self.new_game(30, 15, 15))
        difficulty_menu.add_command(label="Hard", command=lambda: self.new_game(50, 20, 20))
        self.master.config(menu=menubar)


        def onLeftClick(y, x):          #버튼을 좌클릭했을 때
            btn = btn_list[y][x]
                       
            if self.board.checkReveal(y, x) or self.board.checkFlag(y, x):    #이미 밝혀진 칸인 경우 혹은 깃발이 꽂혀 있는 경우
                return
            
            is_bomb = self.board.unveil(y, x)               #해당 값 밝혀내기

            if is_bomb == -1:                               #게임을 패배했을 때

                for row in range(height):
                    for col in range(width):
                        btn = btn_list[row][col]
                        btn["image"] = ""                                           #이미지초기화
                        btn["state"] = tk.DISABLED
                        btn["relief"] = tk.SUNKEN
                        self.board.panels[row][col].isRevealed = True                    

                        if self.board.checkMine(row, col):                          #폭탄일 때
                            btn["background"] = BACKGROUND_COLOR
                            btn["image"] = self.bomb_icon
                            start["image"] = self.fail_icon               
                        
                        else:                                                       #폭탄이 아닐 때
                            if self.board.getNumOfNearMines(row, col) != 0:         #주위에 폭탄이 있을 때
                                btn["text"] = self.board.getNumOfNearMines(row, col)
                                btn["font"] = ("Arial", 15, "bold")


            elif self.board.getNumOfRevealedPanels() == height * width - numMine: #게임을 승리했을 때
                start["image"] = self.success_icon

                if self.board.getNumOfNearMines(y, x) != 0:                         #주위에 폭탄이 있을 때
                    btn["text"] = self.board.getNumOfNearMines(y, x)
                    btn["font"] = ("Arial", 15, "bold")
                    btn["state"] = tk.DISABLED
                    btn["relief"] = tk.SUNKEN

                else:                                                               #주위에 폭탄이 없을 때
                    btn["image"] = ""
                    btn["state"] = tk.DISABLED
                    btn["relief"] = tk.SUNKEN

                for row in range(height):
                    for col in range(width):
                        self.board.panels[row][col].isRevealed = True
            
            else:                                                                   #게임 진행
                for row in range(height):
                    for col in range(width):
                        btn = btn_list[row][col]
                        if self.board.checkReveal(row, col):
                                
                            btn["image"] = ""                                       #이미지 초기화
                            btn["state"] = tk.DISABLED
                            btn["relief"] = tk.SUNKEN

                            if self.board.getNumOfNearMines(row, col) != 0:         #주위에 폭탄이 있을 때
                                btn["text"] = self.board.getNumOfNearMines(row, col)
                                btn["font"] = ("Arial", 15, "bold")
        
            
        def onRightClick(y, x):         #버튼을 우클릭했을 때
            btn = btn_list[y][x]
            
            if self.board.checkReveal(y, x):    #이미 밝혀진 칸인 경우
                return
            
            self.board.toggleFlag(y, x)         #깃발을 토글함.

            if self.board.checkFlag(y, x):      #깃발을 꽂아야 하는 경우
                btn["image"] = self.flag_icon

            else:                               #깃발을 제거해야 하는 경우
                btn["image"] = ""
                
        
        btn_list = []                           #버튼 리스트 (2차원)
        for row in range(height):
            row_list_btn = []           
            for col in range(width):
                btn_wrapper = tk.Frame(body, width=BTN_WIDTH, height=BTN_HEIGHT)        #버튼 생성
                btn_wrapper.pack_propagate(0)
                btn_wrapper.grid(row=row, column=col)
                btn = tk.Button(btn_wrapper, bg=BACKGROUND_COLOR, bd=BORDER_SIZE)
                btn.bind("<Button-1>", lambda event, y=row, x=col: onLeftClick(y, x))   #버튼 좌클릭
                btn.bind("<Button-3>", lambda event, y=row, x=col: onRightClick(y, x))  #버튼 우클릭
                row_list_btn.append(btn)                 
                btn.pack(expand=True, fill='both')
            btn_list.append(row_list_btn)
        self.pack()

    def new_game(self, numMine, height, width):     #난이도 설정 및 게임 초기화 메서드 
       
        for widget in self.winfo_children():             # 현재 창의 위젯들을 제거하고 다시 초기화
            widget.destroy()
        
        self.create_widgets(numMine, height, width)     # 새로운 난이도에 맞게 위젯들을 다시 생성

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root, 10, 10, 10)
    app.mainloop()
