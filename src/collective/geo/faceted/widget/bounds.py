# -*- coding: utf-8 -*-
from collective.geo.faceted import _
from collective.geo.faceted.widget.interfaces import IBoundsWidget
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from zope.interface import implementer

import logging


logger = logging.getLogger('collective.geo.faceted.')


@implementer(IBoundsWidget)
class Widget(AbstractWidget):
    """ Widget
    """
    # Widget properties
    widget_type = 'bounds'
    widget_label = _('Bounds selection')
    view_js = '++resource++collective.geo.faceted.widget.view.js'
    edit_js = '++resource++collective.geo.faceted.widget.edit.js'
    view_css = '++resource++collective.geo.faceted.widget.view.css'
    # edit_css = '++resource++collective.geo.faceted.widget.edit.css'

    index = ZopeTwoPageTemplateFile('bounds.pt', globals())
    edit_schema = AbstractWidget.edit_schema.copy()
    edit_schema['title'].default = _('Boundary Bounds')

    def __init__(self, context, request, data=None):
        super(Widget, self).__init__(context, request, data)
