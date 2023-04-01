import time
from tkinter import *
from tkinter import ttk
import copy
import asyncio
from aiogram import Bot, Dispatcher

past_line = []
past_line_afk = []


def exit_action(icon):
    icon.visible = False
    icon.stop()
bot_token = "**************************************"
url = "https://api.telegram.org/bot"
bot = Bot(bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(): # получаем от пользователя сообщение start или help

    a = 1
    while a == 1:
        global file_path
        # 'D:\Games\poe\logs\Client.txt'
        file = open(file_path, 'r')
        last_line = file.readlines()[-1]
        time.sleep(.1)
        file.close() 
        if '@From' in last_line:

            global past_line
            # print (last_line)
            if last_line != past_line:
                time.sleep(.1)
                trade_msg = last_line
                print(trade_msg)
                past_line = copy.copy(last_line)
                print('past'+past_line)
                await bot.send_message(chatid, past_line)

            else:
                time.sleep(.1)
                print('rabotaet?')

            
            
        elif 'AFK' in last_line:
            global past_line_afk
            file = open('D:\Games\poe\logs\Client.txt', 'r', encoding='utf-8)
            last_line_afk = file.readlines()[-2]
            file.close() 
            time.sleep(.1)
            if last_line_afk != past_line_afk:
                past_line_afk = copy.copy(last_line_afk)
                print (last_line_afk)
                contents = last_line_afk
                await bot.send_message(chatid, contents)
            else:
                time.sleep(.1)
                print('rabotaet?afk')

        else:
            
            time.sleep(.1)
            await print ('skip')

#Chatid
text1 = []
text2 = []
def show_message():
    label["text"] = 'Нажми крестик'    
    global text1
    text1 = entry.get() 
    entry.delete(0, END)
    chatid_txt = open("chatid.txt", "w+")
    chatid_txt.write(text1)
    chatid_txt.close()

try:
    chatid_txt = open('chatid.txt', 'r')
    text1 = chatid_txt.readlines()[0]
    chatid_txt.close() 
    print(text1)

except:
    root = Tk()
    root.title("Trade_alert_poebot")
    root.geometry("350x150") 

    instruction = ttk.Label()
    instruction["text"] = 'Введите чат ID'
    instruction.pack(anchor=NW, padx=6, pady=6)

    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=6, pady=6)

    btn = ttk.Button(text="Click", command = show_message)
    btn.pack(anchor=NW, padx=6, pady=6)

    label = ttk.Label()
    label.pack(anchor=NW, padx=6, pady=6)

    root.mainloop()
#Путь к логам
def path_file():
    label["text"] = 'Нажми крестик'    
    global text2
    text2 = entry.get() 
    entry.delete(0, END)
    file_path_txt = open("file_path.txt", "w+")
    file_path_txt.write(text2)
    file_path_txt.close()

try:
    file_path = open('file_path.txt', 'r')
    text2 = file_path.readlines()[0]
    file_path.close() 
    print(text2)

except:
    root = Tk()
    root.title("Trade_alert_poebot")
    root.geometry("350x150") 

    instruction = ttk.Label()
    instruction["text"] = 'Введите путь к файлу Client.txt\nПример: D:\Games\poe\logs\Client.txt'

    instruction.pack(anchor=NW, padx=6, pady=6)

    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=6, pady=6)

    btn = ttk.Button(text="Click", command = path_file)
    btn.pack(anchor=NW, padx=6, pady=6)

    label = ttk.Label()
    label.pack(anchor=NW, padx=6, pady=6)

    root.mainloop()

chatid = text1
file_path = text2


asyncio.run(send_welcome())
