from django.urls import path, include
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path('base1/', views.base1, name="base1"),
    path('chats/', views.chats, name="chats"),
    path("search/", views.search, name="search"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
]
