#!/usr/bin/node
// JS script that reverses a list

exports.esrever = function (list) {
  // Function that reverses a list
  var newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
