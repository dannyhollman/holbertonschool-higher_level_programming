$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: (data) => {
      for (const movie of data.results) {
        $('UL#list_movies').append(movie.title);
      }
    }
  });
});
