from os.path import isfile, isdir, exists
from tkinter import *
from tkinter import filedialog
import os
root = Tk()
root.title("파일확인")
root.geometry("640x480")


listbox = Listbox(root, selectmode="extended", height=0)
txt = Text(root, width=30,height=2)
txt.pack()

def btncmd():
    value = txt.get("1.0", 'end-1c')

    path = os.listdir(value)

    int = 0;
    int2 = 0;
    int3 = 0;

    for i in path:
        listbox.insert(int, '[ROOT 폴더]')
        int += 1
        listbox.insert(int, i)
        int += 1
        listbox.insert(int, 'ㄴ')
        int += 1
        value2 = value + path[int2]
        d_path = os.listdir(value2)
        int2 += 1
        for j in d_path:
            listbox.insert(int, j)
            int += 1
            value3 = value2 + '/' + d_path[int3]
            # if os.listdir(value3) :
            #     dd_path = os.listdir(value3)
            #     int3 += 1
            # for k in dd_path:
            #     listbox.insert(int, k)
            #     int += 1

    listbox.pack()

def btncmd2():
    value = txt.get("1.0", 'end-1c')

    path = os.listdir(value)
    listbox.insert(0, '[시작]')
    int = 1;
    for i in path:
            listbox.insert(int, i)
            int +=1;

    listbox.pack()


def pathcmd():
    file_path = filedialog.askdirectory(initialdir='.') #파일경로 선택
    txt.insert(END,file_path+'/') #텍스트 입력값 삽입
    l1 = Label(root, text="File path: " + file_path).pack()

btn1 = Button(root, text="경로선택", command = pathcmd)
btn1.place(x=110, y=80)
btn1.pack()


btn2 = Button(root, text="클릭(1단경로)", command = btncmd2)
btn2.place(x=110, y=80)
btn2.pack()


btn3 = Button(root, text="클릭(2단경로)", command = btncmd)
btn3.place(x=300, y=80)
btn3.pack()



root.mainloop()