from rest_framework import serializers
from .models import ChatRoom, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ChatRoomSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(write_only=True)  # Accept username as input

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'created_by']

    def create(self, validated_data):
        username = validated_data.pop('created_by')  # Get username
        user = User.objects.get(username=username)   # Fetch user object
        chat_room = ChatRoom.objects.create(created_by=user, **validated_data)
        return chat_room

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id','chatroom', 'sender', 'content', 'timestamp']
        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
