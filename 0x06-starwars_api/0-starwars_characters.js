#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api';
const resource = '/films/';

const id = process.argv[2];

request(URL + resource + id, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        throw new Error(error);
      }
      const ch = JSON.parse(body);
      console.log(ch.name);
    });
  });
});
