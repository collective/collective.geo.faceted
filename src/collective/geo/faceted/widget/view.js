Faceted.BoundsWidget = function(wid){
  self = this;
  this.wid = wid;
  this.widget = jQuery('#' + wid + '_widget');
  self.init();
  map.on('moveend',
    function (e) {
      self.do_query();
    }
  );
}

Faceted.BoundsWidget.prototype = {
  init: function(){
    bounds = map.getBounds();
    north = bounds.getNorth();
    east = bounds.getEast();
    south = bounds.getSouth();
    west = bounds.getWest();
    Faceted.Query['north'] = north;
    Faceted.Query['east'] = east;
    Faceted.Query['south'] = south;
    Faceted.Query['west'] = west;
  },
  do_query: function(){
    this.init();
    Faceted.Form.do_query('north', Faceted.Query['north']);
    Faceted.Form.do_query('east', Faceted.Query['east']);
    Faceted.Form.do_query('south', Faceted.Query['south']);
    Faceted.Form.do_query('west', Faceted.Query['west']);
  },
}

Faceted.initializeBoundsWidget = function(evt){
  i = 0;
  jQuery('div.faceted-bounds-widget').each(function(){
    // get only first widget if there are mutliple widgets
    if (i > 1){
      return
    }
    var wid = jQuery(this).attr('id');
    wid = wid.split('_')[0];
    Faceted.Widgets[wid] = new Faceted.BoundsWidget(wid);
  });
};

jQuery(document).ready(function(){
  jQuery(Faceted.Events).bind(
    Faceted.Events.INITIALIZE,
    Faceted.initializeBoundsWidget);
});
