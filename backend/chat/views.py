from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import status, permissions

class ChatRoomListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if ChatRoom.objects.filter(name=name).exists():
            return Response({'error': 'Chat room already exists'}, status=status.HTTP_400_BAD_REQUEST)

        chatroom = ChatRoom.objects.create(name=name, created_by=request.user)
        serializer = self.get_serializer(chatroom)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(chatroom_id=room_id).order_by('timestamp')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class MessageCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, room_id):
        try:
            chatroom = ChatRoom.objects.get(id=room_id)
        except ChatRoom.DoesNotExist:
            return Response({"error": "Chatroom not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user, chatroom=chatroom)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(chatroom_id=room_id).order_by('timestamp')

    def perform_create(self, serializer):
        room_id = self.kwargs['room_id']
        chatroom = ChatRoom.objects.get(id=room_id)
        serializer.save(chatroom=chatroom)

class ActiveUserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Example: Return list of active users (You can replace this logic)
        active_users = ["user1", "user2", "user3"]
        return Response({"active_users": active_users})