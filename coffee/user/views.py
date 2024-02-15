from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                # 인증 실패 시 form 에러 메시지 추가
                form.add_error(None, "아이디 또는 패스워드가 올바르지 않습니다.")
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})
