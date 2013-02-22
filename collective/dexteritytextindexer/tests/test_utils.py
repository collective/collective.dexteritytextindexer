from collective.dexteritytextindexer.tests.helpers import get_searchable_fields
from collective.dexteritytextindexer.utils import searchable
from plone.directives import form
from unittest2 import TestCase
from zope import schema


class IExample(form.Schema):

    foo = schema.TextLine(title=u'foo')


class IBar(form.Schema):
    pass


class IBaz(form.Schema):
    baz = schema.TextLine(title=u'baz')


class TestUtils(TestCase):
    """Test utils module.
    """

    def test_marking_field_as_searchable(self):
        self.assertEquals(get_searchable_fields(IExample), [])
        searchable(IExample, u'foo')
        self.assertEquals(get_searchable_fields(IExample), ['foo'])

    def test_break_when_field_does_not_exist(self):
        with self.assertRaises(AttributeError) as cm:
            searchable(IBar, u'foo')

        self.assertEqual(
            str(cm.exception),
            'collective.dexteritytextindexer.tests.test_utils.IBar'
            ' has no field "foo"')
