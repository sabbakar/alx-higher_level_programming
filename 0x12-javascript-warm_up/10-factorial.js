#!/usr/bin/node
function fact (n) {
  if (isNaN(n) || n < 0) {
    return 1;
    // or if (Number.isNaN(n)) {
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
const arg = process.argv[2];
console.log(fact(arg));
