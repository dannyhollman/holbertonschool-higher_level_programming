#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
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
