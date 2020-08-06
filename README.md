# 简单的使用方法：
- 创建虚拟环境
- 使用pip安装第三方依赖
- 修改settings.example.py文件为settings.py
- 运行migrate命令，创建数据库和数据表(python manage.py migrate)
- 运行python manage.py runserver启动服务器


# 路由设置
```
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
```
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

# 关于静态文件
1.关于debug模式后，还需要设置一下ALLOWED_HOSTS
2.默认关闭debug后，静态页面无法访问，此时，测试使用的话可以使用如下命令：`python manage.py runserver --insecure`
部署到服务器的话结合nginx使用

# 首页
home模块是首页文件
参考地址：https://github.com/noisky?tab=repositories

# 数据库模型
## 数据库配置
```
# mysite/settings.py
# Django默认使用SQLite数据库

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


----- mysql -----
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'mysite',  # 数据库名，先前创建的
        'USER': 'root',     # 用户名，可以自己创建用户
        'PASSWORD': '****',  # 密码
        'HOST': '192.168.1.121',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
    }
}
```



## 数据库日常操作
将应用添加到项目中，需要在INSTALLED_APPS设置中增加指向该应用的配置文件的链接
```
# mysite/settings.py

INSTALLED_APPS = [
    'polls.apps.PollsConfig', # 注意这行数据
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```


```
在models.py中修改模型
运行python manage.py makemigrations为改动创建迁移记录
运行python manage.py migrate，将操作同步到数据库

检查：python manage.py check

运行某一个具体应用的模型：python manage.py makemigrations polls
查看具体sql语句：python manage.py sqlmigrate polls 0001 
运行某一个具体应用的模型同步到数据库：python manage.py migrate polls


```

## 使用模型的API
```
$ python manage.py shell

>>> import django
>>> django.setup()

>>> from polls.models import Question, Choice # 导入我们写的模型类
    # 现在系统内还没有questions对象
>>> Question.objects.all()
    <QuerySet []>

>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

>>> q.id
1
```

# admin后台管理站点
创建一个可以登录admin站点的用户
```
$ python manage.py createsuperuser
```
