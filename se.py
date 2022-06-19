import json

import firebase_admin
from decouple import config

from firebase_admin import credentials

try:
    cred = credentials.Certificate({
        "type": config('FIREBASE_TYPE'),
        "project_id": config('FIREBASE_PROJECT_ID'),
        "private_key_id": config('FIREBASE_PRIVATE_KEY_ID'),
        "private_key": config('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
        "client_email": config('FIREBASE_CLIENT_EMAIL'),
        "client_id": config('FIREBASE_CLIENT_ID'),
        "auth_uri": config('FIREBASE_AUTH_URI'),
        "token_uri": config('FIREBASE_TOKEN_URI'),
        "auth_provider_x509_cert_url": config('FIREBASE_AUTH_PROVIDER_x509_CERT_URL'),
        "client_x509_cert_url": config('FIREBASE_CLIENT_x509_CERT_URL')
    })
    firebase_admin.initialize_app(cred)
except Exception as e:
    print(e.__str__())


def verify_firebase_user(uid):
    firebase_user = firebase_admin.auth.get_user(uid)
    if not firebase_user:
        return False
    return firebase_user


if __name__ == '__main__':
    user = verify_firebase_user('TYIhmEU87BRMzonnqYbGlCiFfz52')
    print(json.dumps(user.__dict__))
