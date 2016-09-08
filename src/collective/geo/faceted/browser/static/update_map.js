jQuery(document).ready(function() {
  jQuery(Faceted.Events).bind(
    Faceted.Events.AJAX_QUERY_SUCCESS,
    update_map
  );
});

var geojson_layer;
var markers;

function update_map() {
  // alert('update map');
  json = $('#geojson').data('geojson');
  layername = $('h1.documentFirstHeading').html();
  if (typeof geojson_layer !== 'undefined') {
    // controllayers.removeLayer(geojson_layer);
    geojson_layer.clearLayers();
  }
  if (typeof markers !== 'undefined') {
    controllayers.removeLayer(markers);
    markers.clearLayers();
  }
  markers = new L.MarkerClusterGroup();

  geojson_layer = L.geoJson(json, {
    onEachFeature: function(feature, layer) {
      layer.bindPopup(
        '<a href="' + feature.properties.url + '" target="_blank">' +
        '<h3>' + feature.properties.title + '</h3>' +
        '</a>' +
        '<p>' + feature.properties.description + '</p>');
    },
    pointToLayer: function(feature, latlng) {
      //Extend the Default marker class
      var CustomIcon = L.Icon.Default.extend({
        options: {
          iconUrl: feature.style.image
        }
      });
      var customIcon = new CustomIcon();
      return L.marker(latlng, {
        icon: customIcon
      });
    }
  });
  markers.addLayer(geojson_layer);
  map.addLayer(markers);
  // map.addLayer(geojson_layer);
  controllayers.addOverlay(markers, layername);

}
