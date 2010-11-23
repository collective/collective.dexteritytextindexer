from plone.indexer import indexer
from collective.dexteritytextindexer.behavior import IDexterityTextIndexer
from five import grok


@indexer(IDexterityTextIndexer)
def dynamic_searchable_text_indexer(obj):
    pass

grok.global_adapter(dynamic_searchable_text_indexer, name='SearchableText')


