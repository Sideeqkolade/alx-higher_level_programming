#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API URL
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode !== 200) {
    console.log('Unable to fetch the task data.');
  }

  // Parse the response body
  const tasks = JSON.parse(body);

  // Create an object to store the task counts by user ID
  const taskCounts = {};

  // Count the completed tasks by user ID
  tasks.forEach(task => {
    if (task.completed) {
      if (taskCounts[task.userId]) {
        taskCounts[task.userId]++;
      } else {
        taskCounts[task.userId] = 1;
      }
    }
  });

  // Print the task counts for users with completed tasks in dictionary format
  console.log(taskCounts);
});
