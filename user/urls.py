from django.urls import re_path, path

from user import views

app_name="user"
urlpatterns = [
    # 登陆界面
    re_path(r'^login$', views.user_login.as_view(), name='login'),
    # 注册界面
    re_path(r'^register$', views.user_register.as_view(), name='register'),

    # # 登陆成功
    # re_path(r'^login_success$', views.login_info, name='login_success'),
    # # 注册成功
    # re_path(r'^register_success$', views.login_info, name='register_success'),



    # 用户中心
    re_path(r'^center$', views.user_center_home, name='user_center_home'),
    # 用户中心测试
    re_path(r'^test$', views.user_center_test, name='user_center_test'),

]