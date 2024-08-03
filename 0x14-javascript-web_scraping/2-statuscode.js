#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  console.log('code:', response.statusCode);
});
