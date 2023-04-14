#!/usr/bin/node
// JS script function that adds two numbers

function add (a, b) {
  return a + b;
}

const addition = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(addition);
