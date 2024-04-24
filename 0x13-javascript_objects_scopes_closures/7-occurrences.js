#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentValue) => {
    return accumulator + (currentValue === searchElement);
  }, 0);
};
