#!/usr/bin/node

/**
 * This script retrieves data from a given API URL and writes the fetched data to a specified file.
 * The script uses the 'request' module for HTTP requests and the 'fs' module for file operations.
 *
 * Usage:
 *    node script_name.js <API_URL> <FILE_PATH>
 *
 * Example:
 *    node script_name.js https://swapi-api.alx-tools.com/api/films ./output.txt
 *
 * The script fetches data from the provided API URL and saves it to the specified file.
 */

const fs = require('fs');
const request = require('request');

// Check if the required arguments are provided
if (process.argv.length < 4) {
  console.error('Usage: node script_name.js <API_URL> <FILE_PATH>');
  process.exit(1);
}

const STAR_WAR_API = process.argv[2];
const FILE_PATH = process.argv[3];

/**
 * Fetches data from a given URL.
 *
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<string>} - A promise that resolves to the body data fetched from the URL.
 */
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error(`Network error: ${error.message}`));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load page, status code: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

/**
 * Writes content to a specified file.
 *
 * @param {string} filepath - The path of the file.
 * @param {string} content - The content to write to the file.
 */
function writeToFile (filepath, content) {
  fs.writeFile(filepath, content, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err.message}`);
    } else {
      // console.log('Content has been written successfully!');
    }
  });
}

// Main execution
fetchData(STAR_WAR_API).then(data => {
  writeToFile(FILE_PATH, data);
}).catch(err => {
  console.error(`Error: ${err.message}`);
});
