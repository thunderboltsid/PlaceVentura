from django.views.generic import ListView, DetailView
from apps.quests.models import Quest


class QuestList(ListView):
    model = Quest
    class Meta:
        pass


class QuestDetail(DetailView):
    model = Quest
    class Meta:
        pass