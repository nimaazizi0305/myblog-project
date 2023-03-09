from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from myblog.models import Posts,categories
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# def home(request:HttpRequest):
#     # when we want get all pots of the one user
#     # user.post_set.all
#     # then we don't need save
#     posts=Posts.objects.all()
#
#     context={
#         "posts":posts
#     }
#     return render(request,"myblog/home.html",context)

class PostView(ListView):
    model = Posts
    template_name = "myblog/home.html"
    context_object_name = "posts"
    ordering = ("-created")
    paginate_by = 2


class UserPostListView(ListView):
    model = Posts
    template_name = "myblog/user_post.html"
    context_object_name = "posts"
    ordering = ("-created")
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(auth=user).order_by('-created')


class DetialViewPost(DetailView):
    model = Posts
    template_name = "myblog/detial.html"

class PostCreateView(CreateView):
    model = Posts
    fields = ['title', 'category',"text"]
    template_name = "myblog/createpost.html"

    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Posts
    fields = ['title',"category" ,'text']
    template_name = "myblog/updatepost.html"

    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auth:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = "myblog/deletepost.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auth:
            return True
        return False

def about(request:HttpRequest):
    context={

    }
    return render(request,"myblog/about.html",context)







