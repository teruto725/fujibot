# -*- coding: utf-8 -*-
import random
def say_random_message():#ランダムでメッセージを返すよ
    f = open("./random_text.txt",encoding="utf-8_sig")
    message_list = f.readlines()
    f.close()
    print(message_list[random.randint(0,len(message_list)-1)])

def add_random_message(add_message):#ランダムメッセージを追加するよ
    f = open("./random_text.txt","a",encoding="utf-8_sig")
    f.write(add_message)
    f.close()
    print(add_message+" OK!")

while True:
    message = input()
    if message == "huji":
        say_random_message()
    if "/add_rand " in message:
        add_random_message(message.lstrip("/add_rand "))
