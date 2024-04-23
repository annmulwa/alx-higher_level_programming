#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const Completedtasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!Completedtasks[todo.userId]) {
        Completedtasks[todo.userId] = 1;
      } else {
        Completedtasks[todo.userId] += 1;
      }
    }
  });
  console.log(Completedtasks);
});
