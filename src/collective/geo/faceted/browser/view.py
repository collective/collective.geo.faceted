# -*- coding: utf-8 -*-
from collective.geo.json.browser.jsonview import JsonFolderDocument


class MapView(JsonFolderDocument):

    def json(self):
        view = self.context.restrictedTraverse('faceted_query')
        brains = view.query(batch=False)
        self.set_brains(brains)
        json = self.get_json()
        return json

    def set_brains(self, brains):
        self.brains = brains

    def get_brains(self):
        """Needed by get_json method from collective.geo.json."""
        return self.brains
