class StatusCode:
    def __init__(self, status: int, code: str = None):
        self.status = status
        self.code = code

    def has_code(self) -> bool:
        return self.code is not None


class ResponseCode:
    def __init__(self, status_code: StatusCode, message: str = None):
        self.status_code = status_code
        self.message = message

    def has_code(self) -> bool:
        return self.status_code.has_code()

    def has_message(self) -> bool:
        return self.message is not None

    def get_status(self) -> int:
        return self.status_code.status

    def get_code(self) -> str:
        return self.status_code.code

    def get_message(self) -> str:
        return self.message
