import datetime

from django.db import models
from django.utils import timezone

import json
import requests
import time


class WordStat:

    def __init__(self, phrase):
        self.phrase = phrase
        self.url = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
        self.token = 'AQAAAAACslbuAAWDAxMwffnF303dsVgLYJGLyy8'

    def get_id(self):
        data = {
            # указываем метод вордстат, с которым работаем, в данном случае - создаем отчет
            'method': 'CreateNewWordstatReport',
            # указываем токен доступа
            'token': self.token,
            'locale': 'ru',
            # задаем входные параметры; у каждого метода они свои
            'param': {
                'Phrases': [self.phrase]
            }}
        # Трансформируем json-запрос в одну строку и отправляем в Яндекс
        jdata = json.dumps(data, ensure_ascii=False)
        r = requests.post(self.url, jdata.encode('utf-8'))
        rdata = json.loads(r.text)
        return rdata["data"]

    # Функция проверки готовности отчета
    def checkRep(self):
        data = {
            # метод проверки готовности отчета
            'method': 'GetWordstatReportList',
            'token': self.token
        }
        jdata = json.dumps(data, ensure_ascii=False)
        r = requests.post(self.url, jdata.encode('utf-8'))
        rdata = json.loads(r.text)
        return rdata["data"][len(rdata["data"]) - 1]["StatusReport"]

    def readRep(self, id):
        # Задаем условие: пока функция проверки готовности не даст положительный ответ, будем ждать
        while self.checkRep() != 'Done':
            print('...')
            time.sleep(2)

        print(id, ' id')

        data = {
            # используем метод для получения отчета
            'method': 'GetWordstatReport',
            'token': self.token,
            # указываем номер отчета
            'param': id
        }

        jdata = json.dumps(data, ensure_ascii=False)
        r = requests.post(self.url, jdata.encode('utf-8'))
        rdata = json.loads(r.text)
        return rdata["data"][0]
