from django.core.exceptions import ValidationError
from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from apps.badges.models import Badge
from apps.quests.models import Quest, Response, in_range


class QuestList(ListView):
    model = Quest
    class Meta:
        pass


class QuestDetail(DetailView):
    model = Quest
    class Meta:
        pass
def check_badge(user):
    if user.quest_set.count()==1:
        return "first"
    if user.quest_set.count()==5:
        return "five"
    return None
def make_badge(toggle):
    if not toggle:
        return
    badge ,created = Badge.objects.get_or_create(name=toggle,description=toggle)
    if True:
        with open('common/static/common/' + toggle + '.svg', 'rb') as doc_file:
            badge.thumbnail.save(toggle + ".svg", File(doc_file), save=True)
        badge.save()
    return badge
class ResponseCreate(CreateView):
    model = Response
    fields = ["quest", "lat", "lng"]
    class Meta:
        pass

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            resp = form.save(commit=False)
            resp.user = self.request.user
            if(in_range((resp.lat, resp.lng), (resp.quest.lat, resp.quest.lng), resp.quest.precision)):
                resp.save()
                # super(ResponseCreate, self).form_valid(form)
                badge=make_badge(check_badge(self.request.user))
                if badge:
                    self.request.user.badge_set.add(badge)
                return JsonResponse({"status":0,"message":"Good job!"})
            else:
                return JsonResponse({"status":2,"message":"Sorry, wrong location"})
        else:
            return JsonResponse({"status":1,"message":"Login bitch !"})
