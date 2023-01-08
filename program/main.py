import tkinter as tk 

from QuizPage import QuizFrame
from Toppage import ToppageFrame
from HistoryPage import HistoryFrame

class App():
    def __init__(self, master):
        self.master = master
        self.master.title("歴史年号")
        self.master.geometry('800x800')
        self.master.resizable(width=False, height=False)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
    
        self.frame1 = ToppageFrame(self.master)
        self.frame1.grid(row=0, column=0, sticky=tk.NSEW)

        self.frame2 = QuizFrame(self.master, self)
        self.frame2.grid(row=0, column=0, sticky=tk.NSEW)
        
        self.frame3 = HistoryFrame(self.master)
        self.frame3.grid(row=0, column=0, sticky=tk.NSEW)
        
        startButton = tk.Button(self.frame1, text='スタート', width=40, height=5, command=lambda: self.change_frame(self.frame2))
        historyButton = tk.Button(self.frame1, text="履歴", command=lambda: self.change_frame(self.frame3))
        startButton.place(x=210, y=600)
        historyButton.place(x=720, y=10)

        toppageButton1 = tk.Button(self.frame2, text='トップページ', command=lambda: self.change_frame(self.frame1))
        toppageButton1.place(x=680, y=10)
    
        toppageButton2 = tk.Button(self.frame3, text='トップページ', command=lambda: self.change_frame(self.frame1))
        toppageButton2.place(x=680, y=10)

        self.frame1.tkraise()

    def change_frame(self, frame):
        frame.tkraise()
        frame.start()

if __name__ == "__main__":
    master = tk.Tk()
    app = App(master)
    app.master.mainloop()
