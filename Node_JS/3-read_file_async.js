const fs = require('fs');

const countStudents = (path, printFlag = 1) => new Promise((resolve, reject) => {
//The function uses a Promise to handle asynchronous file reading and return the result.
  try {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) reject(Error('Cannot load the database'));
      else {
        const fileLine = data
          .split('\n')
          //filter out empty lines and each line has at least 4 values
          .filter((row) => row !== '' && row.split(',').length >= 4)
          //map each line to an array of comma separated values
          .map((line) => line.split(','))
          //slice the array to remove the header row
          .slice(1)
          //to group students by their fields
          //create an object where keys are fields and values are arrays of students firstnames for each subject
          .reduce((count, strValue) => {
            //the reducer accumulates an object lineCount and iterates through each student record strValue
            const lineCount = count;
            //it extracts the subject field from the last element of the student record array
            const field = strValue[strValue.length - 1];
            //it extracts the firstname from the first element
            const firstName = strValue[0];
            //it check if the subject key field already exists in the object
            //if it exists, push the current student fistname to the existing array for that subject
            //if not exist, create a new array with the student firstname for that subject
            if (typeof lineCount[field] === 'undefined') lineCount[field] = [firstName];
            else lineCount[field].push(firstName);

            return lineCount;
          }, {});

        //store the total count of students in each of fields and format the output to listOut
        let studentsCount = 0;
        let listOut = '';
        //for each of fields, output students count and list
        for (const field in fileLine) {
          if (fileLine.hasOwnProperty) {
            studentsCount += fileLine[field].length;
            listOut += `Number of students in ${field}: ${fileLine[field].length}. List: ${fileLine[field].join(', ')}\n`;
          }
        }
        //add total students count in the beginning
        listOut = (`Number of students: ${studentsCount}\n${listOut}`).slice(0, -1);
        //if printFlag is true, console.log
        if (printFlag) {
          const outPut = listOut.split('\n');
          for (const str of outPut) console.log(str);
        }
        resolve(listOut);
      }
    });
  } catch (err) {
    reject(Error('Cannot load the database'));
  }
});

module.exports = countStudents;