from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from collective.dexteritytextindexer.interfaces import INDEXER_NAMESPACE
from collective.dexteritytextindexer.interfaces import INDEXER_PREFIX
from plone.supermodel.parser import IFieldMetadataHandler
from plone.supermodel.utils import ns
from zope.interface import implements
from zope.interface import Interface


class IndexerSchema(object):
    """Support the indexer: namespace in model definitions.
    """

    implements(IFieldMetadataHandler)

    namespace = INDEXER_NAMESPACE
    prefix = INDEXER_PREFIX

    def _add_searchable(self, schema, value):
        tagged_value = schema.queryTaggedValue(SEARCHABLE_KEY, [])
        tagged_value.append(value)
        schema.setTaggedValue(SEARCHABLE_KEY, tagged_value)

    def read(self, fieldNode, schema, field):
        name = field.__name__
        searchable = fieldNode.get(ns('searchable', self.namespace))

        if searchable:
            value = (Interface, name, 'true')
            self._add_searchable(schema, value)

    def write(self, fieldNode, schema, field):
        name = field.__name__
        searchable = schema.queryTaggedValue(SEARCHABLE_KEY, [])
        field_names = [field[1] for field in searchable]

        if name in field_names:
            fieldNode.set(ns('searchable', self.namespace), 'true')
