import tkinter as tk
import sqlite3
import datetime
import tkinter.messagebox as mb
import random

class QuizFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bg='orange', width=1000, height=1000)
        self.app = app
        self.problemCount = self.getProblemCount()
        self.n, self.answer, self.count, self.idx = self.reset()
        self.buttons = []
        self.make_button()
        self.questionNumber = 1
        self.question = tk.Message(self, text="", font=("HG丸ｺﾞｼｯｸM-PRO",24), fg="black", bg="white", width=500, padx=100, pady=100, relief="raised")
        self.question.place(x=50, y=100)

    def getProblemCount(self):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        sql = '''
            select count(*) from 問題;
            '''
        connection.execute(sql)
        result = connection.fetchall()
        return result[0][0]

    def reset(self):
        return 1, "", 0, random.randint(1, self.problemCount)

    def make_button(self):
        for i in range(4):
            self.make_quiz_button("", i)   
                
    def make_quiz_button(self, text, i):
        def write(event):
            connection = sqlite3.connect("question.db")
            sql = '''
            insert into 回答履歴 (問題番号, 回答, 日付) values (?, ?, ?);
            '''
            connection.execute(sql, ((self.questionNumber, event.widget["text"], datetime.date.today())),)
            connection.commit()

        def next(event):
            if self.n < 5:
                self.n = self.n+1
                self.idx = random.randint(1, self.problemCount)
                self.start()
            else:
                self.end()

        def isCollect(event):
            if event.widget["text"] == self.answer:
                self.count = self.count+1

        button = tk.Button(self, text=text, width=10, height=10, font=("", 20))
        button.place(x=200*i+15, y=500)
        button.bind("<Button-1>", write)
        button.bind("<Button-1>", isCollect, "+")
        button.bind("<Button-1>", next, "+")
        self.buttons.append(button)

    def start(self):
        self.questionNumber = self.getQuestionNumber(self.idx)
        question = self.getQuestion(self.idx)
        choices = self.getChoices(self.idx).split(",")
        self.answer = self.getAnswer(self.idx)
        n = list(range(len(choices)))
        random.shuffle(n)
        for i, e in enumerate(self.buttons):
            e["text"] = choices[n[i]]
        self.question["text"] = question

    def end(self):
        return_YN = mb.askyesno("fin", str(self.count)+"問正解です．もう一度やりますか?")
        self.n, self.answer, self.count, self.idx = self.reset()
        if return_YN == False:
            self.app.change_frame(self.app.frame1)
        elif return_YN == True:
            self.start()

    def getQuestionNumber(self, idx):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        sql = '''
        select 問題番号 from 問題 where 問題番号 = ?;
        '''
        connection.execute(sql, [idx])
        result = connection.fetchall()
        return result[0][0]

    def getQuestion(self, idx):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        sql = '''
        select 問題文 from 問題 where 問題番号 = ?;
        '''
        connection.execute(sql, [idx])
        result = connection.fetchall()
        return result[0][0]

    def getAnswer(self, idx):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        sql = '''
        select 正答 from 問題 where 問題番号 = ?;
        '''
        connection.execute(sql, [idx])
        result = connection.fetchall()
        return result[0][0]

    def getChoices(self, idx):
        conn = sqlite3.connect("question.db")
        connection = conn.cursor()
        sql = '''
        select 選択肢 from 問題 where 問題番号 = ?;
        '''
        connection.execute(sql, [idx])
        result = connection.fetchall()
        return ','.join(result[0])

