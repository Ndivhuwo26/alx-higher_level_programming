#!/usr/bin/node
//this script will  request The first argument to URL
onst request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  } else {
    console.error('Error: Status code', response.statusCode);
  }
});
