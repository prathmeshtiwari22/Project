from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox

root =Tk()
root.title("Reminder Gui")
root.geometry("550x330")

mixer.init()


def th():
    t1=threading.Thread(target=alarm,args=())
    t1.start()


def alarm():
    a=altime.get()

    if a=='':
        msg=messagebox.showerror('Invalid data','Please enter valid time')

    else:
        AlarmT=a
        Currenttime=time.strftime('%H:%M')
        while AlarmT !=Currenttime:
            Currenttime =time.strftime('%H:%M')

        if AlarmT == Currenttime:
            mixer.music.load('tone1.mp3')
            mixer.music.play()
            msg= messagebox.showinfo('Info',f'{msginput.get()}')
            if msg =='ok':
                mixer.music.stop()
                i=0
                with open("records.txt","a") as f:

                    if i>=0:
                        i=i+1
                        f.write(f" Record:{i} Time: {altime.get()} And Message: {msginput.get()} \n")






head=Label(root,text='Notification Reminder',font=('comic sans',20))
head.grid(row=0,columnspan=3,padx=10)


Clocking=PhotoImage(file='al.png')
img=Label(root,image=Clocking)
img.grid(rowspan=4,column=0)

input=Label(root,text='Input time',font=('comic sans',15))
input.grid(row=1,column=1)

altime=Entry(root,font=('comic sans',18),width=6)
altime.grid(row=1,column=2)

msg =Label(root,text='Message',font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput=Entry(root,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

submit =Button(root,text='Submit',font=('comic sans',18),command=th)
submit.grid(row=4,column=1,columnspan=2)


root.mainloop()