# -*- coding: utf-8 -*-

from collective.geo.faceted import _
from collective.geo.faceted.widget.interfaces import IBoundsWidget
from eea.facetednavigation.widgets import ViewPageTemplateFile
from eea.facetednavigation.widgets.interfaces import DefaultSchemata
from eea.facetednavigation.widgets.interfaces import ISchema
from eea.facetednavigation.widgets.interfaces import LayoutSchemata
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget
from zope.interface import implementer

import logging


logger = logging.getLogger('collective.geo.faceted.')


class IBoundsSchema(ISchema):
    pass


@implementer(IBoundsWidget)
class Widget(AbstractWidget):
    """ Widget
    """
    # Widget properties
    widget_type = 'bounds'
    widget_label = _('Bounds selection')

    groups = (
        DefaultSchemata,
        LayoutSchemata,
    )

    index = ViewPageTemplateFile('bounds.pt')

    def __init__(self, context, request, data=None):
        super(Widget, self).__init__(context, request, data)
