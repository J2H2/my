from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from apps.domains.account.services.token_service import TokenService


class TokenView(View):
    @method_decorator(login_required)
    def get(self, request):
        token = TokenService.get_token(request.user)
        context = {
            'token': token,
        }
        return render(request, 'account/token.html', context)
