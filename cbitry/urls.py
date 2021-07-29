from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_view


from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='cbitry-home'),
    path('', views.feed, name='cbitry-feed'),
    path('profile/', views.profile,name='cbitry-profile'),
    path('signup/', views.signup,name='cbitry-register'),
   
    path('Newsfeed/', PostListView.as_view(), name='cbitry-feed'),
    path('trending/', views.trending, name='cbitry-trending'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(extra_context={'title':'New Post'}), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('logout/', auth_view.LogoutView.as_view(template_name='cbitry/logout.html'),name='logout'),
    path('deactivate/', views.delete_user, name='cbitry-delete'),
    path('likes/',views.postlike,name='cbitry-like'),
    path('dashboard/', views.dashboard, name='cbitry-dashboard'),
    path('comment/<int:id>', views.deletecomment, name='cbitry-comment'),
    path('filtered/', views.filter_list, name='cbitry-filter'),
    path('deactivate/confirm/', views.delete_user_confirm, name='cbitry-delete-confirm'),
    url(r'(?P<id>\d+)/saved/$',views.favorite,name='cbitry-favorite'),
    path('bookmark/', views.favorite_list, name='cbitry-bookmark'),
    path('docx/', views.document, name='cbitry-docx'),
]
