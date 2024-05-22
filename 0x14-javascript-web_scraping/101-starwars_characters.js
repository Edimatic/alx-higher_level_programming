#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  getCharacters(0);
});

