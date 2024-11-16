#!/usr/bin/node
/**
 * fetches character names of starwars api movies
 */
const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api';
const resource = '/films/';
const id = process.argv[2];

const url = `${URL}${resource}${id || ''}`;

async function getCharacterNames(url) {
  try {
    const { body } = await fetch(url);
    for (const character of body.characters) {
      const { body } = await fetch(character);
      console.log(body.name);
    }
  } catch (err) {
    throw new Error(err);
  }
}

function fetch(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject({ code: res.statusCode, err });
      } else {
        resolve({ code: res.statusCode, body: JSON.parse(body) });
      }
    });
  });
}

getCharacterNames(url);
