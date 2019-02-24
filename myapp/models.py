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
        self.id = ''
        self.report_status = ''

    def get_id(self):
        data = {
            # указываем метод вордстат, с которым работаем, в данном случае - создаем отчет
            'method': 'CreateNewWordstatReport',
            # указываем токен доступа
            'token': self.token,
            'locale': 'ru',
            # задаем входные параметры; у каждого метода они свои
            'param': {
                # Указываем не более 10 фраз через запятую
                #'Phrases': ['айфон 7 цены ростов ', 'купить колбасу']
                'Phrases': [self.phrase]
            }}
        # Трансформируем json-запрос в одну строку и отправляем в Яндекс:)
        jdata = json.dumps(data, ensure_ascii=False)
        # print(jdata)
        r = requests.post(self.url, jdata.encode('utf-8'))
        return r.text

    def checkRep(self):
        data = {
            # метод проверки готовности отчета
            'method': 'GetWordstatReportList',
            'token': self.token
        }
        jdata = json.dumps(data, ensure_ascii=False)
        r = requests.post(self.url, jdata)
        # responsedata = json.loads(r.read().decode('utf-8', 'ignore'))

        # print(responsedata['data'][len(responsedata['data']) - 1]['StatusReport'])
        # self.report_status = r.text[]
        # return responsedata['data'][len(responsedata['data']) - 1]['StatusReport']

    def readRep(self):
        while self.report_status != 'Done':
            print ('...')
            time.sleep(2)

        print(self.id, ' id')
        data = {
            # используем метод для получения отчета
            'method': 'GetWordstatReport',
            'token': self.token,
            # указываем номер отчета
            'param': self.id
        }
    #
        jdata = json.dumps(data, ensure_ascii=False)
        r = requests.post(self.url, jdata)
        # return r.text
