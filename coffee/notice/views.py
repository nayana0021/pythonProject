from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice, NoticeCount
from tools.utils import get_client_ip
from .forms import NoticeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def notice_row(request, id):
    # 공지사항 한 개 조회
    notice = get_object_or_404(Notice, id=id)

    # 조회수 증가
    # client ip 가져오기
    ip = get_client_ip(request)

    cnt = NoticeCount.objects.filter(ip=ip, notice=notice).count()

    if cnt == 0:
        # QuestionCount 테이블에 ip 와 question 추가
        qc = NoticeCount(ip=ip, notice=notice)
        qc.save()
        # Question 테이블에 조회수 증가
        if notice.view_count:
            notice.view_count += 1
        else:
            notice.view_count = 1
        notice.save()

    return render(request, "notice/detail.html", {"notice": notice})


def notice_list(request):
    # 전체 공지사항 가져오기
    list = Notice.objects.all().order_by("-id")

    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌

    paginator = Paginator(list, 12)
    # paginator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {
        # "list": list,
        "page": page,
        "list": page_obj,
    }

    return render(request, "notice/notice.html", context=context)


@login_required(login_url="users:login")
def notice_create(request):
    if request.method == "POST":
        # request.FILES : file 정보 따로 가져오기( 폼으로 가져올 수 없다 : post로..)
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # user 정보가 없음 일단 False
            post.writer = request.user
            post.save()
            return redirect("notice:notice_list")
    else:
        form = NoticeForm()

    return render(request, "notice/create.html", {"form": form})


@login_required(login_url="users:login")
def notice_update(request, id):
    notice = get_object_or_404(Notice, id=id)

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect("notice:notice_row", notice.id)
    else:
        form = NoticeForm(instance=notice)

    return render(request, "notice/update.html", {"form": form})


@login_required(login_url="users:login")
def notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect("notice:notice_list")
