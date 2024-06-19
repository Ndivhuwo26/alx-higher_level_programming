#!/usr/bin/node
/* script that prints x times “C is fun */
const x = parseInt(process.argv[2], 10);

if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  for (let i = 0; i < x; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trim());
}
