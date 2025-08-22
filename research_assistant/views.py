from rest_framework import generics
from .models import ResearchAssistant
from .serializers import ResearchAssistantSerializer

class ResearchAssistantListCreateView(generics.ListCreateAPIView):
    queryset = ResearchAssistant.objects.all()
    serializer_class = ResearchAssistantSerializer

class ResearchAssistantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResearchAssistant.objects.all()
    serializer_class = ResearchAssistantSerializer
