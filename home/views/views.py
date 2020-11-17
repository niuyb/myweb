from django.http import HttpResponse
from django.shortcuts import render, redirect


#


def home(request):
    return render(request, "home/home.html")





# ———————————————————test———————————————————————————————


def mytest(request):

    return render(request,"test.html")


def post_input(request):

    return redirect("http://niuyb.vaiwan.com:8090")



def post_show(request):

    data={}
    if request.method == "POST":
        print("post!!!! ")
        post_name =request.POST.get("name")
        password =request.POST.get("password")
        gender =request.POST.get("gender")
        hobby =request.POST.getlist("hobby")
        print(post_name,password,gender,hobby)
        print(request.POST)
        data={
            "user":post_name,
            "password":password,
        }


    return render(request, "home/post_show.html", context=data)
