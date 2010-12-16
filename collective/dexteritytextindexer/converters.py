from Products.CMFCore.utils import getToolByName
from collective.dexteritytextindexer import interfaces
from five import grok
from plone.dexterity.interfaces import IDexterityContent
from zope.schema.interfaces import IField
from z3c.form.interfaces import IWidget
import logging


try:
    from plone.namedfile.interfaces import INamedFileField
except ImportError:
    HAS_NAMEDFILE = False
else:
    HAS_NAMEDFILE = True


LOGGER = logging.getLogger('collective.dexteritytextindexer')


class DefaultDexterityTextIndexFieldConverter(grok.MultiAdapter):
    """Fallback field converter which uses the rendered widget in display
    mode for generating a indexable string.
    """

    grok.provides(interfaces.IDexterityTextIndexFieldConverter)
    grok.adapts(IDexterityContent, IField, IWidget)

    def __init__(self, context, field, widget):
        self.context = context
        self.field = field
        self.widget = widget

    def convert(self):
        html = self.widget.render().strip()
        transforms = getToolByName(self.context, 'portal_transforms')
        stream = transforms.convertTo('text/plain', html)
        return stream.getData().strip()
