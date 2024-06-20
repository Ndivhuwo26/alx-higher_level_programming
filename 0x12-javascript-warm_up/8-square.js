#!/usr/bin/node
/* the  script that prints a square */

const args = process.argv.slice(2);
const size = args[0];

function printSquare (size) {
  if (isNaN(size)) {
    console.log('Missing size');
    return;
  }

  size = parseInt(size);

  if (size <= 0) {
    return;
  }

  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
printSquare(size);
