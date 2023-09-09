from django.contrib import admin
from .models import Photo
# 우리가 작성한 models에서 Photo 클래스를 불러와라 

# Register your models here.
admin.site.register(Photo) # admin 페이지에 모델 등록


