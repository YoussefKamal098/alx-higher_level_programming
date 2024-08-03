#!/usr/bin/node

/**
 * This script retrieves and counts the number of Star Wars movies that a specified character appears in.
 * The script uses the Star Wars API (https://swapi-api.alx-tools.com/api/films/) and the 'request' module.
 *
 * Usage:
 *    node script_name.js <API_URL>
 *
 * Example:
 *    node script_name.js https://swapi-api.alx-tools.com/api/films
 *
 * The script will fetch the data from the provided API URL and count the number of
 * movies where the character with ID 18 appears.
 */

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script_name.js <API_URL>');
  process.exit(1);
}

const STAR_WAR_API = process.argv[2];
const CHARACTER_ID = 18;

/**
 * Fetches data from a given URL.
 *
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<Object>} - A promise that resolves to the body data fetched from the URL.
 */
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
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
 * Counts the number of movies in which a specified character appears.
 *
 * @param {string} url -  The URL to fetch data from.
 * @param {number} characterId - The ID of the character to search for.
 * @returns {Promise<number>} - A promise that resolves to the number of movies the character appears in.
 */
async function countMoviesWithCharacterId (url, characterId) {
  try {
    const data = await fetchData(url);
    const movies = JSON.parse(data).results;

    return movies.reduce((count, currMovie) => {
      return count + currMovie.characters.reduce((count, currCharacter) => {
        return count + (currCharacter.includes(characterId) ? 1 : 0);
      }, 0);
    }, 0);
  } catch (error) {
    console.error('Error:', error.message);
    return 0;
  }
}

// Main execution
countMoviesWithCharacterId(STAR_WAR_API, CHARACTER_ID).then(moviesCount => {
  console.log(moviesCount);
}).catch(error => {
  console.error('Unhandled Error:', error.message);
});
