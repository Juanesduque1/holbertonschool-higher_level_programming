#!/usr/bin/node
// JS script that appends a <li> tag when clicking in the "add item" div

$(document).ready(function () {
  $('div#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
