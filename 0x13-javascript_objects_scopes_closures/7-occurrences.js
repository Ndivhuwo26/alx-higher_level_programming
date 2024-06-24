#!/usr/bin/node
/* a function that returns the number of occurrences in a list: */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
