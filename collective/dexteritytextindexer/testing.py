from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import setRoles
from zope.configuration import xmlconfig


class TextIndexerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.dexteritytextindexer
        xmlconfig.file('configure.zcml', collective.dexteritytextindexer,
                       context=configurationContext)
        import collective.dexteritytextindexer.tests
        xmlconfig.file('configure.zcml',
                       collective.dexteritytextindexer.tests,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        setRoles(portal, TEST_USER_NAME, ['Manager'])


TEXT_INDEXER_FIXTURE = TextIndexerLayer()
TEXT_INTEXER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TEXT_INDEXER_FIXTURE,),
    name="collective.dexteritytextindexer:Integration")
