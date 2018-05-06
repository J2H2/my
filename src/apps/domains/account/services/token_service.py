from rest_framework.authtoken.models import Token

from apps.domains.account.models import User


class TokenService:
    @classmethod
    def get_token(cls, user: User) -> Token:
        token, _ = Token.objects.get_or_create(user=user)
        return token
