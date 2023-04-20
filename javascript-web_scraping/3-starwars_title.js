#!/usr/bin/node
// JS script that displays title of a movie depending on its ID

const request = require('request');
const ID = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${ID}`;

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
