"""Dynamic SearchableText index for dexterity content types
"""

import zope.deferredimport

zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.interfaces',
    'IDynamicTextIndexExtender', 'IDexterityTextIndexFieldConverter')

zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.directives',
    'searchable', 'SEARCHABLE_KEY')
