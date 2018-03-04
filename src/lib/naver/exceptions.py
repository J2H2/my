class NaverApiException(Exception):
    pass


class NaverWrongRequest(NaverApiException):
    pass


class InvalidItemData(NaverApiException):
    pass


class InvalidBookData(InvalidItemData):
    pass
