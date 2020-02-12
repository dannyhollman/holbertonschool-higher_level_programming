#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
