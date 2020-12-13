#Preparation
#Please introduce [pip install Pillow]

import tkinter as tk
from tkinter import messagebox
import time
import glob
import random
import os
from PIL import Image

counter = 0
counter_all = 0

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid(row=0,column=0)
  
        self.master.geometry("900x900")
        self.master.title("quiz")

        self.create_widgets()
    
    def create_widgets(self):
        
        self.main_frame = tk.Frame()
        
        
        self.main_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.main_frame.titleLabel = tk.Label(self.main_frame,text="Main Page",font=('Heevetica','90'))
        
        self.main_frame.titleLabel.grid(row=0,column=0,pady=180,padx=180)
        

        self.main_frame.changePageButton = tk.Button(self.main_frame,text="Start",font=("",50), \
            command=lambda : [self.quiz(),self.main_frame_destroy()])
            

        self.main_frame.changePageButton.grid(row=1,column=0)

    def main_frame_destroy(self):

        self.main_frame.destroy()
    
    def next_picture(self):

        self.frame1.destroy()
        self.quiz()
    
    def frame2_to_home(self):
        self.frame2.destroy()
        self.create_widgets()

    #frame1
    def quiz(self):

        global counter_all
        counter_all = counter_all + 1

        self.frame1 = tk.Frame()
        self.frame1.grid(row=0,column=0,sticky="nsew")

        self.choice_picture()
        self.haruka = tk.PhotoImage(file=self.set_picture)

        self.frame1.canvas = tk.Canvas(self.frame1,width=self.img.width,height=self.img.height,bg="white")
        self.frame1.canvas.grid(row=0,column=0)

        self.frame1.canvas.create_image(0,0,image=self.haruka,anchor=tk.NW)
        
        
        
        self.tokei = tk.Label(self.frame1,text="",font=('Helvetica',48),fg='red')
        self.tokei.grid(row=1,column=0)

        self.num()

        self.started = True
        self.count()

        self.txt = tk.Text(self.frame1,width=20,height=1,font=('',30))
        self.txt.focus_set()
        self.txt.grid(row=2,column=0)
        
        
        self.btn_ans = tk.Button(self.frame1,height=1,width=10,text="Submit",command=lambda : self.examine())
        
        self.btn_ans.grid(row=3,column=0)

        self.btn_exit = tk.Button(self.frame1,height=1,width=10,text="Quit",command=lambda : self.exit_window())

        self.btn_exit.grid(row=3,column=1)
    
    
    def examine(self):

        global counter
        result = self.txt.get(1.0,tk.END+"-1c")
        
        if self.answer == result:
            self.started = False
            messagebox.showinfo('Correct Answer','Excellent')
            counter = counter + 1
            self.next_picture()
        elif self.answer != result:
            self.started = False
            messagebox.showinfo('Incorrect Answer','Sorry, try again')
            self.next_picture()
    
    def choice_picture(self):
        #Please Input your Pictures Directory
        picture = [r.split('/')[-1] for r in glob.glob(r'C:\Users\yamab\OneDrive\デスクトップ\pictures\*png')]

        self.set_picture = random.choice(picture)

        #Picture name is correct answer
        #ex. Horse.png → [Horse] is answer
        self.answer = os.path.splitext(os.path.basename(self.set_picture))[0]
        self.img = Image.open(self.set_picture)

    def num(self):
        self.finish = time.time() + 12


    def count(self):
        
        if self.started:
            t = self.finish - time.time()

            if t<0:
                self.tokei.config(text="Time Over")
                self.next_picture()
            else:
                self.tokei.config(text='%02d'%(t%60))
                self.after(100,self.count)
    
    #exit menu
    def exit_window(self):

        global counter_all
        global counter

        self.started = False

        self.frame1.destroy()

        self.frame2 = tk.Frame()
        self.frame2.grid(row=0,column=0,sticky="nsew")

        percentage = '{:.1%}'.format(float(counter)/counter_all)
        txt1 = "Validity : " + str(counter) + "/" + str(counter_all) + " " + percentage
        self.frame2.titleLabel = tk.Label(self.frame2,text=txt1,font=('Heevetica','70'))
        
        self.frame2.titleLabel.grid(row=0,column=0,pady=160,padx=180)

        self.frame2.btn_gobackto_home = tk.Button(self.frame2,height=1,width=10,text="home menu",command=lambda : self.frame2_to_home())
        self.frame2.btn_gobackto_home.grid(row=1,column=0)

        #Initialize
        counter_all = 0
        counter = 0

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
    
