export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(inputName) {
    if (typeof inputName !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = inputName;
  }

  get name() {
    return this._name;
  }

  set length(inputLength) {
    if (typeof inputLength !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = inputLength;
  }

  get length() {
    return this._length;
  }

  set students(inputStudents) {
    if (!Array.isArray(inputStudents)) {
       throw TypeError('Students must be an array of strings');
    } else {
      inputStudents.forEach((eachStudent) => {
        if (typeof eachStudent !== 'string') {
          throw TypeError('Students must be an array of strings');
        }
      });
    }
    this._students = inputStudents;
  }

  get students() {
    return this._students;
  }  
}
