"""The ``searchable`` martian directive is used to mark a field as
searchable within a schema interface.
"""


from plone.directives.form.schema import FormMetadataListStorage
from zope.interface import Interface
from zope.interface.interfaces import IInterface
import martian


SEARCHABLE_KEY = u'collective.dexteritytextindexer.searchable'


class searchable(martian.Directive):
    """Directive used to mark a field as searchable.
    """

    scope = martian.CLASS
    store = FormMetadataListStorage()

    key = SEARCHABLE_KEY
    value = 'true'

    def factory(self, *args):
        """The searchable directive accepts as arguments one or more
        fieldnames (string) of fields which should be searchable.
        """
        if not args:
            raise TypeError('The searchable directive expects at '
                            'least one argument.')

        form_interface = Interface
        if IInterface.providedBy(args[0]):
            form_interface = args[0]
            args = args[1:]
        return [(form_interface, field, self.value) for field in args]
