#!/usr/bin/node
// Read from file

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(data);
  }
});
