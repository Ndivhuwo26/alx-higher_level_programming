#!/usr/bin/node
/* script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer  */
const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg, 10);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
