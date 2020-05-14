from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
"""
表名由Django自动生成，默认格式为“应用+下划线+小写类名”，你可以重写这个规则。
Django默认自动创建自增主键id，当然，你也可以自己指定主键。
"""


class Question(models.Model):  # 默认表名是polls_question
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):  # 默认表名是polls_choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
