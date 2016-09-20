# -*- coding: utf-8 -*-
from collective.geo.leaflet.interfaces import IGeoMap
from eea.facetednavigation.config import ANNO_FACETED_LAYOUT
from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.annotation.interfaces import IAnnotations


class MapViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('mapviewlet.pt')

    def avaiable(self):
        if not getattr(self.context, 'layout', '') == 'facetednavigation_view':
            return False
        view_name = IAnnotations(self.context).get(
            ANNO_FACETED_LAYOUT, 'faceted-preview-items')
        if not view_name == 'faceted-map-view':
            return False
        return True

    @property
    def geomap(self):
        return IGeoMap(self.context)
