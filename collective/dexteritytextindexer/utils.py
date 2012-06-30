from collective.dexteritytextindexer.directives import SEARCHABLE_KEY
from zope import schema


def searchable(iface, field_name):
    """
        mark a field in existing iface as searchable
    """

    if schema.getFields(iface).get(field_name) is None:
        dottedname = '.'.join((iface.__module__, iface.__name__))
        raise AttributeError('%s has no field "%s"' % (
                dottedname, field_name))

    store = iface.queryTaggedValue(SEARCHABLE_KEY)
    if store is None:
        store = []
    store.append((iface, field_name, 'true'))
    iface.setTaggedValue(SEARCHABLE_KEY, store)
