#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg.length >= 2) {
  arg.sort((a, b) => b - a);
  console.log(arg[1]);
} else {
  console.log(0);
}
