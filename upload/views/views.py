from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect





#
def upload_page(request):
    return render(request, "contribution/upload.html")


def upload_test(request):
    return JsonResponse({"id":101})
