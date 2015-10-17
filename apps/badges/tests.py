import pytest
from apps.badges.factories import BadgeFactory

__author__ = 'swozn'
@pytest.mark.django_db
def test_badges_work():
    obj=BadgeFactory()
