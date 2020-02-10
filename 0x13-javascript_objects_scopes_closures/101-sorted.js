#!/usr/bin/node

const data = require('./101-data.js');
const dict = data.dict;

const temp = {};
for (const key in dict) {
  const value = dict[key];
  if (!(value in temp)) {
    temp[value] = [key];
  } else {
    temp[value].push(key);
  }
}
console.log(temp);
