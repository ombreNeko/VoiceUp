from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from tweets.models import Tweet
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)
from tweets.forms import TweetModelForm
from tweets.mixins import FormUserNeededMixin,UserOwnerMixin
from django.urls import reverse_lazy


# Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create'
    # login_url = '/admin/'
    

# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)

#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.user = request.user
#         instance.save()

#     context = {
#         "form": form
#     }
#     return(request,'tweets/create_view.html', context)




# Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'



# Delete
class TweetDeleteView(DeleteView,LoginRequiredMixin):
    model = Tweet
    success_url = reverse_lazy('home')
    template_name = 'tweets/delete_confirm.html'


# Retreive 
class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs) :
        context = super(TweetListView, self).get_context_data(*args,**kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context




# def tweet_detail_view(request, id = 1):
#     obj = Tweet.objects.get(id=id) #Get from database
#     print(obj)
#     context = {
#         "object" : obj
#     }
#     return render(request,"tweets/detail_view.html", context)


# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)

#     for obj in queryset:
#         print(obj.content)

#     context = {
#         "object_list": queryset
#     }
#     return render(request,"tweets/list_view.html", context)
