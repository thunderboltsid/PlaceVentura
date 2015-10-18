from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect
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
        if self.request.user.is_authenticated:
            resp = form.save(commit=False)
            if(in_range((resp.lat, resp.lng), (resp.quest.lat, resp.quest.lng), resp.quest.precision)):
                resp.save(commit=True)
                # super(ResponseCreate, self).form_valid(form)
                return JsonResponse({"status":0,"message":"Good job!"})
            else:
                return JsonResponse({"status":2,"message":"Sorry, wrong location"})
        else:
            return JsonResponse({"status":1,"message":"Login bitch !"})
