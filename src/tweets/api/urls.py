from django.urls import path
from django.views.generic import RedirectView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView
)
app_name = 'tweet'

urlpatterns = [
    # path('', RedirectView.as_view(url = "/")),
    path('', TweetListAPIView.as_view(), name = 'list'),
    # path('<int:pk>/', TweetDetailView.as_view(), name = 'detail'),
    path('create/', TweetCreateAPIView.as_view(), name = 'create'),
    # path('<int:pk>/update/', TweetUpdateView.as_view(), name = 'update'),
    # path('<int:pk>/delete/', TweetDeleteView.as_view(), name = 'delete'),

]


