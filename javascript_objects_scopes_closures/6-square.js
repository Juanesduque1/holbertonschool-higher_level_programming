#!/usr/bin/node
// JS script that creates a class 'Square' that inherits from 'Rectangle'
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint (c) {
    // Method that prints a square of 'c' character
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
