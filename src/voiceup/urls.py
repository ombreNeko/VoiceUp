from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from voiceup.views import home
from tweets.views import TweetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name= "home"),
    path('tweet/', include('tweets.urls', namespace= 'tweet')),
    path('api/tweet/', include('tweets.api.urls', namespace= 'tweet-api'))

]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))
