# -*- coding: utf-8 -*-
from collective.geo.json.browser.jsonview import JsonFolderDocument


class MapView(JsonFolderDocument):

    def json(self, folderContents):
        self.set_brains(folderContents)
        json = self.get_json()
        return json

    def set_brains(self, brains):
        self.brains = brains

    def get_brains(self):
        """Needed by get_json method from collective.geo.json."""
        return self.brains
