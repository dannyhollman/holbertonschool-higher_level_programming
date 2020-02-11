#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, contents) => {
  if (err) {
    console.log(err);
  } else {
    console.log(contents.trim());
  }
});
