from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializers

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
