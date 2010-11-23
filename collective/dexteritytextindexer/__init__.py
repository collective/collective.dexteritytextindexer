import zope.deferredimport

zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.indexer',
    'IDynamicTextIndexExtender')

zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.directives',
    'searchable', 'SEARCHABLE_KEY')
