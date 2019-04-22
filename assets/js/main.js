require('expose-loader?$!jquery');

window.$ = $;
window.jQuery = $;

$(document).ready(function(){
  if($('#flash').length) {
    $('#flash').css({opacity: 1});
  };
});
