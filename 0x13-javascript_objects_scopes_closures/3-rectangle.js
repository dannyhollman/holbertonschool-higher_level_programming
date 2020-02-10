#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || w < 1) {
      return;
    } else if (typeof h !== 'number' || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const array = [];
    for (let i = 0; i < this.width; i++) {
      array.push('X');
    }
    for (let i = 0; i < this.height; i++) {
      console.log(array.join(''));
    }
  }
};
