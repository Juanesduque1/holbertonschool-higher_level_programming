#!/usr/bin/node
// JS script that prints 'x' times a string

const x = process.argv[2];

if (x !== undefined) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
