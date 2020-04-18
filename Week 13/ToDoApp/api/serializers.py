import logging

from rest_framework import serializers
from .models import TaskList, MyUser

logger = logging.getLogger(__name__)


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')


class TaskListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('name', 'created_by', 'photo', 'document', 'description', 'status')

    def validate_name(self, value):
        if '/' in value:
            logger.error(f'Invalid char was detected: {value}')
            raise serializers.ValidationError('invalid char in name field')
        return value

    def validate(self, attrs):
        return attrs


class TaskListSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    created_by = MyUserSerializer(read_only=True)
    description = serializers.CharField()

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
