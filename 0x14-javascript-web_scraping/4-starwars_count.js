#!/usr/bin/node
// Write a script that prints the number of movies where the
// character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars
// API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this
// ID for filtering the result of the API
// You must use the module request
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    const wedgeMovies = movies.filter(movie =>
      movie.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${wedgeMovies.length}`);
  } else {
    console.log('character not found');
  }
});
