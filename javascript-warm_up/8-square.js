#!/usr/bin/node

const args = process.argv.slice(2);
const data = args[0];
if (isNaN(Number(data))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < data; i++) {
    let row = '';
    for (let j = 0; j < data; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
