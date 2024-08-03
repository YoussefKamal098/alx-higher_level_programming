#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

// Define the API endpoint with the given movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie. Status code:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const movie = JSON.parse(body);

  console.log(movie);

  // Print the movie title
  console.log(movie.title);
});
