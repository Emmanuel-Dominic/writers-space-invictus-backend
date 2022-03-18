import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User
"""Configure JWT Here"""
class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header:
            return None

        if len(auth_header) != 2:
            msg = 'Invalid Token'
            raise exceptions.AuthenticationFailed(msg)

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix != 'Bearer':
            msg = 'Use a Bearer Token'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(request, token)

    @classmethod
    def authenticate_credentials(cls, request, token):

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms='HS256')
        except jwt.InvalidTokenError:
            msg = 'Invalid token. Could not decode token'
            raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignatureError:
            msg = 'Token expired, please login again.'
            raise exceptions.AuthenticationFailed(msg)
        token_data = payload['user_data'].split()

        try:
            token_data = payload['user_data'].split()
            user = User.objects.get(
                email=token_data[0], username=token_data[1])
        except User.DoesNotExist:
            msg = 'No user matching this token'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "User has been deactivated"
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
