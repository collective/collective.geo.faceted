# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.geo.faceted.testing import COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.geo.faceted is properly installed."""

    layer = COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.geo.faceted is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.geo.faceted'))

    def test_browserlayer(self):
        """Test that ICollectiveGeoFacetedLayer is registered."""
        from collective.geo.faceted.interfaces import (
            ICollectiveGeoFacetedLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveGeoFacetedLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.geo.faceted'])

    def test_product_uninstalled(self):
        """Test if collective.geo.faceted is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.geo.faceted'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveGeoFacetedLayer is removed."""
        from collective.geo.faceted.interfaces import ICollectiveGeoFacetedLayer  # noqa
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveGeoFacetedLayer, utils.registered_layers())
