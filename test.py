# -*- coding: utf-8 -*-
import random
def say_random_message():#ランダムでメッセージを返すよ
    f = open("./random_text.txt",encoding="utf-8_sig")
    message_list = f.readlines()
    f.close()
    print(message_list[random.randint(0,len(message_list)-1)])

def add_random_message(add_message):#ランダムメッセージを追加するよ
    f = open("./random_text.txt","a",encoding="utf-8_sig")
    f.write("\n"+add_message)
    f.close()
    print(add_message+" OK!")

def index_random_message():#ランダムメッセージ一覧みるよ
    f = open("./random_text.txt",encoding="utf-8_sig")
    message_list = f.readlines()
    f.close()
    for i in range(len(message_list)):
        print(str(i)+":"+message_list[i])

def del_random_message(i):#ランダムメッセージ消すよ
    f = open("./random_text.txt",encoding="utf-8_sig")
    message_list = f.readlines()
    f.close()
    try :
        del message_list[i]
        f = open("./random_text.txt","w",encoding="utf-8_sig")
        messages = ""
        for message in message_list:
            messages += message
        f.write(messages)
        f.close()
        print("delete completed ")
    except IndexError:
        print("配列外参照なんですが...")

        
while True:
    message = input()
    if message == "huji":
        say_random_message()
    if "/add_rand " in message:
        add_random_message(message.lstrip("/add_rand "))
    if "/index_rand" == message:
        index_random_message()
    if "/del_rand" in message:
        del_random_message(int(message.lstrip("/del_rand ")))
