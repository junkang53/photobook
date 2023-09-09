from django.db import models

# Create your models here.
# 앱의 데이터를 다루는 부분
# 데이터베이스에 저장될 데이터의 모양을 정의하고 관련된 일부 기능들을 설정해주는 영역이다
# 모델을 데이터베이스에 적용(migration) 시키면 그게 테이블이 되는 것임

class Photo(models.Model):
    title = models.CharField(max_length=50) # 문자열(길이 제한 둘수있음)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField() # 문자열(길이 제한 필요 없음)
    price = models.IntegerField() # 정수

 