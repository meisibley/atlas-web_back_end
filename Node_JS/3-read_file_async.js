const fs = require('fs').promises;

const countStudents = async (path) => {
    let fileLine;
    try {
        fileLine = await fs.readFile(path, 'utf8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }
    console.log(`Number of students: ${fileLine.split('\n').length - 2}`);
    //calculate student num: splite fileLine with '\n', get file line num, then minus 1 head line and 1 end empty line
    const allFields = fileLine.split('\n').map((line) => line.split(',')[3]);
    //get all field values
    const wantedFields = [...new Set(allFields)];
    //get only wanted fields values
    CSlist = CSlist.join(', ');
    SWElist = SWElist.join(', ');
    console.log(`Number of students in CS: ${CScount}. List: ${CSlist}`);
    console.log(`Number of students in SWE: ${SWEcount}. List: ${SWElist}`);
}

module.exports = countStudents;