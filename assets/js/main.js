require('expose-loader?$!jquery');
require('expose-loader?moment!moment');
require('expose-loader?validate!jquery-validation');

window.$ = $;
window.jQuery = $;
window.jQuery.validate = $.validate

$(document).ready(function(){
  if($('#flash').length) {
    $('#flash').css({opacity: 1});
  };
});
