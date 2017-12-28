# -*- coding: utf-8 -*-
from collective.geo.faceted import _
from collective.geo.faceted.widget.interfaces import IBoundsWidget
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget
from eea.facetednavigation import EEAMessageFactory as EEAMF
from zope.interface import implementer

try:
    AbstractWidget.edit_schema
except AttributeError:
    HAS_EEA10 = True
    from zope import schema
    from z3c.form import field
    from eea.facetednavigation.widgets import ViewPageTemplateFile
    from eea.facetednavigation.widgets.interfaces import ISchema
    from eea.facetednavigation.widgets.interfaces import DefaultSchemata as DS
    from eea.facetednavigation.widgets.interfaces import LayoutSchemata
else:
    HAS_EEA10 = False
    from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

import logging


logger = logging.getLogger('collective.geo.faceted.')


if HAS_EEA10 is True:
    class IBoundsSchema(ISchema):
        title = schema.TextLine(
            title=EEAMF(u"Friendly name"),
            description=EEAMF(u"Title for widget to display in view page"),
            default=_('Bounds selecton'),
        )

    class BoundsDefaultSchemata(DS):
        fields = field.Fields(IBoundsSchema).select(
            u'title',
            u'default',
            u'index'
        )

    @implementer(IBoundsWidget)
    class Widget(AbstractWidget):
        """ Widget
        """
        # Widget properties
        widget_type = 'bounds'
        widget_label = _('Bounds selection')

        groups = (
            BoundsDefaultSchemata,
            LayoutSchemata,
        )

        index = ViewPageTemplateFile('bounds.pt')

        def __init__(self, context, request, data=None):
            super(Widget, self).__init__(context, request, data)

else:
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
