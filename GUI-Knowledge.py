#ห้าม save ชื่อเดียวกับ library

from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #GUI=program หลัก
GUI.title('โปรแกรมบันทึกย้อมูล')
GUI.geometry('500x400') #ขนาด program ไม่เว้นวรรคระหว่าง x

#Button มาจาก * ที่เรา import * (from tkinter import *)
#ttk มาจาก module หนึ่งของ tkinter
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')

#ปุ่มอยู่ด้านบนตรงกลางหน้าจอเสมอ แม้ว่าจอขยาย
B1.pack(ipadx=20,ipady=20) #ipadx-ขนาดปุ่มในแนวแกน x จะบวกขึ้นไปอีก 20 pixel

#ปุ่มแบบเดิม ไม่มี theme
#B2 = Button(GUI,text='เงินมีอยู่กี่บาท')
#B2.pack()

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

#------------------
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
#showwarning
#showerror

FB1 = Frame(GUI) #คล้ายกระดาน
###FB1 = LabelFrame(GUI,text='Money')
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=20)
#B2.place(x=50,y=200)
#place ไม่สามารถขยายขนาดปุ่มได้ ต้องขยายขนาด frame
B2.pack(ipadx=20,ipady=20)
###B2.pack(ipadx=20,ipady=20,padx=30,pady=30)
#------------------


#------------------
def Button3():
    text = 'Python 101, math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)
#showwarning
#showerror

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

#------------------

#------------------
#update to test github
print('Hello Uncle')
print('Hello Somchai')
print('Hello Github')

friend = ['Loong', 'Pa Lek', 'Loong Dam']

print(friend[0])

#------------------

GUI.mainloop()
