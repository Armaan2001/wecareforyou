from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('', include('core.urls')),
    path('blog/', include('Blog.urls')),
    path('confessions/', include('Confession.urls')),
    path('accounts/', include('allauth.urls')),
    path('about/', views.about)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)