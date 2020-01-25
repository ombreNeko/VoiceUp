from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from voiceup.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('tweet/', include('tweets.urls', namespace= 'tweet'))
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))
