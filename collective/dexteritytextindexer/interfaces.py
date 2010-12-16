from zope.interface import Interface


class IDexterityTextIndexFieldConverter(Interface):
    """Interface for a multi-adapter which converts the field value of the
    adapted field into a human readable, translated text for indexing in
    the searchable text index.
    """

    def __init__(context, field, widget):
        """The multi-adpater adapts the context, the field and the widget.
        """

    def convert():
        """Returns a string containing the words to index. Translatable
        Message-objects are already translated into normal strings. On a
        multi-language site the
        """


class IDynamicTextIndexExtender(Interface):
    """Adapter interface for a named adapter which extends the dynamic
    text indexer.
    """
