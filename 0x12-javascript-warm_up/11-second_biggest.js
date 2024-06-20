#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments */
function secondLargest (arr) {
  if (arr.length < 2) {
    return 0;
  }

  let first = -Infinity;
  let second = -Infinity;

  for (const num of arr) {
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num < first) {
      second = num;
    }
  }

  return second;
}

const args = process.argv.slice(2).map(Number);
const result = secondLargest(args);
console.log(result);
