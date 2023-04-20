#!/usr/bin/node
// JS script that writes a string into a file

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
