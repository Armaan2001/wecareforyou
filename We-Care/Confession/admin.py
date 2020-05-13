from django.contrib import admin
from Confession.models import ConfessionPost

class ConfessionPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

  
admin.site.register(ConfessionPost, ConfessionPostAdmin)
