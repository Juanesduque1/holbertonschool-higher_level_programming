#!/usr/bin/node
// JS script that updates color of the <header> tag to red or green using JQuery API

$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
