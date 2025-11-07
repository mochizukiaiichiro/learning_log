from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ユーザーが学んでいるトピックを表す"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    """モデルの文字列表現を返す"""

    def __str__(self):
        return self.text


class Entry(models.Model):
    """トピックに関して学んだ具体的なこと"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    """モデルの文字列表現を返す"""

    def __str__(self):
        return f'{self.text[:25]}...'
