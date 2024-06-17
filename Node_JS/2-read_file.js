const fs = require('fs');
//imports the fs (file system) module for file operations

function countStudents(path) {
    let fileLine;
    try {
        fileLine = fs.readFileSync(path, 'utf8');
        //stores the file content as a long string
    } catch (err) {
        throw new Error('Cannot load the database');
    }
    console.log(`Number of students: ${fileLine.split('\n').length - 2}`);
    //calculate student num: splite fileLine with '\n', get file line num, then minus 1 head line and 1 end empty line
    const CS = fileLine.split('\n').filter((line) => line.includes('CS')).length;
    const SWE = fileLine.split('\n').filter((line) => line.includes('SWE')).length;
    //how many students on field CS or SWE
    let CSstudent = fileLine.split('\n').filter((line) => line.includes('CS')).map((line) => line.split(',')[0]);
    let SWEstudent = fileLine.split('\n').filter((line) => line.includes('SWE')).map((line) => line.split(',')[0]);
    //filter only gets CS or SWE students, and get their firstname (first item in the array [0])
    CSstudent = CSstudent.join(', ');
    SWEstudent = SWEstudent.join(', ');
    console.log(`Number of students in CS: ${CS}. List: ${CSstudent}`);
    console.log(`Number of students in SWE: ${SWE}. List: ${SWEstudent}`);
}

module.exports = countStudents;
