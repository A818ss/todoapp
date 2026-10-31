from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created_at', 'completed']

# 专门用于一键切换完成的序列化器
class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        # 只有id需要，其他字段全设为只读
        read_only_fields = ['title', 'memo', 'created_at', 'completed']