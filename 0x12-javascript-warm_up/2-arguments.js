#!/usr/bin/node
const pro = process.argv;
if (pro.length === 2) {
  console.log('No argument');
} else if (pro.length === 3) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
