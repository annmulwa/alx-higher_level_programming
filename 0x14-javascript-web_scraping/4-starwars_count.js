#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
let count = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
