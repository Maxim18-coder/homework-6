from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator', 'created_at', 'updated_at')
    list_filter = ('status', 'creator')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

admin.site.register(Advertisement, AdvertisementAdmin)