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


Now you need to mark the fields you want to have in your SearchableText. This
is done with directives::

    from collective import dexteritytextindexer
    from plone.autoform.interfaces import IFormFieldProvider
    from plone.supermodel.model import Schema
    from zope import schema
    from zope.interface import alsoProvides

    class IMyBehavior(Schema):

        dexteritytextindexer.searchable('specialfield')
        specialfield = schema.Text(title=u'Special field')

    alsoProvides(IMyBehavior, IFormFieldProvider)

If you want to mark fields of an existing 3rd party behavior, it can be
done using this utility function::

    from plone.app.dexterity.behaviors.metadata import ICategorization
    from collective.dexteritytextindexer.utils import searchable

    searchable(ICategorization, 'categorization')

The `title` and `description` on `plone.app.dexterity`'s `IBasic` behavior
are marked as searchable by default.
For marking them as no longer searchable, there is a utility function::

    from plone.app.dexterity.behaviors.metadata import IBasic
    from collective.dexteritytextindexer.utils import no_longer_searchable

    no_longer_searchable(IBasic, 'title')

Alternatively, if you specified your model as a plone.supermodel XML model,
you can mark the field searchable that way::

    <model xmlns="http://namespaces.plone.org/supermodel/schema"
           xmlns:indexer="http://namespaces.plone.org/supermodel/indexer">
      <schema based-on="plone.supermodel.model.Schema">

          <field name="specialfield" type="zope.schema.TextLine"
                 indexer:searchable="true">
            <title>Special field</title>
          </field>

      </schema>
    </model>


Your SearchableText indexer includes now your custom field on your behavior, as
soon you enable it in your content type, where `IDexterityTextIndexer` behavior
is enabled too.


Registering a custom field converter
====================================

By default, a field is converted to a searchable text by rendering the widget
in display mode and transforming the result to text/plain. However, if you need
to convert your custom field in a different way, you only have to provide a
more specific converter multi-adapter.

Convert multi-adapter specification:

:Interface: `collective.dexteritytextindexer.IDexterityTextIndexFieldConverter`
:Discriminators: context, field, widget

Example::

    from collective.dexteritytextindexer.converters import DefaultDexterityTextIndexFieldConverter
    from collective.dexteritytextindexer.interfaces import IDexterityTextIndexFieldConverter
    from my.package.interfaces import IMyFancyField
    from plone.dexterity.interfaces import IDexterityContent
    from z3c.form.interfaces import IWidget
    from zope.component import adapts
    from zope.interface import implements

    class CustomFieldConverter(DefaultDexterityTextIndexFieldConverter):
        implements(IDexterityTextIndexFieldConverter)
        adapts(IDexterityContent, IMyFancyField, IWidget)

        def convert(self):
             # implement your custom converter
             # which returns a string at the end
             return ''

ZCML::

    <configure xmlns="http://namespaces.zope.org/zope">

        <adapter factory=".converters.CustomFieldConverter" />

    </configure>


There is already an adapter for converting NamedFiles properly. It's registered
only if `plone.namedfile` is installed.



Extending indexed data
======================

Sometimes you need to extend the SearchableText with additional data which is
not stored in a field. It's possible to register a named adapter which provides
additional data::

    from collective import dexteritytextindexer
    from zope.component import adapts
    from zope.interface import implements

    class MySearchableTextExtender(object):
        adapts(IMyBehavior)
        implements(dexteritytextindexer.IDynamicTextIndexExtender)

        def __init__(self, context):
            self.context = context

        def __call__(self):
            """Extend the searchable text with a custom string"""
            return 'some more searchable words'


ZCML::

    <configure xmlns="http://namespaces.zope.org/zope">

        <adapter factory=".indexer.MySearchableTextExtender"
                 name="IMyBehavior"
                 />

    </configure>


This is a **named** adapter! This makes it possible to register multiple
extenders for the same object on different behavior interfaces. The name of
the adapter does not matter, but it's recommended to use the name of the
behavior (this may reduce conflicts).

If your behavior has a defined factory (which is not attribute storage), then
you need to define a marker interface and register the adapter on this marker
interface (dexterity objects do not provide behavior interfaces of behaviors,
which are not using attribute storage).


Contributors
============

(In order of appearance)

- `Jonas Baumann <http://github.com/jone>`_
- `Philippe Gross <http://github.com/phgross>`_
- `Lukas Graf <http://github.com/lukasgraf>`_
- `Izhar Firdaus <http://github.com/kagesenshi>`_
- `Sune Broendum Woeller <http://github.com/sunew>`_
- `Nejc Zupan <http://github.com/zupo>`_
