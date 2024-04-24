#!/usr/bin/node
const { dict } = require('./101-data');

const usersByOccurrence = {};

Object.entries(dict).forEach(([userId, occurrence]) => {
  usersByOccurrence[occurrence] = usersByOccurrence[occurrence] || [];
  usersByOccurrence[occurrence].push(userId);
});

console.log(usersByOccurrence);
