#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (arg) {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let y = 0; y < arg; y++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
