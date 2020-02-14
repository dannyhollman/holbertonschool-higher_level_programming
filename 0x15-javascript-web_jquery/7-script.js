$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: (data) => {
      $('DIV#character').append(data.name);
    }
  });
});
