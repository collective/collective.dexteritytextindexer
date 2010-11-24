from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from zope import schema
from zope.interface import alsoProvides


class ISimpleBehavior(form.Schema):

    dexteritytextindexer.searchable('foo')
    foo = schema.TextLine(title=u'Foo')

    bar = schema.TextLine(title=u'Bar')


alsoProvides(ISimpleBehavior, IFormFieldProvider)


class IListBehavior(form.Schema):

    dexteritytextindexer.searchable('list_field')

    list_field = schema.List(
         title=u'List field',
         value_type=schema.TextLine())


alsoProvides(IListBehavior, IFormFieldProvider)


class IIntBehavior(form.Schema):

    dexteritytextindexer.searchable('int_field')
    int_field = schema.Int(title=u'Int')


alsoProvides(IIntBehavior, IFormFieldProvider)


class IDictBehavior(form.Schema):

    dexteritytextindexer.searchable('dict_field')
    dict_field = schema.Dict(
        title=u'Dict field',
        value_type=schema.TextLine(),
        key_type=schema.TextLine())

alsoProvides(IDictBehavior, IFormFieldProvider)
