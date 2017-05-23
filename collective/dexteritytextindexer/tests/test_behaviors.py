# -*- coding: utf-8 -*-
"""Containing a tests suite for testing the behaviors.
"""

from collective.dexteritytextindexer import testing
from plone.testing import layered

import doctest
import unittest as unittest


def test_suite():
    """Test suite testing the behaviors with a doctest from behaviors.txt
    """
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('behaviors.rst'),
                layer=testing.TEXT_INTEXER_INTEGRATION_TESTING),
    ])
    return suite
