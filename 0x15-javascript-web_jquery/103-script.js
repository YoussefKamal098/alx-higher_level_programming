$(document).ready(function () {
  const languageInput = $('#language_code');
  const translateBtn = $('#btn_translate');

  function fetchTranslation () {
    const languageCode = languageInput.val();
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/';

    $.getJSON(apiUrl, { lang: languageCode }, function (json) {
      $.each(json, function (key, value) {
        console.log(key, value);
      });

      $('#hello').text(json.hello);
    });
  }

  translateBtn.click(fetchTranslation);
  languageInput.keyup(function (event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });
});
