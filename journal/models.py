from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(max_length=20)
    username = models.CharField(max_length=30)
    email = models.CharField(maxlength=80)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

class JournalEntry(models.Model):
    mood_choices = [('Content', 'Melancholy', 'Enthusiastic', 'Sorrowful')]

    id = models.IntegerField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField(max_length=5000)
    mood = models.CharField(max_length=20, choices=mood_choices)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class ChatMessage(models.Model):
    id = models.IntegerField(max_length=20)
    sender = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    recipient = models.ForeignKey(JournalEntry, on_delete=models.CASCADE )
    text = models.CharField(max_length=2000)
    timestamp = models.TimeField()
    room_id = models.IntegerField(max_length=20)