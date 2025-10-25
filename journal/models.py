from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

class JournalEntry(models.Model):
    MOOD_CHOICES = [('content', 'Content'),
                     ('melancholy', 'Melancholy'), 
                     ('sorrowful', 'Sorrowful'),
                     ('grateful', 'Grateful'),
                     ('energetic', 'Energetic'),
                     ('positive', 'Positive'),
                     ('motivated', 'Motivated'),
                     ('tired', 'Tired'),
                     ('depressive', 'Depressive')]

    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField(max_length=5000)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class ChatMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='received_messages')
    text = models.CharField(max_length=2000)
    timestamp = models.TimeField()
    room_id = models.IntegerField()