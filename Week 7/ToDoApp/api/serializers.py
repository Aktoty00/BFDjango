from rest_framework import serializers
from .models import TaskList, MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')


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
