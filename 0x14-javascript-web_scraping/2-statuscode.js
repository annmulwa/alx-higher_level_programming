#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
request.get(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
