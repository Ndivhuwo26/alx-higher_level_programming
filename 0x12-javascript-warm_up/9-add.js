#!/usr/bin/node
/* script that prints the addition of 2 integers  */

const args = process.argv.slice(2);
function add (a, b) {
  return a + b;
}
if (args.length < 2 || isNaN(args[0]) || isNaN(args[1])) {
  console.log('NaN');
} else {
  const a = parseInt(args[0]);
  const b = parseInt(args[1]);
  const sum = add(a, b);
  console.log(sum);
}
