from django.contrib import admin
from tweets.models import Tweet
from tweets.forms import TweetModelForm

# Register your models here.
# admin.site.register(Tweet) 

class TweetModelAdmin(admin.ModelAdmin):
        # form = TweetModelForm
        class Meta:
                model = Tweet

admin.site.register(Tweet, TweetModelAdmin)