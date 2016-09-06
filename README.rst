.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/collective.geo.faceted.svg?branch=master
   :target: https://travis-ci.org/collective/collective.geo.faceted
.. image:: https://coveralls.io/repos/collective/collective.geo.faceted/badge.svg?branch=master
 :target: https://coveralls.io/github/collective/collective.geo.faceted?branch=master
 
==============================================================================
collective.geo.faceted
==============================================================================

This package add a map view for eea.facetednavigation.
It depends on collective.geo.leaflet and eea.facetednavigation.

When a criteria from facetednavigation is modified, a geojson is updated (thanks to collective.geo.json) and this geojson fill the map.

Features
--------

- Add a faceted view which put object with coordinates on a map.

.. image:: https://raw.githubusercontent.com/collective/collective.geo.faceted/master/docs/screenshot.png
    :alt: The map on a collection.
    :width: 1007
    :height: 1026
    :align: center

Installation
------------

Install collective.geo.faceted by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.geo.faceted


and then running ``bin/buildout``

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.geo.faceted/issues
- Source Code: https://github.com/collective/collective.geo.faceted

License
-------

The project is licensed under the GPLv2.
