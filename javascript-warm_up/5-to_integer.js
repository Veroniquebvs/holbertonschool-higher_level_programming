#!/usr/bin/node

const args = process.argv.slice(2);
const data = args[0];
if (isNaN(parseInt(data))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(data, 10));
}
