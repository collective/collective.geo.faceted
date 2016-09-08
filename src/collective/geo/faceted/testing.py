# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.geo.faceted


class CollectiveGeoFacetedLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.geo.faceted, name='testing.zcml')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geo.faceted:testing')


COLLECTIVE_GEO_FACETED_FIXTURE = CollectiveGeoFacetedLayer()


COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEO_FACETED_FIXTURE,),
    name='CollectiveGeoFacetedLayer:IntegrationTesting'
)


COLLECTIVE_GEO_FACETED_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEO_FACETED_FIXTURE,),
    name='CollectiveGeoFacetedLayer:FunctionalTesting'
)


COLLECTIVE_GEO_FACETED_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_GEO_FACETED_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveGeoFacetedLayer:AcceptanceTesting'
)
