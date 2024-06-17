/*create a small HTTP server using the http module:
It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /, it should display Hello Holberton School! in the page body
When the URL path is /students, it should display This is the list of our students
  followed by the same content as the file 3-read_file_async.js (with and without the database)
  - the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) - and they are not a valid student!*/
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(function (req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/students') {
    countStudents(process.argv[2], 0)
      .then((success) => {
        const outPut = `This is the list of our students\n${success}`;
        res.end(outPut);
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
