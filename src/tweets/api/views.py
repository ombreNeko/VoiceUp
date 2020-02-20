from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by("-time_stamp")
        print(self.request.GET)
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query) 
            )    
            print("in view")
        return qs

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

