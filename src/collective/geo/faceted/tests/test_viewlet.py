# -*- coding: utf-8 -*-
from collective.geo.faceted.testing import COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING  # noqa
from collective.geo.leaflet import geomap
from eea.facetednavigation.config import ANNO_FACETED_LAYOUT
from plone import api
from Products.Five.browser import BrowserView
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import unittest


class TestViewlet(unittest.TestCase):
    """Test collective.geo.faceted map viewlet"""

    layer = COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def get_viewlet(self, context, manager_name, viewlet_name):
        # getting viewlet
        view = BrowserView(self.portal, self.request)
        manager = queryMultiAdapter(
            (context, self.request, view),
            IViewletManager,
            manager_name,
            default=None)
        self.assertIsNotNone(manager)
        manager.update()

        my_viewlet = [
            v for v in manager.viewlets if v.__name__ == viewlet_name]
        self.assertEqual(len(my_viewlet), 1)
        viewlet = my_viewlet[0]
        return viewlet

    def test_avaiable(self):
        context = self.portal
        viewlet = self.get_viewlet(
            context, 'plone.belowcontentbody', 'mapviewlet')
        self.assertFalse(viewlet.avaiable())

        coll = api.content.create(
            type='Collection', container=self.portal, id='collection')
        viewlet = self.get_viewlet(
            coll, 'plone.belowcontentbody', 'mapviewlet')
        subtyper = getMultiAdapter(
            (coll, self.request), name=u'faceted_subtyper')
        subtyper.enable()
        self.assertFalse(viewlet.avaiable())

        annotations = IAnnotations(coll)
        annotations.setdefault(ANNO_FACETED_LAYOUT, 'faceted-map-view')
        self.assertTrue(viewlet.avaiable())

    def test_geomap(self):
        context = self.portal
        viewlet = self.get_viewlet(
            context, 'plone.belowcontentbody', 'mapviewlet')
        self.assertTrue(isinstance(viewlet.geomap, geomap.GeoMap))
