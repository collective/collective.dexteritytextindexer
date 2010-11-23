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
       i18n:domain="example.conference" xmlns:i18n="http://xml.zope.org/namespaces/i18n">

     <!-- enabled behaviors -->
     <property name="behaviors">
         <element value="collective.dexteritytextindexer.behavior.IDexterityTextIndexer" />
     </property>

    </object>


Now you need to mark the fields you wan't to have in your SearchableText. This
is done with directives::

    >>> from collective.dexteritytextindexer.directives import searchable
    >>> from plone.directives import form
    >>> from zope import schema
    >>>
    >>> class IMyBehavior(form.Schema):
    ...
    ...     searchable('specialfield')
    ...     specialfield = schema.TextField(title=u'Special field')

Don't forget to grok your package in your ``configure.zcml``::

    <configure xmlns="http://namespaces.zope.org/zope"
               xmlns:grok="http://namespaces.zope.org/grok">

        <include package="five.grok" />
        <grok:grok package="." />

    </configure>

Your SearchableText indexer includes now your custom field on your behavior, as soon
you enable it in your content type, where `IDexterityTextIndexer` behavior
is enabled too.
