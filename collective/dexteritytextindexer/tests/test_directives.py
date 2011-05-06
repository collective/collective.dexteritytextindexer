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

    def test_inherited_schema_still_has_tagged_value(self):
        """An inherited schema should still have the tagged value information
        inherited from its superclass.
        """

        class IFoo(form.Schema):
            """Class with a searchable field
            """
            searchable('baz')
            baz = schema.TextLine(title=u'baz')

        class IBar(IFoo):
            """Schema class which inherits a field from IFoo.
            """

        self.assertEquals(None, IFoo.queryTaggedValue(SEARCHABLE_KEY))
        self.assertEquals(None, IBar.queryTaggedValue(SEARCHABLE_KEY))

        grok_component('IFoo', IFoo)
        grok_component('IBar', IBar)

        self.assertEquals([(Interface, 'baz', 'true')],
                          IFoo.queryTaggedValue(SEARCHABLE_KEY))
        self.assertEquals([(Interface, 'baz', 'true')],
                          IBar.queryTaggedValue(SEARCHABLE_KEY))
