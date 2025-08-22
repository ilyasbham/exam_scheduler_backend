from django.urls import path
from .views import ResearchAssistantListCreateView, ResearchAssistantDetailView

urlpatterns = [
    path('assistants/', ResearchAssistantListCreateView.as_view(), name='ra-list-create'),
    path('assistants/<int:pk>/', ResearchAssistantDetailView.as_view(), name='ra-detail'),
]
