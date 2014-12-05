from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from hacku.models import *

class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 0    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]

admin.site.register(Question,QuestionAdmin)