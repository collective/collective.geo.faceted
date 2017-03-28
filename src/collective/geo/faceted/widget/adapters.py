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
                    lon, lat = brain.zgeo_geometry['coordinates']
                    if south <= lat <= north and west <= lon <= east:
                        yield brain
