#!/usr/bin/node

/**
 * addMeMaybe - Increments a number and calls a function
 * @number: The number to increment
 * @theFunction: The function to call
 */
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

module.exports = { addMeMaybe };
