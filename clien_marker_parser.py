import requests
from bs4 import BeautifulSoup
import os

import telegram
import time

bot = telegram.Bot(token='1468872772:AAFziOdiTK-mHxBsYxvL6n9e7AQ1vV4IYU8')

chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('https://www.clien.net/service/board/sold')
    req.encoding = 'utf-8' # 클리앙에서 encdoing 정보를 보내주지 않아서 추가해야함

    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    posts = soup.select('#div_content > div.list_content > div:nth-child(1) > div.list_title > a > span.subject_fixed')

    latest= posts[0].text

    with open(os.path.join(BASE_DIR,'latest.txt'),'r+') as f_read:
        before = f_read.readline()
        if before !=latest:
            bot.sendMessage(chat_id=chat_id,text="새 글이 올라왔어요!")
        else:
            bot.sendMessage(chat_id=chat_id,text="새 글이 없어요ㅜㅜ")
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
        f_write.write(latest)
        f_write.close()

    time.sleep(60)