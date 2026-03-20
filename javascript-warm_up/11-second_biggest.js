#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log('0');
} else {
  const newNumber = args.map(i => Number(i));
  let max = -Infinity;
  let secondMax = -Infinity;
  for (let n = 0; n < newNumber.length; n++) {
    const num = newNumber[n];
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
