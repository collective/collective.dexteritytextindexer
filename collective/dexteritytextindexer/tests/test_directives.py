"""Contains martian directive tests.
"""

from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from collective.dexteritytextindexer.directives import searchable
from grokcore.component.testing import grok, grok_component
from plone.directives import form
from zope import schema
from zope.interface import Interface
import unittest
import zope.component.testing


class TestDirectives(unittest.TestCase):
    """Test suite for testing the martian directive.
    """

    def setUp(self):
        """After setting up, grok the meta module for enabling the
        grokker.
        """
        grok('collective.dexteritytextindexer.meta')

    def tearDown(self):
        """Tear down the testing setup.
        """
        zope.component.testing.tearDown()

    def test_schema_directives_store_tagged_values(self):
        """Test, if the schema directive values are stored as tagged
        values.
        """

        class IDummy(form.Schema):
            """Dummy schema class.
            """
            searchable('foo')
            foo = schema.TextLine(title=u'Foo')

        self.assertEquals(None, IDummy.queryTaggedValue(SEARCHABLE_KEY))

        grok_component('IDummy', IDummy)

        self.assertEquals([(Interface, 'foo', 'true')],
                          IDummy.queryTaggedValue(SEARCHABLE_KEY))
