"""Dynamic SearchableText index for dexterity content types
"""

from collective.dexteritytextindexer import utils
from plone.app.dexterity.behaviors.metadata import IBasic

import zope.deferredimport


zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.interfaces',
    'IDynamicTextIndexExtender', 'IDexterityTextIndexFieldConverter')

zope.deferredimport.defineFrom(
    'collective.dexteritytextindexer.directives',
    'searchable', 'SEARCHABLE_KEY')

utils.searchable(IBasic, 'title')
utils.searchable(IBasic, 'description')
