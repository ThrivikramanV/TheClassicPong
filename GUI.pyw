from tkinter import *
from os import system

class player_window():

    def __init__(self,master):
        self.master=master
        self.title_frame=Frame(self.master,bg='#19647e')
        self.text = Label(self.title_frame,text='PING PONG',bg='#19647e',fg='#ffc857',font=('Calibri',30,'bold'))
        self.text.pack()
        self.title_frame.pack(fill=BOTH)
        self.main_frame=Frame(self.master,bg='#071e3d')
        self.single_button=Button(self.main_frame,text='SINGLE PLAYER',command=self.single_func,width=15,font=('Calibri',20,'bold'),bg='#c1224f',fg='#efe6dd')
        self.two_button=Button(self.main_frame,text='TWO PLAYERS',command=self.two_func,width=15,font=('Calibri',20,'bold'),bg='#fff78f',fg='#2c302e')
        self.single_button.place(x=100,y=50)
        self.two_button.place(x=100,y=150)
        self.main_frame.pack(fill=BOTH,expand=1)

    def single_func(self):
        self.main_frame.destroy()
        self.title_frame.destroy()
        levels=level_window(self.master)

    def two_func(self):
        self.main_frame.destroy()
        self.title_frame.destroy()
        self.master.geometry('600x500')
        instruc_two=instruc_two_window(self.master)
                                                            
class level_window():
    
    def __init__(self,master):
        self.master=master
        self.main_frame=Frame(self.master,bg='#071e3d')
        self.easy_button=Button(self.main_frame,text='EASY',command=self.easy_func,width=7,font=('Calibri',20,'bold'),bg='red',fg='white')
        self.medium_button=Button(self.main_frame,text='MEDIUM',command=self.medium_func,width=7,font=('Calibri',20,'bold'),bg='#ce1616',fg='white')
        self.hard_button=Button(self.main_frame,text='HARD',command=self.hard_func,width=7,font=('Calibri',20,'bold'),bg='#a02020',fg='white')
        self.back_button = Button(self.main_frame, text = "BACK", command = self.back,width=5,font=('Calibri',15),bg='#ffdd00')
        self.easy_button.place(x=140,y=60)
        self.medium_button.place(x=140,y=130)
        self.hard_button.place(x=140,y=200)
        self.back_button.place(x=2,y=2)
        self.main_frame.pack(fill=BOTH,expand=1)
        
    def easy_func(self):
        level='easy'
        self.main_frame.destroy()
        self.master.geometry('600x500')
        instruc_single=instruc_single_window(level,self.master)
        
    def medium_func(self):
        level='medium'
        self.main_frame.destroy()
        self.master.geometry('600x500')
        instruc_single=instruc_single_window(level,self.master)
        
    def hard_func(self):
        level='hard'
        self.main_frame.destroy()
        self.master.geometry('600x500')
        instruc_single=instruc_single_window(level,self.master)

    def back(self):
        self.main_frame.destroy()
        players=player_window(self.master)

longtext2='Left Player: W and S keys\nRight Player: UP and DOWN arrow keys\nPress Ctrl to pause\nPress Enter to start'

class instruc_two_window(Frame):

    def __init__(self,master):
        self.master=master
        Frame.__init__(self,self.master,bg='red')
        self.pack(fill=BOTH, expand=1)
        self.back_button = Button(self, text = "BACK", command = self.back,width=5,font=('Calibri',14),bg='#ffdd00')
        self.back_button.place(x=2, y=2)
        self.text2 = Label(self,text='Fastest to 3 Wins!',pady=100,bg='red',fg='blue',font=('Calibri',30,'italic'))
        self.text2.pack()
        self.text = Label(self,text=longtext2,bg='red',fg='white',font=('Times',20,'bold'))
        self.text.pack()
        self.master.bind('<Return>',self.start_game)
                       
    def back(self):
        self.destroy()
        self.master.geometry('400x300')
        players=player_window(self.master)

    def start_game(self,event):
        self.master.destroy()
        system('python pingpong.pyw twoplayer')
        
longtext='Use the W/S or UP/DOWN arrow keys\nPress Ctrl to pause\nPress Enter to start'
        
class instruc_single_window(Frame):

    def __init__(self,level,master):
        self.level=level
        self.master=master
        Frame.__init__(self,self.master,bg='red')
        self.pack(fill=BOTH, expand=1)
        self.back_button = Button(self, text = "BACK", command = self.back,width=5,font=('Calibri',15),bg='#ffdd00')
        self.back_button.place(x=2, y=2)
        self.text2 = Label(self,text='Fastest to 3 Wins!',pady=100,bg='red',fg='blue',font=('Calibri',30,'italic'))
        self.text2.pack()
        self.text = Label(self,text=longtext,bg='red',fg='white',font=('Times',20,'bold'))
        self.text.pack()
        self.master.bind('<Return>',self.start_game)

    def back(self):
        self.destroy()
        self.master.geometry('400x300')
        levels=level_window(self.master)        

    def start_game(self,event):
        self.master.destroy()
        system(f'python pingpong.pyw {self.level}')
        
root=Tk()
root.geometry('400x300')
root.title('PING PONG')
root.resizable(False,False)
players=player_window(root)
root.mainloop()
