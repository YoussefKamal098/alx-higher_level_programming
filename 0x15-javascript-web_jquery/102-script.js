$(document).ready(function () {
  const translateBtn = $('#btn_translate');

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/';

    $.getJSON(apiUrl, { lang: languageCode }, function (json) {
      $.each(json, function (key, value) {
        console.log(key, value);
      });

      $('#hello').text(json.hello);
    });
  }

  translateBtn.click(fetchTranslation);
});
