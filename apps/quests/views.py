from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, CreateView
from apps.quests.models import Quest, Response, in_range


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

    def form_valid(self, form):
        resp = form.save(commit=False)
        if(in_range((resp.lat, resp.lng), (resp.quest.lat, resp.quest.lng), resp.quest.precision)):
            return super(ResponseCreate, self).form_valid(form)
        else:
            raise ValidationError("Sorry, you're not in the right location!")
