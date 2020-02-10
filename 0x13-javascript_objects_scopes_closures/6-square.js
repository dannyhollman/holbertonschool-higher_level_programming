#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    const array = [];
    for (let i = 0; i < this.width; i++) {
      array.push(c);
    }
    for (let i = 0; i < this.height; i++) {
      console.log(array.join(''));
    }
  }
}

module.exports = Square;
