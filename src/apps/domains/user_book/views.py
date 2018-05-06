from rest_framework.views import APIView

from lib.base.views import ApiResponseMixin


class IndexView(ApiResponseMixin, APIView):
    def get(self, request):
        data = {
        }

        return self.success_response(data=data)
