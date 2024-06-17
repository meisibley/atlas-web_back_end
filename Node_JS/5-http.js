/*create a small HTTP server using the http module:
It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /, it should display Hello Holberton School! in the page body
When the URL path is /students, it should display This is the list of our students
  followed by the same content as the file 3-read_file_async.js (with and without the database)
  - the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) - and they are not a valid student!*/
var http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(function (req, res) {
    if (req.method === 'GET') {
        if (req.url === '/') {
            res.write('Hello Holberton School!');
            res.end();
        } else if (req.url === '/students') {
            await countStudents(process.argv[2])
              .then((fileData) => {
                res.write('This is the list of our students\n');
                res.write(`Number of students: ${fileData.CS.num + fileData.SWE.num}\n`);
                res.write(`Number of students in CS: ${fileData.CS.num}. List: ${fileData.CS.list}\n`);
                res.write(`Number of students in SWE: ${fileData.SWE.num}. List: ${fileData.SWE.list}`);
                res.end();
            })
            .catch((err) => {
                res.write('This is the list of our students\n');
                res.end(err.message);
            });
        }
    }
}).listen(1245);

module.exports = app;
