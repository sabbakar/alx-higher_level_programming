#!/usr/bin/node
// import { argv } from 'node:process';
// const process = require('process');

// print process.argv
// process.argv.forEach((val, index) => {
// const pro = (`${index}: ${val}`);
// });
//
const pro = process.argv;
if (pro.length === 2) {
  console.log('No argument');
} else if (pro.length === 3) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
