from plone.directives.form.schema import TEMP_KEY
from collective.dexteritytextindexer.directives import SEARCHABLE_KEY

def searchable(iface, field_name):
    """ 
        mark a field in existing iface as searchable 
    """
    store = iface.queryTaggedValue(SEARCHABLE_KEY)
    if store is None:
        store = []
    store.append((iface, field_name, 'true'))
    iface.setTaggedValue(SEARCHABLE_KEY, store)
