Faceted.initializeBoundsWidget = function(evt){
  jQuery('div.faceted-bounds-widget').each(function(){
    this.wid = wid;
    this.widget = jQuery('#' + wid + '_widget');
    var wid = jQuery(this).attr('id');
    wid = wid.split('_')[0];
    // var widget = new Faceted.StringWidget(wid);
    // query = jQuery.param(Faceted.Query, traditional=true);
    // jQuery.bbq.pushState(query, 1);
  });
};

jQuery(document).ready(function(){
  jQuery(FacetedEdit.Events).bind(
    FacetedEdit.Events.INITIALIZE_WIDGETS,
    FacetedEdit.initializeBoundsWidget);
});
