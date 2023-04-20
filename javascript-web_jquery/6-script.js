#!/usr/bin/node
// JS script that updates the header text when clicking on it

$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
