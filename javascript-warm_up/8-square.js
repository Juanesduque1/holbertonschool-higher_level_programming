#!/usr/bin/node
// JS script that prints a square of x times 'x'

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
