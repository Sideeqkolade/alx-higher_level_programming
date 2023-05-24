#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dc = data.characters;
  for (const i of dc) {
    request.get(i, (error, response, body1) => {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
