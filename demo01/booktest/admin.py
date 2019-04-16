from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
'''
通过少量代码拥有一个强大的后台
'''

admin.site.register(BookInfo)
admin.site.register(HeroInfo)