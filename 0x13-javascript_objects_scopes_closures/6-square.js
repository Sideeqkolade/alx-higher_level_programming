#!/usr/bin/node

//  a class Square that defines a square
//  and inherits from Square of 5-square.js
//  You must use the class notation for defining your class and extends
//  Create an instance method called charPrint(c)
//  that prints the rectangle using the character c
//  If c is undefined, use the character X

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += C;
      }
      console.log(rec);
    }
  }
}

module.exports = Square;
