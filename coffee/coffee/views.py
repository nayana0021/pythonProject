from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# from crawl.crawl import coffee_crawl


# 원본
def index(request):
    # coffee_crawl()
    products = Product.objects.all()

    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌

    paginator = Paginator(products, 12)
    # paginator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {
        "products": page_obj,
        "page": page,
        # "keyword": keyword,
        # "sort": sort,
    }

    return render(request, "coffee/index.html", context=context)


def product_detail(request, pid):
    product = get_object_or_404(Product, id=pid)

    # 좋아요 여부
    # is_liked = False
    # # 로그인 사용자가 게시물에 좋아요 표시를 했다면
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True

    # context = {"post": post, "is_liked": is_liked}
    context = {"product": product}

    return render(request, "coffee/detail.html", context)


def all(request):
    products = Product.objects.all()

    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌

    paginator = Paginator(products, 12)
    # paginator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {
        "products": page_obj,
        "page": page,
    }

    return render(request, "coffee/all.html", context=context)


def product_list(request, tab):
    if tab == "원두커피":
        prod = Product.objects.filter(category=1)
    elif tab == "캡슐커피":
        prod = Product.objects.filter(category=2)
    elif tab == "커피용품":
        prod = Product.objects.filter(category__in=[3, 4])
    elif tab == "전체상품":
        prod = Product.objects.all()

    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌
    paginator = Paginator(prod, 12)
    page_obj = paginator.get_page(page)
    context = {
        "products": page_obj,
        "page": page,
        "prod": prod,
        "current_tab": tab,
    }

    return render(request, "coffee/all.html", context=context)


# @login_required(login_url="user:login")
# def jjim(request):
#     # jjim = get_object_or_404(Product)
#     products = Product.objects.all()

#     check_jjim = products.jjim.filter(id=request.user.id).exists()

#     is_jjimed_change = False
#     if check_jjim:
#         products.jjim.remove(request.user)
#     else:
#         products.jjim.add(request.user)
#         is_jjimed_change = True
#     return JsonResponse({"likes": products.jjim.count(), "is_jjimed": is_jjimed_change})


@login_required(login_url="user:login")
def jjim(request, pid):
    product = get_object_or_404(Product, id=pid)

    if product.jjim.filter(id=request.user.id).exists():
        product.jjim.remove(request.user)
        is_jjimed_change = False
    else:
        product.jjim.add(request.user)
        is_jjimed_change = True

    return JsonResponse({"likes": product.jjim.count(), "is_jjimed": is_jjimed_change})


@login_required(login_url="user:login")
def jjim_page(request):
    return render(request, "users/jjim.html")


# 찜 삭제 함수
@login_required(login_url="user:login")
def jjim_delete(request, pid):
    product = get_object_or_404(Product, id=pid)

    if product.jjim.filter(id=request.user.id).exists():
        product.jjim.remove(request.user)
        is_jjimed_change = True  # 찜이 삭제되었음을 표시
    else:
        return HttpResponseBadRequest("찜이 이미 삭제되었거나 존재하지 않습니다.")

    return JsonResponse({"is_jjimed": is_jjimed_change})


# # 전체페이지 db에 찜이 되어있는지 확인하는 함수
# @login_required(login_url="user:login")
# def all_jjim_check(request, pid):
#     # 로그인한 사용자 확인
#     if not request.user.is_authenticated:
#         return JsonResponse({"error": "로그인이 필요합니다."}, status=401)

#     product = get_object_or_404(Product, id=pid)


# 상세페이지 db에 찜이 되어있는지 확인하는 함수
@login_required(login_url="user:login")
def jjim_check(request, pid):
    # 로그인한 사용자 확인
    if not request.user.is_authenticated:
        return JsonResponse({"error": "로그인이 필요합니다."}, status=401)

    product = get_object_or_404(Product, id=pid)

    # 해당 제품에 대해 현재 로그인한 사용자가 찜했는지 여부 확인
    is_jjimed = product.jjim.filter(id=request.user.id).exists()

    return JsonResponse({"is_jjimed": is_jjimed})


def seller(request):
    return render(request, "coffee/seller_info.html")


def notice(request):
    return render(request, "coffee/notice.html")


# 검색기능
def search(request):
    keyword = request.GET.get("keyword", "")
    search_list = Product.objects.order_by("id")

    if keyword:
        search_list = search_list.filter(
            Q(name__icontains=keyword)
            | Q(description__icontains=keyword)
            | Q(price__icontains=keyword)
        ).distinct()

    paginator = Paginator(search_list, 5)
    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌
    # paginator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {
        "search_list": page_obj,
        # "products": page_obj,
        "keyword": keyword,
        # "page": page,
    }

    return render(request, "coffee/search.html", context)
