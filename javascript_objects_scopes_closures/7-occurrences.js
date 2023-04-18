#!/usr/bin/node
// JS script that counts the occurrences of an item in a list

exports.nbOccurences = function (list, SearchElement) {
  // Function that counts the occurrences of an elements in a list
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === SearchElement) {
      count += 1;
    }
  }
  return count;
};
