from django.contrib import admin
from diary.models import DiaryPost

@admin.register(DiaryPost)
class DiaryPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'created_at', 'owner')
    list_filter = ('title', 'created_at', 'owner')
