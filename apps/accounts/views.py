from django.views.generic import DetailView, ListView

from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


class AccountList(ListView):
    model = Account


class AccountDetail(DetailView):
    model = Account
