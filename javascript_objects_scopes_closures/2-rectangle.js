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
};
