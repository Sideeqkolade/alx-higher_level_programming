#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie where
// the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
// You must use the module request

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Film not found');
  }
});
