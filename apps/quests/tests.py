# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.test import Client

import pytest
from apps.quests.factories import QuestFactory

__author__ = 'Sebastian Wozny'
import logging
import models

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
    assert len(response.context["object_list"])==2, "Quest List contains incorrect amount of badges"
@pytest.mark.django_db
def test_quest_detail_accessible():
    obj=QuestFactory()
    url = reverse_lazy('quest-detail',kwargs={"pk":obj.id})
    c=Client()
    response=c.get(url)
    assert response.status_code==200, "Quest detail was unreachable"


def test_in_range():
    data = [
        ((53.170389, 8.645187), (53.169071, 8.642344), 300, True),
        ((53.166739, 8.637598), (53.165079, 8.644067), 400, False),
        ((53.194558, 8.615379), (53.201110, 8.601758), 1000, False)
    ]

    for item in data:
        assert models.in_range(item[0],item[1],item[2]) == item[3], "In range fails"
