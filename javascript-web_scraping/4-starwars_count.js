#!/usr/bin/node
// JS script that counts apparences of an specific character

const request = require('request');
const characterID = 18;
const URL = process.argv[2];

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    let count = 0;

    data.results.forEach(film => {
      const hasCharacter = film.characters.some(character => character.includes(characterID));
      if (hasCharacter) {
        count++;
      }
    });
    console.log(count);
  }
});
