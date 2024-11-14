#!/usr/bin/node

const request = require('request');

const film = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${film}`;

function getCharacters () {
  request(url, (error, response, body) => {
    if (error) {
      console.log('Error:', error);
      return;
    }

    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      const characterLinks = data.characters;

      characterLinks.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.log('Error:', error);
            return;
          }

          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

getCharacters();
