# -*- coding: utf-8 -*-
from collective.geo.faceted.testing import COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING  # noqa
from eea.facetednavigation.interfaces import IFacetedNavigable
from plone import api
from zope.interface import directlyProvides

import unittest


class TestView(unittest.TestCase):

    layer = COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_map_view(self):
        coll = api.content.create(
            type='Collection', container=self.portal, id='collection')
        view = coll.restrictedTraverse('faceted-single-map-view')
        directlyProvides(coll, IFacetedNavigable)
        json = view.json()
        self.assertEqual(
            json, '{"type": "FeatureCollection", "features": [], "title": ""}')
        self.assertEqual(len(view.get_brains()), 7)
