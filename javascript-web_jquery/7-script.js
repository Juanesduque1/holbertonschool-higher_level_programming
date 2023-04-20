#!/usr/bin/node
// JS script that fetches the character name from an URL

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
