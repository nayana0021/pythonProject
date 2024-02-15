from django.urls import path

from .views import notice_list, notice_row, notice_create, notice_update, notice_delete


app_name = "notice"

urlpatterns = [
    # http://127.0.0.1:8000/notice
    path("", notice_list, name="notice_list"),
    # http://127.0.0.1:8000/notice/1
    path("<int:id>/", notice_row, name="notice_row"),
    # http://127.0.0.1:8000/notice/create
    path("create/", notice_create, name="notice_create"),
    # http://127.0.0.1:8000/notice/update
    path("update/<int:id>/", notice_update, name="notice_update"),
    # http://127.0.0.1:8000/notice/delete/1
    path("delete/<int:id>/", notice_delete, name="notice_delete"),
]
