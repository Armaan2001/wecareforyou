from django.contrib import admin
from Blog.models import BlogPost, Images

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

  
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Images)
