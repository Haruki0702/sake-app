from django.db import models

from bs4 import BeautifulSoup

class Sake(models.Model):
    SCORE_CHOICES=[
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****"),
    ]
    title=models.CharField("銘柄", max_length=200)
    brewery=models.CharField("酒蔵", max_length=200, blank=True)
    score=models.IntegerField("評価", choices=SCORE_CHOICES, default=3)
    tasting_date=models.DateField("飲んだ日")
    image=models.ImageField("ラベル画像", upload_to="images/", blank=True, null=True)
    memo=models.TextField("メモ", blank=True)
    created_at=models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.title
