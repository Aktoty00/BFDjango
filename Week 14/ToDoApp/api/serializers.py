import logging

from rest_framework import serializers
from .models import TaskList, MyUser

logger = logging.getLogger(__name__)


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


class MyUserSerializer(serializers.ModelSerializer):
    tasklists = TaskListModelSerializer(many=True)
    tasklists_count = serializers.IntegerField(default=0)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'tasklists', 'tasklists_count')


class TaskListSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    created_by = MyUserSerializer(read_only=True)
    created_by_username = serializers.CharField(source='created_by.username')

    description = serializers.CharField()

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

