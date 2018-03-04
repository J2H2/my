from typing import List

import requests
from bs4 import BeautifulSoup

from lib.kyobo.exceptions import WrongRequestException

ITEMS_PER_PAGE = 50


class ReachToEndException(Exception):
    pass


def _get_new_books_isbn_by_page(page: int, isbns: List[int]):
    url = 'http://www.kyobobook.co.kr/newproduct/newTopicKorList.laf'
    params = {
        'mallGb': 'KOR',
        'pageNumber': page,
        'targetPage': page,
        'perPage': ITEMS_PER_PAGE,
        'sortColumn': 'near_date',
    }

    response = requests.get(url, params=params)
    try:
        contents = response.content.decode('euc-kr')
    except UnicodeDecodeError:
        return WrongRequestException()

    soup = BeautifulSoup(contents, 'html.parser')

    items = soup.select('input[name=barcode]')
    if len(items) == 0:
        raise ReachToEndException()

    for item in items:
        isbn = item.get('value', None)
        if isbn is None:
            continue
        isbns.append(int(isbn))

    if len(isbns) != len(list(set(isbns))):
        raise ReachToEndException()


def get_new_books_isbn():
    isbns = []
    page = 1

    try:
        while True:
            _get_new_books_isbn_by_page(page, isbns)
            page += 1
    except ReachToEndException:
        pass

    return isbns
