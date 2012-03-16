from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from collective.dexteritytextindexer.utils import searchable
from plone.directives import form
from plone.supermodel.utils import mergedTaggedValueList
from unittest2 import TestCase
from zope import schema


class IExample(form.Schema):

    foo = schema.TextLine(title=u'foo')


class TestUtils(TestCase):
    """Test utils module.
    """

    def test_marking_field_as_searchable(self):
        self.assertEquals([], mergedTaggedValueList(IExample, SEARCHABLE_KEY))

        searchable(IExample, u'foo')
        self.assertEquals([(IExample, 'foo', 'true')],
                          mergedTaggedValueList(IExample, SEARCHABLE_KEY))
