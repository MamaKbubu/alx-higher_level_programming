#!/usr/bin/node
// This script writes that C is fun, you decide how many times(x)
//
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
