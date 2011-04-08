"""Testing setup providing layers and fixtures
TextIndexerLayer                   basic text indexer layer
TEXT_INDEXER_FIXTURE               text indexer fixture
TEXT_INTEXER_INTEGRATION_TESTING   integration testing layer
"""

from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from zope.configuration import xmlconfig


class TextIndexerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """After setting up zope, load all necessary zcml files.
        """
        import collective.dexteritytextindexer
        xmlconfig.file('configure.zcml', collective.dexteritytextindexer,
                       context=configurationContext)
        import collective.dexteritytextindexer.tests
        xmlconfig.file('configure.zcml',
                       collective.dexteritytextindexer.tests,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        """After setting up plone, give Manager role to the test user.
        """
        setRoles(portal, TEST_USER_ID, ['Manager'])


TEXT_INDEXER_FIXTURE = TextIndexerLayer()
TEXT_INTEXER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TEXT_INDEXER_FIXTURE,),
    name="collective.dexteritytextindexer:Integration")
