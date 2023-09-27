#!/usr/bin/node
dict = require('./101-data.js').dict;
const newDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (newDict[dict[occurences]] === undefined) {
    newDict[dict[occurences]] = [occurences];
  } else {
    newDict[dict[occurences]].push(occurences);
  }
});
console.log(newDict);
