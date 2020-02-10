#!/usr/bin/node

const fs = require('fs');

const a = fs.readFileSync(process.argv[2]);
const b = fs.readFileSync(process.argv[3]);
const c = a + b;

fs.writeFile(process.argv[4], c, (err) => {
  if (err) throw err;
});
