"""Containing a tests suite for testing the behaviors.
"""

import unittest2 as unittest
import doctest
from plone.testing import layered
from collective.dexteritytextindexer import testing


def test_suite():
    """Test suite testing the behaviors with a doctest from behaviors.txt
    """
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('behaviors.txt'),
                layer=testing.TEXT_INTEXER_INTEGRATION_TESTING),
    ])
    return suite
