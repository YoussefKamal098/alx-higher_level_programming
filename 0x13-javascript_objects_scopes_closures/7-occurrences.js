#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((accumulator, currentValue) => {
    return accumulator + currentValue === searchElement;
  }, 0);

  return count;
};
