from .models import Notice
from django import forms

"""
django - 화면 디자인 처리
1. html : 일반적인 처리(bootstrap 이용, 직접 디자인)
2. 장고의 form 클래스 이용
    forms.ModelForm, forms.Form 클래스를 상속받고 작성
"""


class NoticeForm(forms.ModelForm):
    class Meta:  # 어느 테이블과 연동된건지 알려주고
        model = Notice
        fields = ["title", "contents", "image", "category"]  # 보여줄 필드 지정
