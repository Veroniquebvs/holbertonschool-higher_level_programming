#!/usr/bin/node

const args = process.argv.slice(2);
const a = args[0];
const b = args[1];

if (isNaN(Number(a)) || isNaN(Number(b))) {
  console.log('NaN');
} else {
  function add (a, b) {
    console.log(a + b);
  }
  add(Number(a), Number(b));
}
