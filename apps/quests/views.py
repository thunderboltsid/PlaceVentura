from django.views.generic import ListView, DetailView, CreateView
from apps.quests.models import Quest, Response


class QuestList(ListView):
    model = Quest
    class Meta:
        pass


class QuestDetail(DetailView):
    model = Quest
    class Meta:
        pass

class ResponseCreate(CreateView):
    model = Response
    fields = ["user", "quest", "lat", "lng"]
    class Meta:
        pass