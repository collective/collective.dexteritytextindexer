import martian
from plone.directives.form.meta import FormSchemaGrokker
from collective.dexteritytextindexer.directives import searchable


class TextIndexerFormSchemaGrokker(FormSchemaGrokker):
    """Grok form schema hints
    """

    martian.directive(searchable)
