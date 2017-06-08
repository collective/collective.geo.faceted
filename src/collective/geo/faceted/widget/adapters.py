# -*- coding: utf-8 -*-
""" Adapters
"""
from eea.facetednavigation.interfaces import IWidgetFilterBrains
from zope.interface import implementer

import Missing


@implementer(IWidgetFilterBrains)
class WidgetFilterBrains(object):
    """ Filter brains after query
    """

    def __init__(self, context):
        self.widget = context

    def __call__(self, brains, form):
        """ Filter brains
        """
        if set(['west', 'east', 'north', 'south']).issubset(form.keys()):
            north = float(form.get('north'))
            east = float(form.get('east'))
            south = float(form.get('south'))
            west = float(form.get('west'))
            for brain in brains:
                if brain.zgeo_geometry is not Missing.Value:
                    zgeo_geometry = brain.zgeo_geometry
                    geo_type = brain.zgeo_geometry.get('type', None)
                    if geo_type == 'Point':
                        lon, lat = zgeo_geometry['coordinates']
                        if south <= lat <= north and west <= lon <= east:
                            yield brain
                    elif geo_type in ['Polygon', 'Line']:
                        in_map = False
                        for lon, lat in zgeo_geometry['coordinates'][0]:
                            # see polygon if one of is point is in map
                            if south <= lat <= north and west <= lon <= east:
                                in_map = True
                        if in_map:
                            yield brain
