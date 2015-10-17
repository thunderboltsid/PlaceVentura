# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.test import Client

import pytest
from apps.quests.factories import QuestFactory

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_quest_has_attrs():
    obj=QuestFactory()
    assert hasattr(obj,"lng")
    assert hasattr(obj,"lat")
    assert hasattr(obj,"type")
    assert hasattr(obj,"precision")

@pytest.mark.django_db
def test_quest_list_accessible():
    obj=QuestFactory()
    url = reverse_lazy('quest-list')
    c=Client()
    response=c.get(url)
    assert response.status_code==200, "Quest List was unreachable"
@pytest.mark.django_db
def test_quest_list_contains_objects():
    obj=QuestFactory()
    obj=QuestFactory()
    url = reverse_lazy('quest-list')
    c=Client()
    response=c.get(url)
    assert len(response.context["object_list"])==2, "Quest List contains incorrect amount of quests"
@pytest.mark.django_db
def test_quest_detail_accessible():
    obj=QuestFactory()
    url = reverse_lazy('quest-detail',kwargs={"pk":obj.id})
    c=Client()
    response=c.get(url)
    assert response.status_code==200, "Quest detail was unreachable"
