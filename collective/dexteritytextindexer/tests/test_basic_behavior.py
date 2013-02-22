from collective.dexteritytextindexer.tests.helpers import get_searchable_fields
from plone.app.dexterity.behaviors.metadata import IBasic
from unittest2 import TestCase


class TestBasicBehaviorIsSearchable(TestCase):

    def test_title_is_searchable(self):
        self.assertIn('title', get_searchable_fields(IBasic))

    def test_description_is_searchable(self):
        self.assertIn('description', get_searchable_fields(IBasic))
