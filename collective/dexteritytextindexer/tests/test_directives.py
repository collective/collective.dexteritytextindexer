from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from collective.dexteritytextindexer.directives import searchable
from grokcore.component.testing import grok, grok_component
from plone.directives import form
from zope import schema
from zope.interface import Interface
import unittest
import zope.component.testing


class TestDirectives(unittest.TestCase):

    def setUp(self):
        grok('collective.dexteritytextindexer.meta')

    def tearDown(self):
        zope.component.testing.tearDown()

    def test_schema_directives_store_tagged_values(self):

        class IDummy(form.Schema):
            searchable('foo')
            foo = schema.TextLine(title=u'Foo')

        self.assertEquals(None, IDummy.queryTaggedValue(SEARCHABLE_KEY))

        grok_component('IDummy', IDummy)

        self.assertEquals([(Interface, 'foo', 'true')],
                          IDummy.queryTaggedValue(SEARCHABLE_KEY))
