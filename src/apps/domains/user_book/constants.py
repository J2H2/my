from lib.base.constants import BaseConstant


class OwnStatus(BaseConstant):
    NONE = 0
    WANT = 1
    OWN = 2

    _LIST = (NONE, WANT, OWN)
    _STRING_MAP = {
        NONE: 'Not own',
        WANT: 'Want',
        OWN: 'Own',
    }


class ReadingStatus(BaseConstant):
    NONE = 0
    READING = 1
    READ = 2

    _LIST = (NONE, READING, READ)
    _STRING_MAP = {
        NONE: 'Not own',
        READING: 'Want',
        READ: 'Own',
    }
