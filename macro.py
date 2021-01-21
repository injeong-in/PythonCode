import pyautogui as m
import pyautogui
from random import *
import time
import sys

Choice_arr = []
Mouse_L_X = [] # 매크로 마우스의 x좌표를 저장할 리스트
Mouse_L_Y = []
Mouse_R_X = []
Mouse_R_Y = []
Mouse_time = []
Keyboard_in_list = []
Keyboard_time = []

def Keyboard_in():
    pass

def Mouse_in():
    tmp = input('1 엔터 2스페이스바 : ')
    Keyboard_in_list.append(tmp)
    tmp = input('키보드 입력 동작 시간 입력 : ')
    Keyboard_time.append(tmp)
def start():
    while True:
        M_time_cnt = -1
        K_time_cnt = -1

        for i in Choice_arr:
            if i=='1':
                M_time_cnt += 1
                Mouse_out(M_time_cnt)
            elif i=='2':
                K_time_cnt += 1
                Keyboard_out(K_time_cnt)
            else:
                print('다시 시작.')

def main():
    while True:
        Choice = input("1.마우스 이동/클릭 2.키보드입력 3.시작 : ")
        print(Choice)
        Choice_arr.append(Choice)  # 입력한 동작을 저장
        if Choice == '1':
            Mouse_in()
        elif Choice == '2':
            Keyboard_in()
        else:
            print("start!!")
            start()
            break

if __name__ == '__main__' :
    main()