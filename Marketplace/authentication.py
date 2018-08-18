from accounts.models import User
from rest_framework import authentication
from rest_framework import exceptions

# when using Django REST Framework
class ApiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('HTTP_X_EMAIL')
        if not email:
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)