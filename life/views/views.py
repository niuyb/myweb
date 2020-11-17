from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect



def life_page(request):
    return render(request, "life/life_page.html")


#
def life_copy(request):
    return render(request, "life/life_page_b.html")


def infos_api(request):
    # 生活记录最多1200字
    result={"data":[],"code":1,"msg":"","page":1,"total_results":315519,"total_pages":15776}

    res = []
    result["data"]=res


    return JsonResponse(result)