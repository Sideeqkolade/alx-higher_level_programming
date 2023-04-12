#!/usr/bin/node

//  a script that prints My number: <first argument converted in integer>
//  If the argument can’t be converted to an integer, print “Not a number”
//  You must use console.log(...) to print all output

const arg1 = parseInt(process.argv[2]);
if (arg1) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
