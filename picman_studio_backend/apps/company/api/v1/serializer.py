from rest_framework import serializers

from picman_studio_backend.apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, data):
        """Function to validate Company exists """
        if Company.objects.does_exist(name=data['name'], email=data['email']):
            raise serializers.ValidationError('Company Already exists')
        return data


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
