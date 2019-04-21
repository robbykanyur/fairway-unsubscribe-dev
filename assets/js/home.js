function submitOnEnter(){
  $('.input').keypress(function(e) {
    if(e.which == 13) {
      $('form').submit();
      return false;
    };
  });
};

function trumpet(source_text, url){
  var url = url;
  var text = JSON.stringify(source_text);
  $.ajax({
    type: "POST",
    url: url,
    data: text,
    contentType: "application/json",
    dataType: 'json'
  }); 
};

function submitForm(e,unsubscribe_url,trumpet_url,home_url){
  $('#overlay').css({'opacity': 1});
  var unsubscribe_url = unsubscribe_url;
  var trumpet_url = trumpet_url;
  var home_url = home_url;
  $.ajax({
    type: "POST",
    url: unsubscribe_url,
    data: $('form').serialize(),
    success: function(data) {
      $('#overlay').css({'opacity': 0});
      $('#full-content').html('<h1>Success</h1><p>You have been successfully unsubscribed.</p>');
      var email = data['email'];
      var previously = data['previously'];
      if(previously === true) {
        var trumpet_text = '[WARNING] Multiple unsubscribes for ' + email + '.';
        trumpet(trumpet_text, trumpet_url);
      }
    },
    error: function(data) {
      $('#overlay').css({'opacity': 0});
      if(data.responseJSON) {
        email = data.responseJSON['email'];
        trumpet('[500] Unsubscribe attempt failed for ' + email + '.');
      };
      $('#full-content').html('<h1>Error</h1><p>There was an error processing your request. Please try again at a later time.</p><p class="margin-none"><a class="button button-primary" href="' + home_url + '">Try Again</a></p>');
    }
  });
  e.preventDefault();
};

$(document).ready(function(){
  submitOnEnter();
  window.submitForm = submitForm;
});

