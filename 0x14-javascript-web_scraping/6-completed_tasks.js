#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  let dict = {};
  for (const task of JSON.parse(body)) {
    if (task.completed == true) {
      if (!(task.userId in dict)) {
        dict[task.userId] = 1;
      } else {
        dict[task.userId] += 1;
      }
    }
  }
  console.log(dict);
});
