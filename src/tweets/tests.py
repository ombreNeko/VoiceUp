from django.test import TestCase
from tweets.models import Tweet
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self): #setup an object itself (optional)
        some_user = User.objects.create(username = 'somya')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        self.assertTrue(obj.content == 'Some random content')
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)  #assertTrue is essentially the same as assertEqual

    def test_tweet_url(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        absolute_url = reverse("tweet:detail", kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url) 