#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  let count = 0;
  for (const movie of JSON.parse(body).results) {
    for (const actor of movie.characters) {
      if (actor.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
