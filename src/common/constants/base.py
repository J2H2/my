
class CommonConstant:
    _LIST = ()
    _STRING_MAP = {}

    @classmethod
    def get_list(cls):
        return cls._LIST

    @classmethod
    def get_choices(cls):
        return ((item, cls._STRING_MAP[item]) for item in cls._LIST)

    @classmethod
    def to_string(cls, item) -> str:
        return cls._STRING_MAP[item]

    @classmethod
    def get_string_map(cls):
        return cls._STRING_MAP
