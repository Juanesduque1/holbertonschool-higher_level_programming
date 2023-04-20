#!/usr/bin/node
// JS script that counts number of tasks completed by user ID

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    const results = {};

    data.forEach(tasks => {
      if (tasks.completed) {
        if (results[tasks.userId]) {
          results[tasks.userId]++;
        } else {
          results[tasks.userId] = 1;
        }
      }
    });
    console.log(results);
  }
});
