from rest_framework import serializers

from picman_studio_backend.apps.user.models import User, UserInvite


class UserSerializer(serializers.ModelSerializer):
    """Serializer to the user details"""

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserInviteSerializer(serializers.ModelSerializer):
    """Serializer to the User Invites"""

    class Meta:
        model = UserInvite
        fields = '__all__'
