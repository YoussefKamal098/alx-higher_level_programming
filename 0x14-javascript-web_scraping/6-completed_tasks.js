#!/usr/bin/node
/**
 * This script retrieves task data from a provided API URL and calculates the number of tasks assigned to each user.
 * It uses the `request` module to fetch data and performs the following steps:
 *
 * 1. Validates that the API URL is provided as a command-line argument.
 * 2. Fetches data from the specified URL.
 * 3. Groups the fetched task data by user ID.
 * 4. Filter out uncompleted tasks for each group.
 * 4. Transforms the grouped data to count the number of completed tasks per user.
 * 5. Outputs the completed task counts per user to the console.
 *
 * Usage:
 *    node script_name.js <API_URL>
 *
 * Example:
 *    node script_name.js https://jsonplaceholder.typicode.com/todos
 *
 * The script will fetch the task data from the given API URL and print an object where keys are user IDs
 * and values are the counts of tasks assigned to each user.
 */

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script_name.js <API_URL>');
  process.exit(1);
}

const JSONPLACEHOLDER_API = process.argv[2];

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
 * Groups an array of objects by a specified key.
 *
 * @param {Array<Object>} array - The array to group.
 * @param {Function} keyMapper - A function that returns the key to group by.
 * @returns {Object} - An object where keys are the grouping criteria and values are arrays of grouped items.
 */
function groupBy (array, keyMapper) {
  return array.reduce((groups, item) => {
    const key = keyMapper(item);
    (groups[key] || (groups[key] = [])).push(item);
    return groups;
  }, {});
}

/**
 * Transforms the values of an object based on a transformer function.
 *
 * @param {Object} obj - The object to transform.
 * @param {Function} transformer - A function to apply to each value.
 * @returns {Object} - A new object with transformed values.
 */
function transformValues (obj, transformer) {
  return Object.keys(obj).reduce((result, key) => {
    result[key] = transformer(obj[key]);
    return result;
  }, {});
}

/**
 * Fetches tasks data and calculates the number of tasks per user.
 *
 * @param {string} url - The URL to fetch tasks data from.
 * @returns {Promise<Object>} - A promise that resolves to an
 *      object with user IDs as keys and task counts as values.
 */
async function getTasksCountByUser (url) {
  try {
    const data = await fetchData(url);
    const tasks = JSON.parse(data);
    const groupedTasks = groupBy(tasks, task => task.userId);

    for (const key in groupedTasks) {
        groupedTasks[key] = groupedTasks[key].filter(task => task.completed);
    }

    return transformValues(groupedTasks, tasks => tasks.length);
  } catch (error) {
    console.error('Error:', error.message);
    return {};
  }
}

// Main execution
getTasksCountByUser(JSONPLACEHOLDER_API).then(tasks => {
  console.log(tasks);
}).catch(error => {
  console.error('Unhandled Error:', error.message);
});
