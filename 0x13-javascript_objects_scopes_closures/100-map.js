#!/usr/bin/node

const data = require('./100-data.js');
const array = data.list;

let counter = 0;
const map1 = array.map(x => x * counter++);

console.log(array);
console.log(map1);
