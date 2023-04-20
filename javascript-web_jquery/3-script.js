#!/usr/bin/node
// JS script that updates color of the <header> tag to red using JQuery API

$(document).ready(function () {
  $('div#red_header').click(function () {
    $('header').addClass('red');
  });
});
