# -*- coding: utf-8 -*-
from collective.geo.faceted.testing import COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING  # noqa
from collective.geo.faceted.widget.adapters import WidgetFilterBrains
from collective.geo.faceted.widget.bounds import Widget
from collective.geo.geographer.interfaces import IWriteGeoreferenced
from eea.facetednavigation.widgets.storage import Criterion
from plone import api
from zope.component import getMultiAdapter

import unittest


class TestWidget(unittest.TestCase):

    layer = COLLECTIVE_GEO_FACETED_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.folder = api.content.create(
            container=self.portal,
            id='folder',
            type='Folder'
        )
        subtyper = getMultiAdapter(
            (self.folder, self.request), name=u'faceted_subtyper'
        )
        subtyper.enable()

    def test_bounds_widget_template(self):
        data = Criterion()
        widget = Widget(self.folder, self.request, data=data)
        self.assertIn('style="display: none"', widget.index())
        self.assertIn('faceted-bounds-widget', widget.index())

    def test_bounds_widget_adapter(self):
        # data = Criterion()
        form = {
            'north': '51.00000',
            'east': '6.000',
            'south': '49.000',
            'west': '5.000'
        }
        widget = WidgetFilterBrains(self.folder)
        # document and event have ICoordinates behavior
        event = api.content.create(
            container=self.portal,
            id='event',
            type='Event'
        )
        doc = api.content.create(
            container=self.portal,
            id='doc',
            type='Document'
        )
        geo_doc = IWriteGeoreferenced(doc)
        geo_event = IWriteGeoreferenced(event)
        geo_doc.setGeoInterface('Point', (5.583, 50.633))
        geo_event.setGeoInterface('Point', (5.73, 50.933))
        doc.reindexObject(idxs=['zgeo_geometry', 'collective_geo_styles'])
        event.reindexObject(idxs=['zgeo_geometry', 'collective_geo_styles'])
        # import ipdb; ipdb.set_trace()
        portal_catalog = api.portal.get_tool('portal_catalog')
        query = {}
        query['portal_type'] = ['Event', 'Document']
        brains = portal_catalog(query)
        gen = widget(brains, form)
        geo_brains = [g for g in gen]
        self.assertEqual(len(geo_brains), 2)

        geo_event.setGeoInterface('Point', (6.73, 50.933))
        event.reindexObject(idxs=['zgeo_geometry', 'collective_geo_styles'])
        brains = portal_catalog(query)
        gen = widget(brains, form)
        geo_brains = [g for g in gen]
        self.assertEqual(len(geo_brains), 1)

        geo_doc.setGeoInterface('Point', (5.583, 52.633))
        doc.reindexObject(idxs=['zgeo_geometry', 'collective_geo_styles'])
        brains = portal_catalog(query)
        gen = widget(brains, form)
        geo_brains = [g for g in gen]
        self.assertEqual(len(geo_brains), 0)
