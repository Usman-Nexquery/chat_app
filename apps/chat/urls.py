from django.urls import path

from .views import get_message_history, GetOrCreateChatRoom

urlpatterns = [
   # path('history/', get_message_history(), name='history'),
    path('room/', GetOrCreateChatRoom.as_view(), name='get_or_create_chat_room'),
]
