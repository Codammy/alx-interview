#!/usr/bin/node
/**
 * fetches character names of starwars api movies
 */
const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api';
const resource = '/films/';
const id = process.argv[2];

const url = `${URL}${resource}${id || ''}`;

async function getCharacterNames (url) {
  try {
    const body = await fetch(url);
    const charactersPromise = body.characters.map((character) =>
      fetch(character)
    );
    const characters = await Promise.all(charactersPromise);
    characters.forEach(character => console.log(character.name));
  } catch (err) {
    throw new Error(err);
  }
}

function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

getCharacterNames(url);
