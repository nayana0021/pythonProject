from django.urls import path
from .views import (
    index,
    product_detail,
    all,
    jjim_page,
    jjim,
    seller,
    product_list,
    notice,
    jjim_delete,
    jjim_check,
    search,
)


app_name = "coffee"

urlpatterns = [
    # http://127.0.0.1:8000/coffee
    path("", index, name="index"),
    # http://127.0.0.1:8000/coffee/1    상세조회
    path("<int:pid>/", product_detail, name="product_detail"),
    # http://127.0.0.1:8000/coffee/all
    path("all/", all, name="all"),
    # http://127.0.0.1:8000/user/jjim
    path("jjim/", jjim_page, name="jjim_page"),
    # http://127.0.0.1:8000/coffee/jjim/1
    path("jjim/<int:pid>/", jjim, name="jjim"),
    # http://127.0.0.1:8000/coffee/jjim/delete/1
    path("jjim/delete/<int:pid>/", jjim_delete, name="jjim_delete"),
    # http://127.0.0.1:8000/coffee/jjim/check/1
    path("jjim/check/<int:pid>/", jjim_check, name="jjim_check"),
    # http://127.0.0.1:8000/coffee/seller
    path("seller/", seller, name="seller"),
    # 내브바 탭하면 페이지 이동
    path("products/<str:tab>", product_list, name="product_list"),
    # 공지사항 페이지 이동
    # http://127.0.0.1:8000/coffee/notice
    path("notice/", notice, name="notice"),
    # 검색 이동
    # http://127.0.0.1:8000/coffee/search
    path("search/", search, name="search"),
]
