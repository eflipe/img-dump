from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
