#!/usr/bin/node
/* eslint-disable semi */
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
