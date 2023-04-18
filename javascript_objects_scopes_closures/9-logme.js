#!/usr/bin/node
// JS script that prints number of arguments already printed

let count = 0;

exports.logMe = function (item) {
	//Function that prints number of arguments already printed
	console.log(count + ': ' + item)
	count++;
}
