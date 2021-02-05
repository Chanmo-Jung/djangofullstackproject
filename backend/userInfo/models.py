#backend/post/models.py 모델 정의
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class userInfo(models.Model):
#     # id =models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phonenum = models.CharField(max_length=11, unique=True)
#     # email = models.CharField(max_length=100, unique=True)
#     # password = models.CharField(max_length=20)
#     # name = models.CharField(max_length=10)
#     # nickname = models.CharField(max_length=20, unique=True) # 문자 자료형 필드 표현
#     # created_at = models.DateTimeField('Create Time', default=datetime.datetime.now) # 날짜와 시간 자료형 필드 표현
#     # # content = models.TextField()
#
# @receiver(post_save, sender=User)
# def create_user_userInfo(sender, instance, created, **kwargs):
#     if created:
#         userInfo.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_userInfo(sender, instance, **kwargs):
#     instance.userInfo.save()

