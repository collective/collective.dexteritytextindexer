import unittest2 as unittest
import doctest
from plone.testing import layered
from collective.dexteritytextindexer.testing import TEXT_INTEXER_INTEGRATION_TESTING


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('behaviors.txt'),
                layer=TEXT_INTEXER_INTEGRATION_TESTING),
    ])
    return suite
