from datetime import date


def convert_to_date_from_8digit(date_string: str):
    year = int(date_string[0:4])
    if year is 0:
        year = 1

    month = int(date_string[4:6])
    if month is 0:
        month = 1

    day = int(date_string[6:8])
    if day is 0:
        day = 1

    return date(year, month, day)


def convert_6digit_to_8digit(date_string: str) -> str:
    _8digit_date_string = date_string
    if len(date_string) == 6:
        # There can be 6-digit data like 150906.
        # Do not do it correctly and go on trying to make an effort.
        # Add 2,000 in the first two places, and if it is bigger than the current date, it is a 20th century book.
        # It seems to be safe until this century (21st century).

        if int(date_string[0:2]) + 2000 > date.today().year:
            _8digit_date_string = '19' + date_string
        else:
            _8digit_date_string = '20' + date_string

    return _8digit_date_string


def convert_4digit_to_8digit(date_string: str) -> str:
    _date_string = date_string
    if len(_date_string) == 4:
        # There can be data with 4 digits like 2015
        # Do not do it correctly and go on trying to make an effort.
        _date_string = date_string + '0101'

    return _date_string
