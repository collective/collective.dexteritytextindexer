# -*- coding: utf-8 -*-
"""Contains different behaviors needed for testing.
"""
from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ISimpleBehavior(model.Schema):
    """Simple behavior containing simple text line fields.
    """

    dexteritytextindexer.searchable('foo')
    foo = schema.TextLine(title=u'Foo')

    bar = schema.TextLine(title=u'Bar')


@provider(IFormFieldProvider)
class IListBehavior(model.Schema):
    """More advanced behavior with a list of fields.
    """

    dexteritytextindexer.searchable('list_field')

    list_field = schema.List(
        title=u'List field',
        value_type=schema.TextLine()
    )


@provider(IFormFieldProvider)
class IIntBehavior(model.Schema):
    """Basic behavior with a integer field.
    """

    dexteritytextindexer.searchable('int_field')
    int_field = schema.Int(title=u'Int')


@provider(IFormFieldProvider)
class IInheritedBehavior(ISimpleBehavior):
    """Behavior extending from ISimpleBehavior for testing inheritance.
    """


@provider(IFormFieldProvider)
class IMissingFieldBehavior(model.Schema):
    """A behavior defining a field as searchable which does not exist.
    """

    dexteritytextindexer.searchable('foo')
    foo = schema.TextLine(title=u'Foo')

    dexteritytextindexer.searchable('bar')
