from django.urls import path
from . import views
from .views import PostView, DetialViewPost,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns=[
    path("",PostView.as_view(),name="home"),
    path("posts/<str:username>", UserPostListView.as_view(), name="userpost"),
    path("detial/<int:pk>", DetialViewPost.as_view(), name="detial"),
    path("new-post", PostCreateView.as_view(), name="createpost"),
    path("update-post/<int:pk>", PostUpdateView.as_view(), name="updatepost"),
    path("delete-post/<int:pk>", PostDeleteView.as_view(), name="deletepost"),
    path("about", views.about, name="about"),
]