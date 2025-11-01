from django.shortcuts import render
from rest_framework import generics
from.models import JournalEntry
from.serializers import JournalEntrySerializer

# Create your views here.

class JournalDetailAPIView(generics.RetrieveAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

