from lib.base.constants import BaseConstant


class BookImageType(BaseConstant):
    FRONT_COVER = 0
    SPINE = 1
    BACK_COVER = 2

    _LIST = (FRONT_COVER, SPINE, BACK_COVER,)
    _STRING_MAP = {
        FRONT_COVER: 'Front cover',
        SPINE: 'Spine',
        BACK_COVER: 'Back cover',
    }


class BookImageSourceType(BaseConstant):
    NAVER = 0
    ALADIN = 1
    AMAZON = 2

    _LIST = (NAVER, ALADIN, AMAZON, )
    _STRING_MAP = {
        NAVER: 'Naver',
        ALADIN: 'Aladin',
        AMAZON: 'Amazon',
    }
