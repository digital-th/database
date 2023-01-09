import tkinter as tk
import sqlite3

class HistoryFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='green', width=1000, height=1000)
        tk.Message(self, text="履歴", font=("HG丸ｺﾞｼｯｸM-PRO",24), fg="black", bg="white", width=500, padx=350, pady=60, relief="raised").place(x=30, y=50)
        self.historys = []
        self.set()

        defaultButton = tk.Button(self, text='時間順', width=10, height=1, 
                                command=lambda: self.display('''
                                                             select 問題.問題番号, 問題.問題文, 回答履歴.日付 from 問題, 回答履歴 where 問題.問題番号 in (select 問題番号 from 回答履歴) and 問題.問題番号 = 回答履歴.問題番号 limit 5;
                                                             '''))
        defaultButton.place(x=50, y=210)

        mistakeButton = tk.Button(self, text='不正解数', width=10, height=1, 
                                command=lambda: self.display('''
                                                             select 問題.問題番号, 問題.問題文, 回答履歴.日付 from 問題, 回答履歴 where 問題.問題番号 in (select 問題番号 from 回答履歴) and 問題.問題番号 = 回答履歴.問題番号 and 問題.正答 = 回答履歴.回答 group by 問題.問題番号 order by count(*) desc limit 5;
                                                             '''))
        mistakeButton.place(x=200, y=210)

        correctButton = tk.Button(self, text='正解数', width=10, height=1, 
                                command=lambda: self.display('''
                                                             select 問題.問題番号, 問題.問題文, 回答履歴.日付 from 問題, 回答履歴 where 問題.問題番号 in (select 問題番号 from 回答履歴) and 問題.問題番号 = 回答履歴.問題番号 and not 問題.正答 = 回答履歴.回答 group by 問題.問題番号 order by count(*) desc limit 5;
                                                             '''))
        correctButton.place(x=350, y=210)  

    def set(self):
        for i in range(5):
            h = tk.Message(self, text="", font=("HG丸ｺﾞｼｯｸM-PRO",18), fg="black", bg="white", width=600, padx=40, relief="raised")
            h.place(x=30, y=270+i*60)
            self.historys.append(h)

    def start(self):
        self.display('''select 問題.問題番号, 問題.問題文, 回答履歴.日付 from 問題, 回答履歴 where 問題.問題番号 = 回答履歴.問題番号 limit 5;''')     

    def getHistorys(self, sql):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        connection.execute(sql)
        result = connection.fetchall()
        return result

    def display(self, sql):
        result = self.getHistorys(sql)
        for h, t in zip(self.historys, result):
            h["text"] = str(t[0])+"  "+t[1]+"  "+t[2]