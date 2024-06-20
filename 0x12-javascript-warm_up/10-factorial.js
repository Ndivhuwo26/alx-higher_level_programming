#!/usr/bin/node
/* a script that computes and prints a factorial */
const args = process.argv.slice(2);
const input = parseInt(args[0]);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (input > 100000) {
  console.log('Input too large to compute factorial accurately.');
} else {
  // Compute and print the factorial
  const result = factorial(input);
  console.log(result);
}
