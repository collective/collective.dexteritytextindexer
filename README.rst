Introduction
============

`collective.dexteritytextindexer` provides a dynamic SearchableText indexer for
dexterity content types. It makes it possible to index fields of multiple
behaviors as SearchableText.


Usage
=====

For enabling the indexer just add the behavior to the list of behaviors of your
content types.

In your *profiles/default/types/YOURTYPE.xml* add the behavior::

    <?xml version="1.0"?>
    <object name="example.conference.presenter" meta_type="Dexterity FTI"
       xmlns:i18n="http://xml.zope.org/namespaces/i18n"
       i18n:domain="example.conference">

     <!-- enabled behaviors -->
     <property name="behaviors">
         <element value="collective.dexteritytextindexer.behavior.IDexterityTextIndexer" />
     </property>

    </object>


Now you need to mark the fields you wan't to have in your SearchableText. This
is done with directives::

    from collective import dexteritytextindexer
    from plone.autoform.interfaces import IFormFieldProvider
    from plone.directives import form
    from zope import schema
    from zope.interface import alsoProvides

    class IMyBehavior(form.Schema):

        dexteritytextindexer.searchable('specialfield')
        specialfield = schema.TextField(title=u'Special field')

    alsoProvides(IMyBehavior, IFormFieldProvider)


Don't forget to grok your package in your ``configure.zcml``::

    <configure xmlns="http://namespaces.zope.org/zope"
               xmlns:grok="http://namespaces.zope.org/grok">

        <include package="five.grok" />
        <grok:grok package="." />

    </configure>

Your SearchableText indexer includes now your custom field on your behavior, as
soon you enable it in your content type, where `IDexterityTextIndexer` behavior
is enabled too.


Extending indexed data
======================

Sometimes you need to extend the SearchableText with additional data which is
not stored in a field. It's possible to register a named adapter which provides
additional data::

    from five import grok
    from collective import dexteritytextindexer

    class MySearchableTextExtender(grok.Adapter):
        grok.context(IMyBehavior)
        grok.name('IMyBehavior')
        grok.implements(dexteritytextindexer.IDynamicTextIndexExtender)

        def __init__(self, context):
            self.context = context

        def __call__(self):
            """Extend the searchable text with a custom string"""
            return 'some more searchable words'


This is a **named** adapter! This makes it possible to register multiple
extenders for the same object on different behavior interfaces. The name of
the adapter does not matter, but it's recommended to use the name of the
behavior (this may reduce conflicts).

If your behavior has a defined factory (which is not attribute storage), then
you need to define a marker interface and register the adapter on this marker
interface (dexterity objects do not provide behavior interfaces of behaviors,
which are not using attribute storage).


Credits
=======

Sponsered by `4teamwork`_.

 * `Jonas Baumann`_, author


.. _`4teamwork`: http://www.4teamwork.ch/
.. _`Jonas Baumann`: http://github.com/jone
