const fs = require('fs');

function countStudents(path) {
    let fileLine;
    try {
        fileLine = fs.readFileAsync(path, 'utf8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }
    console.log(`Number of students: ${fileLine.split('\n').length - 2}`);
    const CS = fileLine.split('\n').filter((line) => line.includes('CS')).length;
}