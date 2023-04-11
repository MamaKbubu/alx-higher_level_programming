#!/usr/bin/node
// This code can add two integers together
//
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(a), parseInt(b)));
