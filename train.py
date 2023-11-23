import json

import requests
import time

API_URL = 'https://api.telegram.org/bot'
API_CAT_URL = 'https://api.thecatapi.com/v1/images/search'
TOKEN = ''
ERROR_TEXT = 'Нету картинки'
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int # сообщаем что эта переменная должна быть инт
cat_response: requests.Response
cat_link: str



while counter < MAX_COUNTER:

    print('attemt =',counter)
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset+1}').json()

    # print(json.dumps(updates,separators=(',','-'),indent='    '))
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CAT_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                print(cat_link)
                requests.get(f'{API_URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text=Нету кота сорян')

                # requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
