import firebase_admin
from decouple import config
from django.contrib.auth import logout
from django.db import transaction
from firebase_admin import credentials, auth
from rest_framework.authtoken.models import Token

from picman_studio_backend.apps.company.models import Company
from picman_studio_backend.apps.user.api.v1.serializer import UserSerializer, UserInviteSerializer
from picman_studio_backend.apps.user.models import User, UserInvite
from picman_studio_backend.apps.utils import response_helper
from picman_studio_backend.apps.utils.constants import INVITE_ACCEPTED


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "picman-studio",
  "private_key_id": config('FIREBASE_PRIVATE_KEY_ID'),
  "private_key": config('FIREBASE_PRIVATE_KEY'),
  "client_email": "firebase-adminsdk-nr6p1@picman-studio.iam.gserviceaccount.com",
  "client_id": config('FIREBASE_CLIENT_ID'),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-nr6p1%40picman-studio.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred)


class UserService:

    def verify_firebase_user(self, uid):
        firebase_user = firebase_admin.auth.get_user(uid)
        if not firebase_user:
            return False
        return True

    def login(self):
        uid = self.request.data['uid']
        if not self.verify_firebase_user(uid):
            return response_helper.http_404('Firebase user not found')
        user_exists = User.objects.filter(uid=uid).exists()
        if not user_exists:
            return response_helper.http_404('Unable to find the user, Please sign up first')

        user = User.objects.get(uid=uid)
        user_data = UserSerializer(user)
        if not user.allow_multiple_sessions:
            Token.objects.filter(user=user).delete()
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            "token": token.key,
            "user_data": user_data.data
        }
        return response_helper.http_200('User Login successfull', data)

    def logout(self):
        """Function to logout the current user"""
        with transaction.atomic():
            logout(self.request)
            return response_helper.http_200_message('User logged out successfully')

    def signup(self, request):
        self.request = request
        with transaction.atomic():
            uid = self.request.data['uid']
            if not self.verify_firebase_user(uid):
                return response_helper.http_404('Firebase user not found')
            user_exists = User.objects.filter(uid=uid).exists()
            if user_exists:
                return response_helper.http_404('User already signed up, Please login to use the application')
            if UserInvite.objects.does_exist(email=self.request.data['email']):
                invite = UserInvite.objects.get(email=self.request.data['email'])
                company = invite.company
                invite.status = INVITE_ACCEPTED
                invite.save()
            else:
                company = Company.objects.create(name=self.request.data['company_name'],
                                                 location=self.request.data['location'])

            serializer = UserSerializer(data=self.request.data)
            if serializer.is_valid():
                user = serializer.save(company=company)
                token, _ = Token.objects.get_or_create(user=user)
                user_data = {
                    "token": token.key,
                    "user_data": user.data
                }
                return response_helper.http_201('User added successfully', user_data)
            return response_helper.http_400('Data format is incorrect, Please check the data')

    def invite(self):
        email = self.request.data['email']
        if UserInvite.objects.does_exist(email=email):
            return response_helper.http_400('User already Invited')
        serializer = UserInviteSerializer(data=self.request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Unable to invite user', serializer.errors)
        invite_data = serializer.save(created_by=self.request.user)
        return response_helper.http_201('UserInvite added successfully', invite_data)
