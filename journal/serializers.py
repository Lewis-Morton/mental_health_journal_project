from rest_framework import serializers
from.models import User, JournalEntry, Conversation, Participant, ChatMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        field = '__all__'

class ConversationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        field = '__all__'

class ParticipantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        field = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        field = '__all__'
    
