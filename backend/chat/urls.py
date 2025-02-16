from django.urls import path
from .views import ChatRoomListCreateView, MessageListView,MessageCreateView,ActiveUserListView

urlpatterns = [
    path('chatrooms/', ChatRoomListCreateView.as_view(), name='chatroom-list-create'),
    path('chatrooms/<int:room_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('chatrooms/<int:room_id>/messages/create/', MessageCreateView.as_view(), name='message-create'),
    path("api/active-users/<str:room_name>/", ActiveUserListView.as_view(), name="active_users"),
]
