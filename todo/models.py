from django.contrib.auth.models import User
from django.db import models

# 定义 Todo 模型，对应数据库里的表
class Todo(models.Model):
    title = models.CharField(max_length=100)  # 待办事项的标题，最大长度100
    memo = models.TextField(blank=True)       # 备忘录内容，blank=True 表示可以不填
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间，添加时自动获取当前时间
    completed = models.BooleanField(default=False)        # 是否完成，默认是 False（未完成）
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 关联用户，用户删除时对应数据也删除

    # 在后台显示对象时，直接显示标题，方便阅读
    def __str__(self):
        return self.title