#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).map(Number);
  const second = array.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
