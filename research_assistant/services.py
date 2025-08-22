from .models import ResearchAssistant
from department.models import Department


def create_research_assistant(data):
    """Service to create a new Research Assistant"""
    return ResearchAssistant.objects.create(**data)

def get_all_research_assistants():
    """Service to fetch all Research Assistants"""
    return ResearchAssistant.objects.all()

def get_research_assistant_by_id(assistant_id):
    """Service to fetch one Research Assistant"""
    return ResearchAssistant.objects.get(id=assistant_id)
