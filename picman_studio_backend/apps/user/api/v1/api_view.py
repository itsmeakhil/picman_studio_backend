from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from picman_studio_backend.apps.user.api.v1.services import UserService
from picman_studio_backend.apps.utils import response_helper


@permission_classes((AllowAny,))
class Login(APIView):

    def post(self, request):
        try:
            return UserService.login(self)
        except Exception as error:
            return response_helper.http_500('Internal server error occurred', error.__str__())


class Logout(APIView):

    def post(self, request):
        try:
            return UserService.logout(self)
        except Exception as error:
            return response_helper.http_500('Internal server error occurred', error.__str__())


@permission_classes((AllowAny,))
class Signup(APIView):

    def post(self, request):
        try:
            return UserService.signup(self, request)
        except Exception as error:
            return response_helper.http_500('Internal server error occurred', error.__str__())


class InviteUser(APIView):

    def post(self, request):
        try:
            return UserService.invite(self, request)
        except Exception as error:
            return response_helper.http_500('Internal server error occurred', error.__str__())
