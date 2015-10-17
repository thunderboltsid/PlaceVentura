from apps.badges.models import Badge

__author__ = 'siddharthshukla'

from django.views.generic import DetailView, ListView
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class BadgeList(ListView):
    model = Badge
    class Meta:
        pass

class BadgeDetail(DetailView):
    model = Badge
    class Meta:
        pass


