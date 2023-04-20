#!/usr/bin/node
// JS script that displays the status code of a GET request

const request = require('request');
const link = process.argv[2];

request.get(link, (error, code) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + code.statusCode);
  }
});
