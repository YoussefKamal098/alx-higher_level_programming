$(document).ready(function () {
  const movies = $('ul#list_movies');

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      movies.append(...data.results.map(movie => `<li>${movie.title}</li>`));
    },
    error: function (xhr, status, error) {
      console.log(xhr.responseText);
      console.log(status);
      console.log(error);
    }
  });
});
