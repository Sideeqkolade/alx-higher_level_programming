#!/usr/bin/node
<<<<<<< HEAD
// a script that prints a message depending of the number of arguments passed
// If no arguments are passed to the script, print “No argument”
// Otherwise, print “Arguments found”
// You must use console.log(...) to print all output
// You are not allowed to use var
=======

//  a script that prints a message
//  depending of the number of arguments passed
//  If no arguments are passed to the script, print “No argument”
//  Otherwise, print “Arguments found”
//  You must use console.log(...) to print all output
//  You are not allowed to use var

>>>>>>> 3f5946cfe719555c88f233fa6d5323fec3fecfdd
const arg = process.argv.slice(2);

if (arg.length === 0) {
  console.log('No argument');
} else if (arg.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
