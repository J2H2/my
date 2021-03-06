from rest_framework.response import Response

from infra.networks.api_status_code import ApiStatusCodes, StatusCode
from infra.networks.statue_code import ResponseCode
from lib.base.exceptions import ErrorException


class ApiResponseMixin:
    @staticmethod
    def _make_response(response_code: ResponseCode, data=None) -> Response:
        if data is None:
            data = {}

        if 'message' in data or 'code' in data:
            raise ErrorException('Data field names contain reserved words.')

        if response_code.has_message():
            data['message'] = response_code.get_message()

        if response_code.has_code():
            data['code'] = response_code.get_code()

        headers = {}
        return Response(data, status=response_code.get_status(), headers=headers)

    @staticmethod
    def make_response_code(status: StatusCode, message: str = None) -> ResponseCode:
        return ResponseCode(status_code=status, message=message)

    @classmethod
    def success_response(cls, data=None, response_code: ResponseCode = None) -> Response:
        if response_code is None:
            response_code = ResponseCode(ApiStatusCodes.C_200_OK)
        return cls._make_response(response_code, data=data, )

    @classmethod
    def fail_response(cls, response_code: ResponseCode, data=None) -> Response:
        return cls._make_response(response_code, data=data)
