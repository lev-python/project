$(document).ready(function(){
    $.ajax({
    method: "GET",
    url: "http://127.0.0.1:5000/"
  })
    .done(function( msg ) {
      alert( "Data Saved: " + msg );
    });
  });