## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP


## 简单的使用方法：


创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表(python manage.py migrate)
运行python manage.py runserver启动服务器


路由设置：


from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]

# 说明
这个项目还有俩app
- login 是一个简单的用户注册，登陆功能
```
首页地址：http://127.0.0.1:8000/login/index/
注册地址：http://127.0.0.1:8000/login/login/
```
- polls 是一个简单的在线投票系统
```
首页地址：http://127.0.0.1:8000/polls/

```

默认后台地址：
```
http://127.0.0.1:8000/admin
用户名:admin
密码:123456
```

关于静态文件
1.关于debug模式后，还需要设置一下ALLOWED_HOSTS
2.默认关闭debug后，静态页面无法访问，此时，测试使用的话可以使用如下命令：`python manage.py runserver --insecure`
部署到服务器的话结合nginx使用