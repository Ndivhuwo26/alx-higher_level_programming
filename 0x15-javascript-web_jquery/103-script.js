// JavaScript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error: Could not fetch translation.');
    });
  }

  // Handle button click
  $('#btn_translate').click(fetchTranslation);

  // Handle Enter key press
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // Enter key code
      fetchTranslation();
    }
  });
});
