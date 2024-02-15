from django.db import models
from django.contrib.auth.models import User


# id, category,title, writer, contents, created_at, view_count, image
class Notice(models.Model):
    NOTICE_CAT = [(1, "일반"), (2, "배송"), (3, "상품"), (4, "이벤트")]
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    created_at = models.DateTimeField(
        auto_now=True,
    )
    category = models.SmallIntegerField(choices=NOTICE_CAT, default=1)
    view_count = models.IntegerField(default=0)


class NoticeCount(models.Model):
    """
    조회수 업데이트를 위한 모델
    사용자의 ip 저장
    """

    ip = models.CharField(max_length=30)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ip
