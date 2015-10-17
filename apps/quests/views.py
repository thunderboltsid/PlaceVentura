from django.views.generic import ListView
from apps.quests.models import Quest


class QuestList(ListView):
    model = Quest
    class Meta:
        pass
