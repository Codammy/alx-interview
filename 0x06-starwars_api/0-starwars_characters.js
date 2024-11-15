#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api';
const resource = '/films/';
const id = process.argv[2];

const uri = `${URL}${resource}${id || ''}`;

request(uri, function (error, response, body) {
  //   if (error) {
  //     throw new Error(error);
  //   }
  if (error || response.statusCode !== 200) {
    return;
  }
  const data = JSON.parse(body);
  let characters = [];
  if (id) {
    characters = data.characters;
  } else {
    data.results.forEach((movie) => {
      characters = [...characters, ...movie.characters];
    });
  }

  //   console.log(characters)

  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        // throw new Error(error);
        return;
      }
      const ch = JSON.parse(body);
      console.log(ch.name);
    });
  });
});
