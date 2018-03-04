from datetime import date


def convert_to_date_from_8digit(date_string: str):
    year = int(date_string[0:4])

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
        # 150906 이렇게 6자리로된 데이터가 있을 수 있다.
        # 정확하게는 안되고 노력을 해보자는 의미로 진행한다.
        # 앞의 두자리에 2000을 더해보고 현재 날짜 보다 크면 20세기 도서라고 판단하자.
        # 이번 세기(21세기)까지는 안전할 것으로 보인다.
        if int(date_string[0:2]) + 2000 > date.today().year:
            _8digit_date_string = '19' + date_string
        else:
            _8digit_date_string = '20' + date_string

    return _8digit_date_string


def convert_4digit_to_8digit(date_string: str) -> str:
    _date_string = date_string
    if len(_date_string) == 4:
        # 2015 이렇게 4자리로된 데이터가 있을 수 있다.
        # 정확하게는 안되고 노력을 해보자는 의미로 진행한다.
        _date_string = date_string + '0101'

    return _date_string
