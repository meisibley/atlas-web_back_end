export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsLocat = students.filter((item) => item.location === city);
  
  // initial all students of the city grades to N/A
  for (const elem of studentsLocat) {
    elem.grade = 'N/A';
  }
  const studentsUpdateNewGrades = studentsLocat.map((item) => {
    for (const nGrade of newGrade) {
      // if the student's id is in newGrade, update it's grade
      if (item.id === nGrade.studentId) {
        item.grade = nGrade.grade;
      }
    }
    return studentsUpdateNewGrades;
  });
}
