#!/usr/bin/node

//  a class Rectangle that defines a rectangle
//  You must use the class notation for defining your class
//  You must use the class notation for defining your class
//  Initialize the instance attribute width with the value of w
//  Initialize the instance attribute height with the value of h
//  If w or h is equal to 0 or not a positive integer, create an empty object
//  Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
