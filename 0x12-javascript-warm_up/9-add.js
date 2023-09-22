#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg = process.argv;

console.log(add(parseInt(arg[2]), parseInt(arg[3])));
// const num1 = parseInt(arg[2]);
// const num2 = parseInt(arg[3]);
// console.log(add(num1, num2));
