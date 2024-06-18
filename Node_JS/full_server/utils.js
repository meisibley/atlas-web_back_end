const fs = require('fs');

async function readDatabase(path) {
  //read the database asynchronously, return a promise
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, fileData) => {
      if (err) {
        //When the file is not accessible, reject the promise with the error
        reject(new Error(`Cannot read database: ${err.message}`));
      } else {
        //return an object of arrays of the firstname of students per fields
        const students = fileData.trim().split('\n');
        const output = {};

        students.forEach((student) => {
          const [firstname, lastname, age, field] = student.split(',');
          if (!output[field]) {
            output[field] = [];
          }
          output[field].push(firstname);
        });
        resolve(output);
      }
    });
  });
}

module.exports = readDatabase;
