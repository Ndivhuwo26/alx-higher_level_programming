#!/usr/bin/node
/* a script that prints two arguments passed to it, in the following format */
const args = process.argv.slice(2);

const arg1 = args[0] !== undefined ? args[0] : 'undefined';
const arg2 = args[1] !== undefined ? args[1] : 'undefined';

console.log(`${arg1} is ${arg2}`);
