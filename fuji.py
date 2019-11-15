# インストールした discord.py を読み込む
import discord
import random
import re
import time
import threading
import requests

TOKEN = "NTc4MTM2Mjc2OTE0NTM2NDU4.XNvPgQ.8Prc-jk79aoTQ5iGwDzmy5G21Gw"
client = discord.Client()


async def weather_tomorrow(message):#明日の天気を返すよ！
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    payload = {"奈良":{"city":"290010"},"福岡":{"city":"400010"},"徳島":{"city":"360010"},"大阪府":{"city":"270000"}}
    for cityname in payload.keys():
        tenki_data = requests.get(url, params=payload[cityname]).json()
        await message.channel.send(cityname+"の明日における天気は     "+tenki_data["forecasts"][1]["telop"])

async def weahter_nexttomorrow(message):#明後日の天気を返すよ！
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    payload = {"奈良":{"city":"290010"},"福岡":{"city":"400010"},"徳島":{"city":"360010"},"大阪府":{"city":"270000"}}
    for cityname in payload.keys():
        tenki_data = requests.get(url, params=payload[cityname]).json()
        await message.channel.send(cityname+"の明後日における天気は     "+tenki_data["forecasts"][2]["telop"])

async def say_random_message(message):#ランダムでメッセージを返すよ
    f = open("./random_text.txt",encoding="utf-8_sig")
    message_list = f.readlines()
    f.close()
    await message.channel.send(massage_list[random.randint(0,len(message_list)-1)])

async def add_random_message(message,add_message):#ランダムメッセージを追加するよ
    f = open("./random_text.txt","a",encoding="utf-8_sig")
    f.write(add_message)
    f.close()
    await message.channel.send(add_message+" OK!")

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if  '明日の天気' in message.content:
        await weather_tomorrow(message)
    if "明後日の天気" in message.content:
        await weahter_nexttomorrow(message)
    if  '藤' in message.content or "剣道" in message.content:
        await say_random_message(message)

    if "/add_rand " in message.content:
        await add_random_message(message,add_message.lstrip("/add_rand "))

    if "ダイス" in message.content:
        await message.channel.send(str(random.randint(0,5)+1))


client.run(TOKEN)
