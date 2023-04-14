#!/usr/bin/node
// JS script function that prints the factorial of the argument passed

function factorial (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (n <= 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
