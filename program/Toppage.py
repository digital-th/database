import tkinter as tk

class ToppageFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='green', width=1000, height=1000)
        tk.Message(self, text="歴史年号クイズ", font=("HG丸ｺﾞｼｯｸM-PRO",24), fg="black", bg="white", width=500, padx=200, pady=60, relief="raised").place(x=120, y=50)
        tk.Message(self, text="あああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ", font=("HG丸ｺﾞｼｯｸM-PRO",18), fg="black", bg="white", width=550, padx=30, pady=60, relief="raised").place(x=95, y=250)

    def start(self):
        return    