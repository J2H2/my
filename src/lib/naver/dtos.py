from datetime import date
from typing import Type

from lib.naver.exceptions import InvalidBookData, InvalidItemData
from lib.utils.book import validate_isbn
from lib.utils.date import convert_4digit_to_8digit, convert_6digit_to_8digit, convert_to_date_from_8digit
from lib.utils.string import clean_tag


class BaseNaverSearchApiResult:
    @classmethod
    def from_dict(cls, xml: dict) -> Type['BaseNaverSearchApiResult']:
        raise NotImplemented


class NaverBookSearchApiResult(BaseNaverSearchApiResult):
    def __init__(self):
        self.title = ''
        self.image = ''
        self.author = ''
        self.publisher = ''
        self.isbn = ''
        self.description = ''
        self.pubdate = date.min
        self.discount = 0
        self.price = 0

    @classmethod
    def from_dict(cls, xml: dict) -> 'NaverBookSearchApiResult':
        result = cls()
        result.title = cls._parse_title(xml['title'])
        result.image = cls._parse_image(xml['image'])
        result.author = clean_tag(xml['author'])
        result.publisher = clean_tag(xml['publisher'])
        result.isbn = cls._parse_isbn(xml['isbn'])
        result.description = clean_tag(xml['description'])
        result.pubdate = cls._parse_date(xml['pubdate'])
        result.discount = cls._parse_price(xml['discount'])
        result.price = cls._parse_price(xml['price'])

        return result

    @classmethod
    def _parse_title(cls, title: str) -> str:
        return clean_tag(title)

    @classmethod
    def _parse_isbn(cls, raw_isbn: str) -> int:
        if raw_isbn is None:
            raise InvalidBookData()

        isbns = [clean_tag(isbn) for isbn in raw_isbn.split(' ')]
        return cls._get_isbn(isbns)

    @classmethod
    def _get_isbn(cls, isbns: list) -> int:
        for isbn in isbns:
            try:
                isbn_integer = int(isbn)
            except ValueError:
                continue

            if validate_isbn(isbn_integer):
                return isbn_integer

        raise InvalidBookData()

    @classmethod
    def _parse_image(cls, image: str) -> str:
        if image is None:
            raise InvalidBookData()

        return image

    @classmethod
    def _parse_date(cls, date_string: str) -> date:
        _date_string = date_string
        if _date_string == '' or _date_string is None:
            return date.min

        _8digit_date_string = _date_string
        if len(_date_string) == 4:
            _8digit_date_string = convert_4digit_to_8digit(_date_string)
        elif len(date_string) == 6:
            _8digit_date_string = convert_6digit_to_8digit(_date_string)

        return convert_to_date_from_8digit(_8digit_date_string)

    @classmethod
    def _parse_price(cls, price: str) -> int:
        # Sometimes the price has a decimal point. Convert to floating point and convert to integer
        return 0 if price is None else int(float(price))


class NaverSearchApiResult:
    def __init__(self):
        self.total = 0
        self.start = 0
        self.display = 0
        self.items = []

    @classmethod
    def from_dict(cls, ditem: Type[BaseNaverSearchApiResult], xml: dict) -> 'NaverSearchApiResult':
        result = cls()
        result.total = int(xml['rss']['channel']['total'])
        result.start = int(xml['rss']['channel']['start'])
        result.display = int(xml['rss']['channel']['display'])
        result.items = []

        if result.display == 0:
            return result

        if result.display == 1:
            try:
                result.items.append(ditem.from_dict(xml['rss']['channel']['item']))
            except InvalidItemData:
                pass
            return result

        for item in xml['rss']['channel']['item']:
            try:
                result.items.append(ditem.from_dict(item))
            except InvalidItemData:
                continue

        return result
