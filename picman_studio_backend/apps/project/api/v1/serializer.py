from rest_framework import serializers

from picman_studio_backend.apps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, data):
        """Function to validate Project exists """
        if Project.objects.does_exist(company=data['company'], created_by=data['created_by']):
            raise serializers.ValidationError('Project Already exists')
        return data


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
