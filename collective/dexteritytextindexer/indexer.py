from Products.CMFCore.utils import getToolByName
from ZODB.POSException import ConflictError
from collective.dexteritytextindexer.behavior import IDexterityTextIndexer
from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from five import grok
from plone.dexterity.utils import iterSchemata
from plone.indexer import indexer
from plone.namedfile.interfaces import INamedFileField
from zope import schema
from zope.app.component.hooks import getSite
from zope.component import getAdapters
from zope.interface import Interface
import logging


LOGGER = logging.getLogger('collective.dexteritytextindexer')


class IDynamicTextIndexExtender(Interface):
    """Adapter interface for a named adapter which extends the dynamic
    text indexer.
    """


@indexer(IDexterityTextIndexer)
def dynamic_searchable_text_indexer(obj):
    """Dynamic searchable text indexer.
    """

    indexed = []

    for storage, fields in get_searchable_contexts_and_fields(obj):
        for field in fields:
            value = field.get(storage)
            if not value:
                continue

            if INamedFileField.providedBy(field):
                value = get_transformed_file(value)

            if isinstance(value, tuple) or isinstance(value, list):
                for subval in value:
                    if isinstance(subval, unicode):
                        subval = subval.encode('utf-8')
                    indexed.append(subval)

            elif isinstance(value, dict):
                for subval in value.values():
                    if isinstance(subval, unicode):
                        subval = subval.encode('utf-8')
                    indexed.append(subval)

            elif isinstance(value, unicode):
                indexed.append(value.encode('utf-8'))

            elif isinstance(value, str):
                indexed.append(value)

            elif value:
                indexed.append(str(value))

    for name, adapter in getAdapters((obj, ), IDynamicTextIndexExtender):
        extended_value = adapter()
        if not extended_value:
            continue
        if isinstance(extended_value, unicode):
            extended_value = extended_value.encode('utf-8')
        indexed.append(extended_value)

    return ' '.join(indexed)

grok.global_adapter(dynamic_searchable_text_indexer, name='SearchableText')


def get_searchable_contexts_and_fields(obj):
    """Returns a generator of tuples, which contains a storage object for
    each schema (adapted `obj`) and a list of fields on this schema which
    are searchable.
    """

    for schemata in iterSchemata(obj):
        fields = []
        tagged_values = schemata.queryTaggedValue(SEARCHABLE_KEY)
        if not tagged_values:
            continue

        for i, name, v in tagged_values:
            fields.append(schema.getFields(schemata).get(name))

        if fields:
            storage = schemata(obj)
            yield storage, fields


def get_transformed_file(data):
    """Transforms field data to text for indexing safely.
    """
    transforms = getToolByName(getSite(), 'portal_transforms')

    if transforms._findPath(data.contentType, 'text/plain'):
        return ''

    try:
        return transforms.convertTo(
            'text/plain', data.data, mimetype=data.contentType,
            filename=data.filename)
    except (ConflictError, KeyboardInterrupt):
        raise
    except Exception, e:
        LOGGER.error('Error while trying to convert file contents '
                     'to "text/plain": %s' % str(e))
