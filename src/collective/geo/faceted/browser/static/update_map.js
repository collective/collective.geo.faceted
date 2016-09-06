jQuery(document).ready(function() {
  jQuery(Faceted.Events).bind(
    Faceted.Events.AJAX_QUERY_SUCCESS,
    update_map
  );
});

var geojson_data;

function update_map() {
  // alert('update map');
  json = $('#geojson').data('geojson');
  layername = $('h1.documentFirstHeading').html();
  if (typeof geojson_data !== 'undefined') {
    controllayers.removeLayer(geojson_data);
    geojson_data.clearLayers();
  }

  geojson_data = L.geoJson(json, {
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
  map.addLayer(geojson_data);
  controllayers.addOverlay(geojson_data, layername);

}
