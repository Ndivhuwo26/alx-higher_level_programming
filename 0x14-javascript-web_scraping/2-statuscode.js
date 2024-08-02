#!/usr/bin/node
// a script that will  display the status code of a GET request.

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code:', response.statusCode);
});
