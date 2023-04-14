#!/usr/bin/node
// JS script that prints the first argument passed

const [arg] = process.argv.slice(2);

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
