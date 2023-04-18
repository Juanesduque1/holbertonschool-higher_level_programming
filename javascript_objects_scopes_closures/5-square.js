#!/usr/bin/node
// JS script that creates a class 'Square' that inherits from 'Rectangle'
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
