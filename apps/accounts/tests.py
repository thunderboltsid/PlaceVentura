# -*- coding: utf-8 -*-
from django.test import Client

import pytest

from apps.accounts.factories import AccountFactory

__author__ = 'Sebastian Wozny'
import logging

from django.core.urlresolvers import reverse_lazy
# Get an instance of a logger
logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_user_list_accessible():
    obj = AccountFactory()
    url = reverse_lazy('account-list')
    c = Client()
    response = c.get(url)
    assert response.status_code == 200, "User List was unreachable"


@pytest.mark.django_db
def test_user_list_contains_objects():
    obj = AccountFactory()
    obj = AccountFactory()
    url = reverse_lazy('account-list')
    c = Client()
    response = c.get(url)
    # there is an anon user so thats why its 3
    assert len(response.context["object_list"]) == 3, "User List contains incorrect amount of users"


@pytest.mark.django_db
def test_user_detail_accessible():
    obj = AccountFactory()
    url = reverse_lazy('account-detail', kwargs={"pk": obj.id})
    c = Client()
    response = c.get(url)
    assert response.status_code == 200, "User detail was unreachable"
