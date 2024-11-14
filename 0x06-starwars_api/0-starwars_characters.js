#!/usr/bin/node

const request = require('request');

const film = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${film}`;

function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(new Error(`Request failed with status ${response.statusCode}`));
      }
    });
  });
}

async function getCharacters () {
  try {
    // Fetch the film data
    const filmData = await fetchUrl(url);
    const characterLinks = filmData.characters;

    const characterPromises = characterLinks.map(fetchUrl);

    const characters = await Promise.all(characterPromises);

    characters.forEach((character) => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

getCharacters();
