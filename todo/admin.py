from django.contrib import admin
from .models import Todo

# 把 Todo 模型注册到后台管理界面，这样才能在网页里操作
admin.site.register(Todo)