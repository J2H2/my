import time
from time import sleep
from typing import Type

import requests
import xmltodict
from django.conf import settings

from lib.naver.dtos import BaseNaverSearchApiResult, NaverBookSearchApiResult, NaverSearchApiResult
from lib.naver.exceptions import NaverWrongRequest

MAX_SEARCH_RESULT_COUNT = 100
SEARCH_BOOK_URL = 'https://openapi.naver.com/v1/search/book.xml'
ALLOWED_REQ_COUNT_IN_SEC = 10


class RequestBalancer:
    _count = {}

    @classmethod
    def ready(cls):
        timestamp = int(time.time())

        if cls._count.get(timestamp, None) is None:
            cls._count[timestamp] = 0
        cls._count[timestamp] += 1

        if cls._count[timestamp] > ALLOWED_REQ_COUNT_IN_SEC:
            sleep(0.5)
            cls._count.clear()


def search_book(query: str):
    params = {
        'query': query,
        'display': MAX_SEARCH_RESULT_COUNT,
    }

    return _call(NaverBookSearchApiResult, SEARCH_BOOK_URL, params)


def _call(ditme: Type[BaseNaverSearchApiResult], url: str, params: dict) -> NaverSearchApiResult:
    RequestBalancer.ready()

    headers = {
        'X-Naver-Client-Id': settings.NAVER_OPEN_API_CLIENT_ID,
        'X-Naver-Client-Secret': settings.NAVER_OPEN_API_CLIENT_SECRET,
    }

    response = requests.get(url, params=params, headers=headers)
    contents = response.content.decode()

    if response.status_code is not 200:
        raise NaverWrongRequest(contents)

    return NaverSearchApiResult.from_dict(ditme, xmltodict.parse(contents))
