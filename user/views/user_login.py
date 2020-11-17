import base64
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from myweb.config import COOKIE_INVALID
from public.config import RESULT, RE_EMAIL







USER_CENTER_URL= "/center"
REGISTER_NEXT_URL = "/user/center"


class user_login(View):

    def get(self,request):
        if 'username' in request.COOKIES:
            return redirect('/user/center')
        else:
            return render(request, 'user/user_login.html')

    def post(self,request):
        result = RESULT
        errmsg=""
        email = request.POST.get("email")
        password = request.POST.get("password")
        # 校验数据
        result["data"] = ["login"]
        result["code"] = 1
        result["msg"] = ""

        if not email:
            errmsg = '邮箱不能为空'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        elif not re.match(RE_EMAIL,email):
            errmsg = '请输入正确的邮箱'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        else:
            pass
        if not password:
            errmsg = '密码不能为空'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        else:
            pass
        # 验证
        u = base64.b64encode(email.encode("utf8")).decode("utf8")
        result["msg"] = errmsg
        response = JsonResponse(result)
        response.set_cookie('username', u, max_age=COOKIE_INVALID)

        return response




class user_register(View):

    def get(self,request):
        return render(request, 'user/user_register.html')


    def post(self,request):
        result = RESULT
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # confirm_password = request.POST.get("confirm_password")
        result["data"] = ["register"]
        result["code"] = 1
        result["msg"] = ""

        # 校验数据
        if not email:
            errmsg = '邮箱不能为空'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        elif not re.match(RE_EMAIL,email):
            errmsg = '请输入正确的邮箱'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        else:
            pass
        if not password:
            errmsg = '密码不能为空'
            result["code"] = -1
            result["msg"] = errmsg
            return JsonResponse(result)
        else:
            pass


        print(username,password)
        print(request.POST)
        return redirect(reverse("user:user_center_home"))

