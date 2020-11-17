"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.App, name='App')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='App')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.conf import settings
# from support import views
from django.contrib import admin

urlpatterns = [
    # re_path(r'^admin/', admin.site.urls),

    # 主页
    re_path(r'^', include('home.urls'), name='home'),
    # 登陆界面
    re_path(r'^user/', include('user.urls', namespace="user")),
    # 图片分页
    re_path(r'^picture/', include('picture.urls', namespace="picture")),
    # 投稿分页
    re_path(r'^contribution/', include('upload.urls', namespace="contribution")),
    # 电影分页
    re_path(r'^movies/', include('movies.urls', namespace="movies")),
    # 工具分页
    re_path(r'^tools/', include('tools.urls', namespace="tools")),
    # 生活记录分页
    re_path(r'^life/', include('life.urls', namespace="life")),

]
