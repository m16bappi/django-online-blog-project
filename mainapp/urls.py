from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="blog-home"),
    path('details/<int:pk>/', views.PostDetailsView.as_view(), name="post-details"),
    path('createPost/', views.PostCreateView.as_view(), name="post-create"),
    path('postUpdate/<int:pk>/', views.PostUpdateView.as_view(), name="post-update"),
    path('postDelete/<int:pk>/', views.PostDeleteView.as_view(), name="post-delete"),
    path('userPost/<str:username>/', views.UserPostView.as_view(), name="user-post"),
]