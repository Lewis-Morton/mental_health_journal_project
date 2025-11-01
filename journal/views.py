from django.shortcuts import render
from rest_framework import generics
from.models import JournalEntry
from.serializers import JournalEntrySerializer

# Create your views here.
# Views for journalentry model
# These views handle CRUD operations on journal entries
class JournalCreateAPIView(generics.CreateAPIView):
    queryset = JournalEntry.objects(all)
    serializer_class = JournalEntrySerializer

class JournalDetailAPIView(generics.RetrieveAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalUpdateAPIView(generics.UpdateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalDestroyAPIView(generics.DestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer


