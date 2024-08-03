#!/usr/bin/node

/**
 * This script retrieves and prints the names of characters from a specific Star Wars movie.
 * The script uses the Star Wars API (https://swapi-api.hbtn.io/api/films/) and the 'request' module.
 *
 * Usage:
 *    node script_name.js <movie_id>
 *
 * Example:
 *    node script_name.js 1
 *
 * The script will fetch the data for the specified movie ID and list the names of
 * all characters appearing in the movie.
 */

const request = require('request');

// Check if the movie ID is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: node script_name.js <movie_id>');
  process.exit(1);
}

const STAR_WAR_API = 'https://swapi-api.hbtn.io/api/films/';
const MOVIE_ID = parseInt(process.argv[2]);

// Validate the movie ID argument
if (Number.isNaN(MOVIE_ID)) {
  console.error('Usage: node script_name.js <movie_id>');
  process.exit(1);
}

/**
 * Fetches data from a given URL.
 *
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<string>} - A promise that resolves to the body data fetched from the URL.
 */
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load page, status code: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

/**
 * Fetches the names of characters appearing in a specific Star Wars movie.
 *
 * @param {number} movieId - The ID of the movie to fetch character names from.
 * @returns {Promise<string[]>} - A promise that resolves to an array of character names.
 */
async function fetchMovieCharacters (movieId) {
  try {
    const data = await fetchData(`${STAR_WAR_API}${movieId}`);
    const movie = JSON.parse(data);
    const characterNames = [];

    for (const characterApi of movie.characters) {
      const characterData = await fetchData(characterApi);
      characterNames.push(JSON.parse(characterData).name);
    }

    return characterNames;
  } catch (error) {
    console.error('Error:', error.message);
    return [];
  }
}

// Main execution: Fetch and print the character names for the specified movie ID
fetchMovieCharacters(MOVIE_ID).then((characters) => {
  console.log(characters.join('\n'));
}).catch((error) => {
  console.error('Unhandled Error:', error.message);
});
