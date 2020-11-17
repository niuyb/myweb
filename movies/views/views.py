from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from myweb.config import EMBY_URL
from myweb.settings import STATIC_URL




movies_static_path = STATIC_URL[1:]+"img/movies/"



#
def movies_page(request):
    return render(request, "movies/movies.html")


# def upload_test(request):
#     return JsonResponse({"id":101})

# D:\file\myweb\myweb\static\img\movies\godzilla.jpg

def infos_api(request):
    result={"data":[],"code":1,"msg":"","page":1,"total_results":315519,"total_pages":15776,"link_url":"http://localhost:8096/web/index.html#!/item?serverId=e14d85210dee439387e4a0ae229174b0&id="}

    res = [
        {"original_title":"神奇女侠","movies_infos":"我的这种情况是什么那阿萨的骄傲阿斯顿啊我的这种情况是什么那阿萨的骄傲阿斯顿啊","img_path":movies_static_path+"godzilla.jpg","link":"9"},
        {"original_title":"哥斯拉","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"10"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"11"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "神奇女侠", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title":"神奇女侠","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title":"哥斯拉","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title":"神奇女侠","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title":"哥斯拉","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title":"神奇女侠","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title":"哥斯拉","movies_infos":"ansodajsodasd","img_path":movies_static_path+"godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
        {"original_title": "哥斯拉", "movies_infos": "ansodajsodasd", "img_path": movies_static_path + "godzilla.jpg","link":"1"},
    ]
    result["data"]=res


    return JsonResponse(result)



def test(request):

    return redirect(EMBY_URL+'item?id=7&serverId=e14d85210dee439387e4a0ae229174b0')



