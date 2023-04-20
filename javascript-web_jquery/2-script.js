#!/usr/bin/node
// JS script that updates color of the <header> tag to red when user clicks on it

$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
