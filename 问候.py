from time import sleep
import pyperclip
from pymouse import PyMouse 
import pyautogui
import pyautogui as pag
import pyautogui as pg

print('你需要@的人(直接输入qq号)')              #自定义@的人
name = input()

print('你需要发送消息后紧跟的表情(例如/cy,可在qq内输入/自己查看)')
expression = input()

print('请将鼠标防止聊天框内，你有5秒时间移动鼠标')  #取聊天框
sleep(5)
x,y = pag.position()
pyautogui.moveTo(x,y)                            

with open(r'1.txt', encoding="utf-8") as file:
    lines = list(file)      #以列表形式赋值文本
    i=0
    o = len(lines)          #获取列表元素数量

    while i < o :
        text = lines[i]
        print(text)
        
        pyperclip.copy(text)            #模拟键盘操作
        spam = pyperclip.paste() 

        pg.write(f'@{name}')
        pg.press('enter')

        pyautogui.hotkey('ctrl','v')
        pg.press('enter')


        pg.write(expression,interval=0.0001)
        pg.press('enter')


        i = i+1
file.close        
        #可优化：1.修改英文输入法   2.自定义@的人   3.自定义表情
    
    
