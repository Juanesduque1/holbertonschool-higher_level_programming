#!/usr/bin/node
// JS script that creates a class 'Rectangle'

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h < 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // Method that prints the rectangle
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    // Method that rotates the rectangle attributes
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Method that multiplies width and height times 2
    this.height *= 2;
    this.width *= 2;
  }
};
