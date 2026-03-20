#!/usr/bin/node

const args = process.argv.slice(2);
const data = Number(args[0]);
if (isNaN(Number(data))) {
  console.log('1');
} else {
  function factorial (data) {
    let result = 1;
    for (let i = 1; i <= data; i++) {
      result *= i;
    }
    return result;
  }
  console.log(factorial(data));
}
