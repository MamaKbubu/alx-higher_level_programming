#!/usr/bin/node
// This code passes 2 arguments except 1
//
console.log(parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
