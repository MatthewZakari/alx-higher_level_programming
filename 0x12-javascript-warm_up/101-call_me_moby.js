#!/usr/bin/node

/**
 * callMeMoby - Executes a function x times
 * @x: Number of times to execute the function
 * @theFunction: The function to execute
 */
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}

module.exports = { callMeMoby };
