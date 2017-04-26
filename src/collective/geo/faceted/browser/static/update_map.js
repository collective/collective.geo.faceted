var markers;

jQuery(document).ready(function() {
  markers = new L.MarkerClusterGroup();;
  jQuery(Faceted.Events).bind(
    Faceted.Events.AJAX_QUERY_SUCCESS,
    update_map
  );
});

var geojson_layer;

function update_map() {
  var json_container = $('#geojson');
  if (json_container.length == 0) {
    $('#map-viewlet').hide();
    return
  } else {
    $('#map-viewlet').show();
  }
  json = json_container.data('geojson');
  layername = $('h1.documentFirstHeading').html();
  if (typeof geojson_layer !== 'undefined') {
    geojson_layer.clearLayers();
  }
  if (typeof markers !== 'undefined') {
    controllayers.removeLayer(markers);
    markers.clearLayers();
  }

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
