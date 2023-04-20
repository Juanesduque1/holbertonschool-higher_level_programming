#!/usr/bin/node
// JS script that stores the content of a webpage into a file

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const filePath = process.argv[3];

request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, error => {
      if (error) {
        console.error(error);
      }
    });
  }
});
