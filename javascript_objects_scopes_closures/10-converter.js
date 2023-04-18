#!/usr/bin/node
// JS script that prints number converted from base 10 to base passed as argument

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
