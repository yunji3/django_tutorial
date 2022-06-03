from django.db import models

# Create your models here.

class Article(models.Model): #상속
    title = models.CharField(max_length=10) #용량을 줄이기 위해선 짧은건 CharField로
    content = models.TextField() # 많은 양을 쓸때 , 자주쓰면 용량차지 많이함.
    created_at = models.DateTimeField(auto_now_add=True)


