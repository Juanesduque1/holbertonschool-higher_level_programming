#!/usr/bin/node
// JS script that prints two arguments passed to it

let firstVar;
let secondVar;

if (process.argv.slice(2) !== undefined) {
  firstVar = process.argv[2];
} else {
  firstVar = 'undefined';
}

if (process.argv.slice(3) !== undefined) {
  secondVar = process.argv[3];
} else {
  secondVar = 'undefined';
}

console.log(firstVar + ' is ' + secondVar);
