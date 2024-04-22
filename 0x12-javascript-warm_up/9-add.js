#!/usr/bin/node

/**
 * add - Function to add two integers
 * @a: The first integer
 * @b: The second integer
 * Return:  {number} The sum of the two integers
 */
function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
